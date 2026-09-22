# entrada: dados csv
import csv

caminhos_arquivo = r'D:\GEOPROCESSAMENTO\daniel_veras\programacao\capitulo_1\01_trabalho\levantamento_rtk.csv'
with open(caminhos_arquivo, 'r') as f:
    dados_gnss = list(csv.DictReader(f))

print#(dados_gnss)

# filtrar dados pela coluna descricao
limite = []
for ponto in dados_gnss:
    if ponto["DESCRICAO"] == "LIMITE":
        limite.append(ponto)

#print(limite)

# função que calcula a distância entre dois pontos no plano cartesiano
def calcular_distancia(x0, y0, x1, y1):
    return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

# calcular perimetro
def calcular_perimetro_poligono(pontos):
    perimetro = 0.0
    pontos.append(pontos[0])  # Adiciona o primeiro ponto no final para fechar o polígono
    for i in range(len(pontos) - 1):
        perimetro = perimetro + calcular_distancia(float(pontos[i]["ESTE"]),
                                                   float(pontos[i]["NORTE"]),
                                                   float(pontos[i + 1]["ESTE"]),
                                                   float(pontos[i + 1]["NORTE"]))
    return perimetro

# calcular area
def calcular_area_poligono(pontos):
    area = 0.0
    pontos.append(pontos[0])  # Adiciona o primeiro ponto no final para fechar o polígono
    for i in range(len(pontos) - 1):
        area = area + (float(pontos[i]["ESTE"]) * float(pontos[i + 1]["NORTE"])) - (float(pontos[i + 1]["ESTE"]) * float(pontos[i]["NORTE"]))
    return abs(area) / 2.0

# exibir na tela o resultado
print ("Perímetro:", round(calcular_perimetro_poligono(limite), 3))
print ("Área:", round(calcular_area_poligono(limite), 3))