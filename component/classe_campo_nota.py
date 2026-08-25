import flet as ft

class Campo_nota(ft.Row):
    def __init__(self):
        super().__init__()

        caixa_texto = ft.TextField(label="NOTA",
                                   filled=True,
                                   bgcolor="#ffe3e3")

        caixa_selecao = ft.Checkbox()

        caixa_bonita = ft.Container(content=ft.Row(controls=[caixa_selecao,
                                                             caixa_texto],
                                                             ),
                                                             bgcolor="#ffffff",
                                                             border=ft.Border.all(width=1,
                                                                                  color="#ffffff"),
                                                            border_radius=10,
                                                            padding=5)

        self.controls = [
            caixa_bonita
        ]

