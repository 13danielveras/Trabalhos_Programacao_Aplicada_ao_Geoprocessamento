
import math


def distancia(utm1, utm2):
    este1, norte1 = utm1
    este2, norte2 = utm2
    return math.sqrt((este2 - este1) ** 2 + (norte2 - norte1) ** 2)


def area_poligono(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0
