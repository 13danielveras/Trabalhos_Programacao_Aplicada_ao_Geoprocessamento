import csv
import unicodedata
from pathlib import Path

import biblioteca as b  # não usado aqui, mas mantém o padrão do projeto


# Codificações testadas em ordem. A primeira que funcionar é usada.
CODIFICACOES = ("utf-8-sig", "cp1252", "latin-1")

# Delimitadores aceitos
DELIMITADORES = ";,"


def normalizar_campo(nome):
    return "".join(
        caractere
        for caractere in unicodedata.normalize("NFKD", nome)
        if not unicodedata.combining(caractere)
    ).upper()


def converter_numero(valor):
    if valor is None:
        return None
    valor = valor.strip()
    if not valor:
        return None
    try:
        return float(valor.replace(",", "."))
    except ValueError:
        return None


def _detectar_delimitador(amostra):
    try:
        return csv.Sniffer().sniff(amostra, delimiters=DELIMITADORES).delimiter
    except csv.Error:
        return ","


def ler_csv(caminho):
    caminho = Path(caminho)

    for codificacao in CODIFICACOES:
        try:
            with caminho.open("r", encoding=codificacao, newline="") as arquivo:
                amostra = arquivo.read(4096)
                arquivo.seek(0)

                delimitador = _detectar_delimitador(amostra.splitlines()[0])

                leitor = csv.DictReader(arquivo, delimiter=delimitador)
                linhas = []
                for linha in leitor:
                    linhas.append(
                        {
                            normalizar_campo(chave): (valor.strip() if valor else "")
                            for chave, valor in linha.items()
                            if chave is not None
                        }
                    )
                return linhas
        except UnicodeDecodeError:
            continue

    raise UnicodeError(
        f"Não foi possível identificar a codificação do arquivo: {caminho}"
    )