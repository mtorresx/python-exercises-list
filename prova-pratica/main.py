import flet as ft
from solitaire import Solitaire

# cor da mesa (verde feltro). Troque por outra, ex: "#1565C0" (azul)
COR_MESA = "#2E7D32"


def main(page: ft.Page):
    # o Container pinta o fundo; o Solitaire fica dentro dele
    page.add(
        ft.Container(
            content=Solitaire(),
            bgcolor=COR_MESA,
            width=1000,
            height=500,
        )
    )


ft.run(main)