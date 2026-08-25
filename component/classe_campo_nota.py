import flet as ft

class Campo_nota(ft.Row):
    def __init__(self):
        super().__init__()

        self.caixa_texto = ft.TextField(label="NOTA",
                                   filled=True,
                                   bgcolor="#ffe3e3")

        self.caixa_selecao = ft.Checkbox(on_change=self.alteral_cor)

        self.caixa_bonita = ft.Container(content=ft.Row(controls=[self.caixa_selecao,
                                                             self.caixa_texto],
                                                             ),
                                                             bgcolor="#fff8e3",
                                                             border=ft.Border.all(width=1,
                                                                                  color="#ffffff"),
                                                            border_radius=10,
                                                            padding=5,
                                                            animate=True)

        self.controls = [
            self.caixa_bonita
        ]

    def alteral_cor(self):
        if self.caixa_selecao.value == True:
            self.caixa_bonita.bgcolor="#B17C56"
        else:
            self.caixa_bonita.bgcolor = "#ffe3e3"

    @property
    def value(self):
        return self.caixa_texto.value
    
    

