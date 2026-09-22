import csv
import unicodedata
import biblioteca as b
import dados as d


def nome_campo(nome):
    return "".join(
        caractere
        for caractere in unicodedata.normalize("NFKD", nome)
        if not unicodedata.combining(caractere)
    ).upper()


def ler_csv(caminho):
    for codificacao in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            with open(caminho, encoding=codificacao, newline="") as arquivo:
                amostra = arquivo.read(4096)
                arquivo.seek(0)
                try:
                    delimitador = csv.Sniffer().sniff(
                        amostra.splitlines()[0], delimiters=";,"
                    ).delimiter
                except csv.Error:
                    delimitador = ","

                leitor = csv.DictReader(arquivo, delimiter=delimitador)
                return [
                    {
                        nome_campo(chave): valor.strip() if valor else ""
                        for chave, valor in linha.items()
                    }
                    for linha in leitor
                ]
        except UnicodeDecodeError:
            continue

    raise UnicodeError("Não foi possível identificar a codificação do CSV.")


def numero(valor):
    return float(valor.replace(",", "."))


# Executar o código importado de dados.py para obter o caminho do arquivo CSV com as coordenadas
caminho_arquivo = d.caminho_arquivo

#1. Trazer os 50 pontos do levantamento.
levantamento = ler_csv(caminho_arquivo)

poligonal = []
for linha in levantamento:
    if (linha['DESCRICAO'].strip() == 'LIMITE'
            and linha['SOLUCAO'].strip().upper() == 'FIX'):
        poligonal.append(linha)

# 3. Avisar na tela quantos pontos foram levantados e quantos formam a poligonal.
print(f"Total de pontos levantados: {len(levantamento)}")
print(f"Vértices da poligonal: {len(poligonal)}")

# 4. Calcular o perímetro, fechando a poligonal do último vértice de volta ao primeiro.
poligonal_fechada = poligonal.copy()
poligonal_fechada.append(poligonal[0])

perimetro = 0.0
for i in range(len(poligonal_fechada) - 1):
    p1 = poligonal_fechada[i]
    p2 = poligonal_fechada[i + 1]
    utm1 = (numero(p1["ESTE"]), numero(p1["NORTE"]))
    utm2 = (numero(p2["ESTE"]), numero(p2["NORTE"]))
    perimetro += b.distancia(utm1, utm2)

# 5. Calcular a área pela fórmula de Gauss, mostrando o valor com sinal antes de aplicar o módulo.
vertices = []
for linha in poligonal:
    vertices.append((numero(linha["ESTE"]), numero(linha["NORTE"])))

area = b.area_poligono(vertices)

# 6. Apresentar perímetro em metros, área em m² e área em hectares, com três casas decimais.
print("Perímetro:", round(perimetro, 3), "m")
print("Área:", round(area, 3), "m²")
print("Área:", round(area / 10000, 3), "ha")