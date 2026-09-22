import dados as d
import biblioteca as b

# mostrar as duas diferenças arredondadas para 3 casas decimais
print("A diferença em Este entre PT003 e PT002 é:", round(d.e2 - d.e1, 3))
print("A diferença em Norte entre PT003 e PT002 é:", round(d.n2 - d.n1, 3))

# calcular a distância horizontal entre PT003 e PT002
distancia_horizontal = b.calcular_distancia(d.e1, d.n1, d.e2, d.n2)
print(f"Distância horizontal entre PT003 e PT002: {distancia_horizontal:.3f}")

# calcular o azimute entre PT003 e PT002
azimute = b.calcular_azimute(d.e1, d.n1, d.e2, d.n2)
print(f"Azimute entre PT003 e PT002: {azimute:.3f} graus")

# 1. mostrar o quinto vértice da lista
print("O quinto vértice da lista é:", d.vertices[4])

# 2. mostrar a coordenada Norte do último vértice da lista
print("A coordenada Norte do último vértice da lista é:", d.vertices[-1][1])

# 3. mostrar quantos vértices tem a poligonal
print("A poligonal tem", len(d.vertices), "vértices")

# 4. mostrar os três primeiros vértices da lista
print("Os três primeiros vértices da lista são:", d.vertices[:3])

# 5. calcular a distância entre os primeiro e o último vértice da lista
distancia = b.calcular_distancia(d.vertices[0][0],
                                 d.vertices[0][1],
                                 d.vertices[-1][0],
                                 d.vertices[-1][1])
print(f"A distância entre o primeiro e o último vértice da lista é: {round(distancia, 3)}")