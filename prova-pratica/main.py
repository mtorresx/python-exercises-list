import flet as ft
from solitaire import Solitaire

# cor da mesa (verde feltro)
COR_MESA = "#2E7D32"


def main(page: ft.Page):
    solitaire = Solitaire()
    page.add(
        ft.Container(
            content=solitaire,
            bgcolor=COR_MESA,
            width=1000,
            height=500,
        )
    )


ft.run(main)
