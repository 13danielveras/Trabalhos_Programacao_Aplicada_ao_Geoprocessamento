import math

# definir função para distancia entre dois com coordenadas UTM usando os nomes este e norte
def distancia(utm1, utm2):
    este1, norte1 = utm1
    este2, norte2 = utm2
    distancia = math.sqrt((este2 - este1) ** 2 + (norte2 - norte1) ** 2)
    return distancia

# definir função para fórmula de area de um polígono usando as coordenadas UTM dos vértices
def area_poligono(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2



