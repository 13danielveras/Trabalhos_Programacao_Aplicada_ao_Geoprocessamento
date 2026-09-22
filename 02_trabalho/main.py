import csv
import math
from pathlib import Path

def distancia(ea, na, eb, nb):
    """Distância horizontal entre dois pontos em coordenadas UTM."""
    de = eb - ea
    dn = nb - na
    return math.sqrt(de**2 + dn**2)

# 1. Trazer os 50 pontos do levantamento.
levantamento = []
arquivo_csv = Path(__file__).resolve().parent / "levantamento_rtk.csv"
with open(arquivo_csv, encoding="utf-8") as arquivo:
    dict_pontos = csv.DictReader(arquivo)
    for linha in dict_pontos:
        levantamento.append(linha)


# 2. Separar apenas os pontos LIMITE com solução FIX, preservando a ordem original.
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
    a = poligonal_fechada[i]
    b = poligonal_fechada[i + 1]
    perimetro = perimetro + distancia(
        float(a["ESTE"]), float(a["NORTE"]),
        float(b["ESTE"]), float(b["NORTE"])
    )


# 5. Calcular a área pela fórmula de Gauss, mostrando o valor com sinal antes de aplicar o módulo.
soma = 0.0
for i in range(len(poligonal_fechada) - 1):
    a = poligonal_fechada[i]
    b = poligonal_fechada[i + 1]
    soma = soma + (float(a["ESTE"]) * float(b["NORTE"]) - float(b["ESTE"]) * float(a["NORTE"]))

area_com_sinal = soma / 2
area = abs(area_com_sinal)

print("Somatório de Gauss dividido por 2 (com sinal):", area_com_sinal)


# 6. Apresentar perímetro em metros, área em m² e área em hectares, com três casas decimais.
print("Perímetro:", round(perimetro, 3), "m")
print("Área:", round(area, 3), "m²")
print("Área:", round(area / 10000, 3), "ha")