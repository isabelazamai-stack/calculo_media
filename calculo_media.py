import flet as ft
from component.classe_campo_nota import Campo_nota

def main(pagina:ft.Page):
    pagina.title = "Calculadora de Média"
    pagina.bgcolor = "#fce9d2"
    pagina.horizontal_alignment = "center"

    titulo = ft.Text(value="Clique para Digitar sua Média",
                     size = 40,
                     font_family = "Baskerville Old Face",
                     color= "#924A10")
    
    lista_notas = []


    
    def adicionar_nota():
        lista_notas.append(Campo_nota())
        
    def calcular_media():
        soma_notas = 0
        contador_notas = 0

        for campo in lista_notas:
            nota = float(campo.value)
            soma_notas = soma_notas + nota
            contador_notas += 1

            campo_resultado.value = soma_notas / contador_notas
    
    botao = ft.FloatingActionButton(icon = ft.Icon(icon=ft.CupertinoIcons.ADD_CIRCLED,
                                                   color="#A73763"),
                                  bgcolor="#f8d1d1",
                                  foreground_color="#FF3D3D",
                                  hover_color="#f89f9f",
                                  on_click=adicionar_nota
                                  )
    
    coluna_notas = ft.Column(controls=lista_notas,
                             expand=True,
                             wrap=True,
                             scroll=ft.ScrollMode.AUTO,
                             horizontal_alignment="center")

    botao_resultado = ft.FilledTonalButton(content="Calcular Média",
                                           bgcolor="#f8d1d1",
                                           on_click=calcular_media
                                           )

    campo_resultado = ft.TextField(
                                   label="Resultado",
                                   read_only=True,
                                   text_align="center",
                                   bgcolor="#f8d1d1",
                                   value= 0)

    linha_resultado = ft.Row(controls=[botao_resultado,
                                       campo_resultado],
                                       alignment="center"
                                       )

    container_resultado = ft.Container(content=linha_resultado,
                                       bgcolor= "#ffdfdf",
                                       padding=30,
                                       border=ft.Border.all(1,color="#ffffff"))

    

    pagina.controls = [titulo,
                       botao,
                       coluna_notas,
                       container_resultado
                       ]

    pagina.update()
ft.run(main)