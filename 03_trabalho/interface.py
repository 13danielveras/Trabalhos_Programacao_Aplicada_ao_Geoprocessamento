import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path

import leitura
import validacao
import saida
import biblioteca


class Aplicacao:
    """Janela principal do programa."""

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Projeto do Capítulo 2 - Poligonal RTK")
        self.raiz.geometry("720x560")
        self.raiz.minsize(640, 480)

        # Estado interno (resultados da última execução)
        self.caminho_csv = None
        self.linhas = None
        self.aproveitados = None
        self.descartes = None
        self.poligonal = None
        self.perimetro = None
        self.area = None

        self._montar_widgets()

    # ------------------------------------------------------------------
    # Montagem da interface
    # ------------------------------------------------------------------
    def _montar_widgets(self):
        # Cabeçalho
        titulo = ttk.Label(
            self.raiz,
            text="Cálculo de perímetro e área de poligonal (RTK)",
            font=("Segoe UI", 14, "bold"),
        )
        titulo.pack(pady=(12, 4))

        subtitulo = ttk.Label(
            self.raiz,
            text="Selecione um arquivo CSV de levantamento para começar.",
            font=("Segoe UI", 10),
        )
        subtitulo.pack(pady=(0, 12))

        # Botões de ação
        frame_botoes = ttk.Frame(self.raiz)
        frame_botoes.pack(pady=4)

        self.botao_abrir = ttk.Button(
            frame_botoes, text="Abrir CSV...", command=self.abrir_csv
        )
        self.botao_abrir.grid(row=0, column=0, padx=4)

        self.botao_geojson = ttk.Button(
            frame_botoes,
            text="Salvar GeoJSON...",
            command=self.salvar_geojson,
            state="disabled",
        )
        self.botao_geojson.grid(row=0, column=1, padx=4)

        self.botao_descartes = ttk.Button(
            frame_botoes,
            text="Salvar descartes...",
            command=self.salvar_descartes,
            state="disabled",
        )
        self.botao_descartes.grid(row=0, column=2, padx=4)

        self.botao_sair = ttk.Button(
            frame_botoes, text="Sair", command=self.raiz.destroy
        )
        self.botao_sair.grid(row=0, column=3, padx=4)

        # Rótulo com o caminho do arquivo carregado
        self.label_arquivo = ttk.Label(
            self.raiz, text="Nenhum arquivo carregado.", foreground="#555"
        )
        self.label_arquivo.pack(pady=(8, 4))

        # Área de resultados
        frame_resultados = ttk.LabelFrame(self.raiz, text="Resultados")
        frame_resultados.pack(fill="both", expand=True, padx=12, pady=8)

        self.texto = tk.Text(
            frame_resultados,
            wrap="word",
            height=18,
            font=("Consolas", 10),
            state="disabled",
        )
        self.texto.pack(fill="both", expand=True, padx=6, pady=6)

        # Barra de status
        self.status = ttk.Label(
            self.raiz, text="Pronto.", relief="sunken", anchor="w"
        )
        self.status.pack(fill="x", side="bottom")

    # ------------------------------------------------------------------
    # Ações
    # ------------------------------------------------------------------
    def abrir_csv(self):
        caminho = filedialog.askopenfilename(
            title="Selecione o CSV do levantamento",
            filetypes=[("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*")],
        )
        if not caminho:
            return

        self.caminho_csv = caminho
        self.label_arquivo.config(text=f"Arquivo: {Path(caminho).name}")
        self.status.config(text="Processando...")
        self.raiz.update_idletasks()

        try:
            self._processar(caminho)
        except Exception as erro:
            messagebox.showerror(
                "Erro ao processar o arquivo", f"{type(erro).__name__}: {erro}"
            )
            self.status.config(text="Erro no processamento.")
            return

        self._mostrar_resultados()
        self.botao_geojson.config(state="normal")
        self.botao_descartes.config(state="normal")
        self.status.config(text="Concluído.")

    def _processar(self, caminho):
        """Pipeline completo: leitura -> validação -> cálculo."""
        self.linhas = leitura.ler_csv(caminho)

        # Descarta linhas totalmente vazias antes de contar
        self.linhas = [
            linha
            for linha in self.linhas
            if not all((v or "").strip() == "" for v in linha.values())
        ]

        self.aproveitados, self.descartes = validacao.classificar(self.linhas)
        self.poligonal = validacao.extrair_poligonal(self.aproveitados)
        self.perimetro, self.area = validacao.calcular_geometria(
            self.poligonal, biblioteca
        )

    def _mostrar_resultados(self):
        self.texto.config(state="normal")
        self.texto.delete("1.0", "end")

        area_ha = self.area / 10000.0

        linhas = [
            f"Total de linhas lidas no CSV: {len(self.linhas)}",
            f"Pontos aproveitados:          {len(self.aproveitados)}",
            f"Pontos descartados:           {len(self.descartes)}",
            f"Vértices da poligonal:        {len(self.poligonal)}",
            "",
            f"Perímetro: {self.perimetro:.3f} m",
            f"Área:      {self.area:.3f} m²",
            f"Área:      {area_ha:.3f} ha",
        ]

        if self.descartes:
            linhas.append("")
            linhas.append("Descartes:")
            for d in self.descartes:
                linhas.append(
                    f"  - {d.get('PONTO', '?'):>6} | {d.get('MOTIVO_DESCARTE', '')}"
                )

        self.texto.insert("1.0", "\n".join(linhas))
        self.texto.config(state="disabled")

    def salvar_geojson(self):
        if not self.poligonal:
            return
        caminho = filedialog.asksaveasfilename(
            title="Salvar GeoJSON",
            defaultextension=".geojson",
            filetypes=[("GeoJSON", "*.geojson"), ("Todos os arquivos", "*.*")],
        )
        if not caminho:
            return
        try:
            saida.gerar_geojson(self.poligonal, caminho)
            messagebox.showinfo("Sucesso", f"GeoJSON salvo em:\n{caminho}")
        except Exception as erro:
            messagebox.showerror("Erro ao salvar GeoJSON", str(erro))

    def salvar_descartes(self):
        if not self.descartes:
            messagebox.showinfo("Sem descartes", "Não há descartes para salvar.")
            return
        caminho = filedialog.asksaveasfilename(
            title="Salvar relatório de descartes",
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv"), ("Todos os arquivos", "*.*")],
        )
        if not caminho:
            return
        try:
            saida.gerar_relatorio_descartes(self.descartes, caminho)
            messagebox.showinfo("Sucesso", f"Relatório salvo em:\n{caminho}")
        except Exception as erro:
            messagebox.showerror("Erro ao salvar relatório", str(erro))


def iniciar():
    """Cria a janela e roda o loop principal do Tkinter."""
    raiz = tk.Tk()
    Aplicacao(raiz)
    raiz.mainloop()