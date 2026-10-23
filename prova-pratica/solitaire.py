import random
import flet as ft
from slot import Slot
from card import Card

SOLITAIRE_WIDTH = 1000
SOLITAIRE_HEIGHT = 500

# imagens das cartas (na pasta assets/images, ao lado do main.py)
IMAGENS = [
    "images/ovo_rock.jpeg",
    "images/rock_aventureira.jpeg",
    "images/the_rock_lisa.jpeg",
]


class Solitaire(ft.Stack):
    """O tabuleiro inteiro. É um Stack, então os controles usam posição absoluta."""

    def __init__(self):
        super().__init__()
        self.controls = []
        self.cards = []
        self.width = SOLITAIRE_WIDTH
        self.height = SOLITAIRE_HEIGHT

    def did_mount(self):
        # criado aqui e não no __init__: os controles só podem ser
        # atualizados depois que o Stack já está na página
        self.create_card_deck()
        self.create_slots()
        self.deal_cards()

    def create_card_deck(self):
        # uma carta para cada imagem
        self.cards = [Card(solitaire=self, image=img) for img in IMAGENS]

    def create_slots(self):
        # stock: onde ficam as cartas viradas para baixo (com borda)
        self.stock = Slot(self, top=0, left=0, border=ft.Border.all(1))

        # waste: onde vão as cartas tiradas do stock (sem borda)
        self.waste = Slot(self, top=0, left=100, border=None)

        # 4 fundações, no canto superior direito
        self.foundations = []
        x = 300
        for i in range(4):
            self.foundations.append(
                Slot(self, top=0, left=x, border=ft.Border.all(1, "outline"))
            )
            x += 100

        # 7 colunas (tableau), abaixo das outras áreas
        self.tableau = []
        x = 0
        for i in range(7):
            self.tableau.append(Slot(self, top=150, left=x, border=None))
            x += 100

        # adiciona todas as áreas ao Stack
        self.controls.append(self.stock)
        self.controls.append(self.waste)
        self.controls.extend(self.foundations)
        self.controls.extend(self.tableau)
        self.update()

    def deal_cards(self):
        random.shuffle(self.cards)
        self.controls.extend(self.cards)

        # as cartas nascem no stock, empilhadas no mesmo lugar
        for card in self.cards:
            card.place(self.stock)

        # todas as cartas ficam viradas para cima, mostrando as imagens
        for card in self.cards:
            card.turn_face_up()

        self.update()
