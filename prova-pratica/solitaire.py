import random
import flet as ft
from slot import Slot
from card import Card

SOLITAIRE_WIDTH = 1000
SOLITAIRE_HEIGHT = 500

# quantas cartas usar: 3 por enquanto, 52 no baralho completo
DECK_SIZE = 3


class Suite:
    """naipe: name é o nome (hearts...) e color é a cor (RED ou BLACK)"""
    def __init__(self, suite_name, suite_color):
        self.name = suite_name
        self.color = suite_color


class Rank:
    """valor: name é o nome (Ace, 2... King) e value é o número (1 a 13)"""
    def __init__(self, card_name, card_value):
        self.name = card_name
        self.value = card_value


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
        suites = [
            Suite("hearts", "RED"),
            Suite("diamonds", "RED"),
            Suite("clubs", "BLACK"),
            Suite("spades", "BLACK"),
        ]
        ranks = [
            Rank("Ace", 1),
            Rank("2", 2),
            Rank("3", 3),
            Rank("4", 4),
            Rank("5", 5),
            Rank("6", 6),
            Rank("7", 7),
            Rank("8", 8),
            Rank("9", 9),
            Rank("10", 10),
            Rank("Jack", 11),
            Rank("Queen", 12),
            Rank("King", 13),
        ]

        # monta o baralho completo (52 cartas)
        self.cards = []
        for suite in suites:
            for rank in ranks:
                self.cards.append(Card(solitaire=self, suite=suite, rank=rank))

        # embaralha e fica só com DECK_SIZE cartas
        random.shuffle(self.cards)
        self.cards = self.cards[:DECK_SIZE]

    def create_slots(self):
        # stock: onde ficam as cartas viradas para baixo (com borda)
        self.stock = Slot(self, top=0, left=0, border=ft.Border.all(1))

        # waste: onde vão as cartas tiradas do stock (sem borda)
        self.waste = Slot(self, top=0, left=100, border=None)

        # 4 fundações, uma por naipe, no canto superior direito
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

        # 1) distribui nas colunas: a 1ª coluna recebe 1 carta, a 2ª recebe 2, e assim por diante
        remaining = list(self.cards)
        first_slot = 0
        while first_slot < len(self.tableau):
            for slot in self.tableau[first_slot:]:
                if not remaining:
                    break  # acabaram as cartas (necessário com poucas cartas)
                top_card = remaining.pop(0)
                top_card.place(slot)
            first_slot += 1

        # 2) o que sobrou vai para o stock
        for card in remaining:
            card.place(self.stock)

        # 3) vira a carta de cima de cada coluna que tiver carta
        for slot in self.tableau:
            top = slot.get_top_card()
            if top is not None:
                top.turn_face_up()

        self.update()