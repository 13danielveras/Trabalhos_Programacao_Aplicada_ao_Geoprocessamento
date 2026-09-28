# Projeto do Capítulo 2 — Poligonal RTK

Programa em Python que lê um levantamento topográfico em CSV, valida os
pontos, calcula perímetro e área de uma poligonal e exporta GeoJSON.
Interface feita com Tkinter.

## Como rodar

1. Clone o repositório:

   ```
   git clone https://github.com/13danielveras/Trabalhos_Programacao_Aplicada_ao_Geoprocessamento/tree/main/03_trabalho
   ```

2. Abra a pasta `03_trabalho/` no VS Code, abra o `main.py` e aperte **F5**.

3. Clique em **"Abrir CSV..."** e escolha `levantamento_rtk.csv` ou
   `levantamento_bruto.csv`. O programa trata sozinho codificação,
   delimitador, vírgula decimal e registros incompletos.

## Módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Abre a janela do Tkinter. |
| `interface.py` | Interface gráfica (front-end). |
| `leitura.py` | Leitura dos CSVs. |
| `validacao.py` | Validação dos pontos e cálculo de perímetro/área. |
| `biblioteca.py` | Funções geométricas (`distancia`, `area_poligono`). |
| `saida.py` | Geração do GeoJSON e do relatório de descartes. |