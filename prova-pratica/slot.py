import flet as ft

SLOT_WIDTH = 70
SLOT_HEIGHT = 100


class Slot(ft.Container):
    """Área do tabuleiro onde cartas podem ser colocadas.
    Guarda a lista de cartas que estão nela (pile)."""

    def __init__(self, solitaire, top, left, border):
        super().__init__()
        self.pile = []                    # cartas do slot, da de baixo para a de cima
        self.width = SLOT_WIDTH
        self.height = SLOT_HEIGHT
        self.left = left
        self.top = top
        self.solitaire = solitaire        # referência ao tabuleiro
        self.border = border              # ft.Border ou None (sem borda)
        self.border_radius = ft.BorderRadius.all(6)

    def get_top_card(self):
        """devolve a carta de cima da pilha, ou None se a pilha estiver vazia"""
        if len(self.pile) > 0:
            return self.pile[-1]
        return None