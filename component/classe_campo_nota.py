import flet as ft

class Campo_nota(ft.Row):
    def __init__(self):
        super().__init__()

        caixa_texto = ft.TextField(label="NOTA",
                                   filled=True)

        caixa_selecao = ft.Checkbox()

        self.controls = [
            caixa_selecao,
            caixa_texto
        ]

