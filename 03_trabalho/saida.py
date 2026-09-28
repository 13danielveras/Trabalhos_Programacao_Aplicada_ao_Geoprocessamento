import csv
import json
from pathlib import Path

import leitura


def _montar_feature(linha, indice):
    este = leitura.converter_numero(linha["ESTE"])
    norte = leitura.converter_numero(linha["NORTE"])
    cota = leitura.converter_numero(linha.get("COTA", ""))

    propriedades = {
        "ponto": linha.get("PONTO", ""),
        "descricao": linha.get("DESCRICAO", ""),
        "solucao": linha.get("SOLUCAO", ""),
        "ordem": indice + 1,
    }
    if cota is not None:
        propriedades["cota"] = cota

    return {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [este, norte]},
        "properties": propriedades,
    }


def gerar_geojson(poligonal, caminho_saida):
    features = [_montar_feature(linha, i) for i, linha in enumerate(poligonal)]

    colecao = {"type": "FeatureCollection", "features": features}

    caminho_saida = Path(caminho_saida)
    with caminho_saida.open("w", encoding="utf-8") as arquivo:
        json.dump(colecao, arquivo, ensure_ascii=False, indent=2)


def gerar_relatorio_descartes(descartes, caminho_saida):
    colunas = ["PONTO", "ESTE", "NORTE", "DESCRICAO", "SOLUCAO", "MOTIVO_DESCARTE"]

    caminho_saida = Path(caminho_saida)
    with caminho_saida.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas, delimiter=";")
        escritor.writeheader()
        for linha in descartes:
            escritor.writerow({coluna: linha.get(coluna, "") for coluna in colunas})