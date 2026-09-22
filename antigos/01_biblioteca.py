import math

# função que recebe as coordenadas E e N de dois pontos e devolve a distância horizontal entre eles
def calcular_distancia(e1, n1, e2, n2):
    """ calcula a distância horizontal entre dois pontos """
    return ((e2 - e1)**2 + (n2 - n1)**2)**0.5

# método que devolve o azimute entre dois pontos, em graus, a partir das coordenadas E e N
def calcular_azimute(e1, n1, e2, n2):
    de = e2 - e1
    dn = n2 - n1
    azimute = math.atan2(de, dn)
    return math.degrees(azimute)