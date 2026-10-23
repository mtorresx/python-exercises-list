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

    def move_on_top(self):
        """move a carta para o topo da pilha do Stack"""
        self.solitaire.controls.remove(self)
        self.solitaire.controls.append(self)
        self.solitaire.update()

    def bounce_back(self):
        """devolve a carta para a posição dentro do slot de origem"""
        self.top = self.slot.top + self.slot.pile.index(self) * CARD_OFFSET
        self.left = self.slot.left
        self.update()

    def place(self, slot):
        """coloca a carta no slot, no final da pilha, com deslocamento"""
        # tira a carta do slot antigo primeiro, para contar certo
        if self.slot is not None:
            self.slot.pile.remove(self)

        self.slot = slot
        slot.pile.append(self)

        self.top = slot.top + (len(slot.pile) - 1) * CARD_OFFSET
        self.left = slot.left

    def start_drag(self, e: ft.DragStartEvent):
        self.move_on_top()
        self.update()

    def drag(self, e: ft.DragUpdateEvent):
        self.top = max(0, self.top + e.local_delta.y)
        self.left = max(0, self.left + e.local_delta.x)
        self.update()

    def drop(self, e: ft.DragEndEvent):
        for slot in self.solitaire.slots:
            if (
                abs(self.top - slot.top) < DROP_PROXIMITY
                and abs(self.left - slot.left) < DROP_PROXIMITY
            ):
                self.place(slot)
                self.update()
                return

        self.bounce_back()
        self.update()