import flet as ft

def main(pagina:ft.Page):
    pagina.title = "Calculadora de Média"
    pagina.bgcolor = "#fce9d2"
    pagina.horizontal_alignment = "center"

    titulo = ft.Text(value="Clique para Digitar sua Média",
                     size = 40,
                     font_family = "Baskerville Old Face",
                     color= "#924A10")

    botao = ft.FloatingActionButton(icon = ft.Icons.ADD,
                                  bgcolor="#f8d1d1",
                                  foreground_color="#FF3D3D",
                                  hover_color="#ff9595"
                                  )

    botao_resultado = ft.FilledTonalButton(content="Calcular Média")

    campo_resultado = ft.TextField(value = 0,
                                   label="Resultado",
                                   read_only=True,
                                   text_align="center")

    



    pagina.controls = [titulo,
                       botao,
                       botao_resultado,
                       campo_resultado
                       ]

    pagina.update()
ft.run(main)