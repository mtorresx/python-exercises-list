import flet as ft
from slot import Slot
from card import Card

SOLITAIRE_WIDTH = 1000
SOLITAIRE_HEIGHT = 500

# imagens das cartas (pasta assets/images, ao lado do main.py)
IMAGENS = [
    "images/ovo_rock.jpeg",
    "images/rock_aventureira.jpeg",
    "images/the_rock_lisa.jpeg",
]


class Solitaire(ft.Stack):
    def __init__(self):
        super().__init__()
        self.controls = []
        self.slots = []
        self.cards = []
        self.width = SOLITAIRE_WIDTH
        self.height = SOLITAIRE_HEIGHT

    def did_mount(self):
        self.create_card_deck()
        self.create_slots()
        self.deal_cards()

    def create_card_deck(self):
        self.cards = [Card(self, image=img) for img in IMAGENS]

    def create_slots(self):
        self.slots.append(Slot(top=0, left=0))
        self.slots.append(Slot(top=0, left=200))
        self.slots.append(Slot(top=0, left=300))
        self.controls.extend(self.slots)
        self.update()

    def deal_cards(self):
        self.controls.extend(self.cards)
        for card in self.cards:
            card.place(self.slots[0])
        self.update()
