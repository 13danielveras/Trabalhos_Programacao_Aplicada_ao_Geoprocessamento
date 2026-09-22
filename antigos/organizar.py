
print("quantidade de vértices:", len(vertices))
print("primeiro vértice:", vertices[0])
print("último vértice:", vertices[-1])
print("E do primeiro vértice:", vertices[0][0])
print("N do primeiro vértice:", vertices[0][1])
print("E do último vértice:", vertices[-1][0])
print("N do último vértice:", vertices[-1][1])

# 1. mostrar o quinto vértice da lista
print("quinto vértice:", vertices[4])

# 2. mostrar a coordenada Norte do último vértice
print("Norte do último vértice:", vertices[-1][1])

# 3. mostrar quantos vértices tem a poligonal
print("quantidade de vértices:", len(vertices))

# 4. mostrar os três primeiros vértices de uma vez só
print("três primeiros vértices:", vertices[:3])

# 5. calcular a distância entre o primeiro e o último vértice
p1 = vertices[0]
p2 = vertices[-1]

distancia = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

print(f"Distância: {distancia:.3f}")

# coordenadas do ponto PT002: E = 746226.659, N = 6944443.246
# coordenadas do ponto PT003: E = 746256.549, N = 6944466.367
# calcular a diferença em Este e em Norte entre PT003 e PT002

diferenca_E = float(E_PT003) - float(E_PT002)
diferenca_N = float(N_PT003) - float(N_PT002)




# calcular a diferença em Este e em Norte entre PT003 e PT002
de = e2 - e1
dn = n2 - n1





# calcular a distância horizontal entre PT002 e PT003
distancia_horizontal = calcular_distancia(e1, n1, e2, n2)
print(f"Distância horizontal entre PT002 e PT003: {distancia_horizontal:.3f}")

# função que recebe as coordenadas E e N de dois pontos e devolve o azimute do ponto 2 em relação ao ponto 1


