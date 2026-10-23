import flet as ft

CARD_WIDTH = 70
CARD_HEIGHT = 100
CARD_OFFSET = 20
DROP_PROXIMITY = 20


class Card(ft.GestureDetector):
    def __init__(self, solitaire, color):
        super().__init__()
        self.slot = None
        self.mouse_cursor = ft.MouseCursor.MOVE
        self.drag_interval = 5
        self.on_pan_start = self.start_drag
        self.on_pan_update = self.drag
        self.on_pan_end = self.drop
        self.left = None
        self.top = None
        self.solitaire = solitaire
        self.color = color
        self.content = ft.Container(
            bgcolor=self.color, width=CARD_WIDTH, height=CARD_HEIGHT
        )
        self.draggable_pile = [self]

    def get_draggable_pile(self):
        """lista das cartas que serão arrastadas juntas, começando pela carta escolhida"""
        if self.slot is not None:
            self.draggable_pile = self.slot.pile[self.slot.pile.index(self):]
        else:
            # carta ainda não está em slot (na distribuição inicial)
            self.draggable_pile = [self]

    def move_on_top(self):
        """traz a pilha arrastada para o topo do Stack, mantendo a ordem"""
        for card in self.draggable_pile:
            self.solitaire.controls.remove(card)
            self.solitaire.controls.append(card)
        self.solitaire.update()

    def bounce_back(self):
        """devolve a pilha para a posição original no slot"""
        for card in self.draggable_pile:
            card.top = self.slot.top + self.slot.pile.index(card) * CARD_OFFSET
            card.left = self.slot.left
        self.solitaire.update()

    def place(self, slot):
        """coloca a pilha arrastada no slot"""
        # primeiro tira todas as cartas dos slots antigos
        for card in self.draggable_pile:
            if card.slot is not None:
                card.slot.pile.remove(card)

        # depois adiciona no novo slot, na ordem
        for card in self.draggable_pile:
            card.slot = slot
            slot.pile.append(card)
            card.top = slot.top + (len(slot.pile) - 1) * CARD_OFFSET
            card.left = slot.left

        self.solitaire.update()

    def start_drag(self, e: ft.DragStartEvent):
        self.get_draggable_pile()
        self.move_on_top()
        self.update()

    def drag(self, e: ft.DragUpdateEvent):
        # calcula a nova posição uma vez, antes de mexer nas cartas
        new_top = max(0, self.top + e.local_delta.y)
        new_left = max(0, self.left + e.local_delta.x)

        for i, card in enumerate(self.draggable_pile):
            card.top = new_top + i * CARD_OFFSET
            card.left = new_left

        self.solitaire.update()

    def drop(self, e: ft.DragEndEvent):
        for slot in self.solitaire.slots:
            if (
                abs(self.top - slot.top) < DROP_PROXIMITY
                and abs(self.left - slot.left) < DROP_PROXIMITY
            ):
                self.place(slot)
                return

        self.bounce_back()