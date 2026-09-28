# Projeto do Capítulo 2 — Poligonal RTK

Programa em Python que lê um levantamento topográfico em CSV, valida os
pontos, calcula perímetro e área de uma poligonal e exporta GeoJSON.
A interface é feita com Tkinter.

## Como rodar

1. Clone o repositório:

   ```
   git clone https://github.com/13danielveras/Trabalhos_Programacao_Aplicada_ao_Geoprocessamento
   ```

2. Entre na pasta do projeto:

   ```
   cd Trabalhos_Programacao_Aplicada_ao_Geoprocessamento/03_trabalho
   ```

3. Rode o programa:

   ```
   python main.py
   ```

   A janela do programa deve abrir. Clique em **"Abrir CSV..."** e
   escolha um dos arquivos:

   - `levantamento_rtk.csv` (dados corrigidos)
   - `levantamento_bruto.csv` (dados brutos, com erros propositais)

   O programa trata sozinho codificação, delimitador (`;` ou `,`),
   vírgula decimal e registros incompletos.

## Módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Abre a janela do Tkinter. |
| `interface.py` | Interface gráfica (front-end). |
| `leitura.py` | Leitura dos CSVs. |
| `validacao.py` | Validação dos pontos e cálculo de perímetro/área. |
| `biblioteca.py` | Funções geométricas (`distancia`, `area_poligono`). |
| `saida.py` | Geração do GeoJSON e do relatório de descartes. |