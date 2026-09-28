import leitura


# Motivos de descarte (usados no relatório)
MOTIVO_SOLUCAO_NAO_FIX = "Solução diferente de FIX"
MOTIVO_DUPLICADO = "Ponto duplicado (mantido o registro FIX)"
MOTIVO_INCOMPLETO = "Registro incompleto (sem coordenadas ou solução)"


def _ponto_esta_completo(linha):
    este = linha.get("ESTE", "").strip()
    norte = linha.get("NORTE", "").strip()
    solucao = linha.get("SOLUCAO", "").strip()
    return bool(este and norte and solucao)


def _e_registro_vazio(linha):
    return all((valor or "").strip() == "" for valor in linha.values())


def classificar(linhas):
    aproveitados = []
    descartes = []
    pontos_vistos = {}  # PONTO -> índice em 'aproveitados'

    for linha in linhas:
        # 1) Linha totalmente vazia (ex.: linha em branco no CSV bruto)
        if _e_registro_vazio(linha):
            continue

        ponto = linha.get("PONTO", "").strip()
        solucao = linha.get("SOLUCAO", "").strip().upper()

        # 2) Registro incompleto (sem ESTE, NORTE ou SOLUCAO)
        if not _ponto_esta_completo(linha):
            descartes.append({**linha, "MOTIVO_DESCARTE": MOTIVO_INCOMPLETO})
            continue

        # 3) Solução diferente de FIX (FLOAT, etc.)
        if solucao != "FIX":
            descartes.append({**linha, "MOTIVO_DESCARTE": MOTIVO_SOLUCAO_NAO_FIX})
            continue

        # 4) Ponto duplicado: se já vimos esse PONTO com FIX antes,
        #    mantemos o primeiro e descartamos este.
        if ponto in pontos_vistos:
            descartes.append({**linha, "MOTIVO_DESCARTE": MOTIVO_DUPLICADO})
            continue

        # Ponto aprovado
        pontos_vistos[ponto] = len(aproveitados)
        aproveitados.append(linha)

    return aproveitados, descartes


def extrair_poligonal(aproveitados):
    poligonal = []
    for linha in aproveitados:
        descricao = linha.get("DESCRICAO", "").strip().upper()
        if descricao == "LIMITE":
            poligonal.append(linha)
    return poligonal


def calcular_geometria(poligonal, biblioteca):
    vertices = []
    for linha in poligonal:
        este = leitura.converter_numero(linha["ESTE"])
        norte = leitura.converter_numero(linha["NORTE"])
        vertices.append((este, norte))

    # Perímetro: fecha do último vértice de volta ao primeiro
    perimetro = 0.0
    n = len(vertices)
    for i in range(n):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % n]
        perimetro += biblioteca.distancia(p1, p2)

    area = biblioteca.area_poligono(vertices)
    return perimetro, area