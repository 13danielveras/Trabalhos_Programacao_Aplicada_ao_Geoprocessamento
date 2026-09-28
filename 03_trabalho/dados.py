import csv

# pedir ao usuário o caminho do arquivo CSV com as coordenadas
print("Digite o caminho do arquivo CSV com as coordenadas:")

# criar um menu onde o usuário pode digitar o caminho do arquivo CSV com as coordenadas
# criar um loop caso o usuário digite um caminho inválido, o programa
# deve pedir novamente até que o usuário digite um caminho válido
while True:
    caminho_arquivo = input()
    try:
        with open(caminho_arquivo, 'r') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                pass
            break
    except FileNotFoundError:
        print("Arquivo não encontrado. Por favor, digite um caminho válido.")