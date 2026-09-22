from dados_levantamento import levantamento

# criar uma lista a partir de lista levatamento contendo apenas os dados cuja descricao é limite
dados_limite = []
for item in levantamento:
    if item["DESCRICAO"] == "LIMITE":
        dados_limite.append(item)

# Imprime cada item em uma nova linha
for item in dados_limite:
    print(item)

# contar quantos pontos têm a descrição ARVORE
dados_arvore = []
for item in levantamento:
    if item["DESCRICAO"] == "ARVORE":
        dados_arvore.append(item)

print(f"O número de itens cuja descrição é 'ARVORE': {len(dados_arvore)}")

# montar uma lista só com os pontos cuja solução não é FIX
dados_nao_fix = []
for item in levantamento:
    if item["SOLUCAO"] != "FIX":
        dados_nao_fix.append(item)
print(f"O número de itens cuja solução não é 'FIX': {len(dados_nao_fix)}")

# encontrar o ponto de maior cota do levantamento, não usar lambda
ponto_maior_cota = None
for item in levantamento:
    if ponto_maior_cota is None or item["COTA"] > ponto_maior_cota["COTA"]:
        ponto_maior_cota = item

print(f"O ponto de maior cota é: {ponto_maior_cota}")