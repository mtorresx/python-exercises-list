import flet as ft

CARD_WIDTH = 70
CARD_HEIGHT = 100
CARD_OFFSET = 20       # distância vertical entre cartas empilhadas (leque)
DROP_PROXIMITY = 20    # distância máxima para a carta encaixar num slot
COR_VERSO = "#0D47A1"  # cor do verso (carta virada para baixo)


class Card(ft.GestureDetector):
    """Uma carta do jogo. Mostra a imagem recebida quando está virada para cima
    e uma cor lisa (o verso) quando está virada para baixo."""

    def __init__(self, solitaire, image):
        super().__init__()
        self.mouse_cursor = ft.MouseCursor.MOVE
        self.drag_interval = 5
        self.on_pan_start = self.start_drag
        self.on_pan_update = self.drag
        self.on_pan_end = self.drop

        self.image = image                # caminho da imagem, ex: "images/ovo_rock.jpeg"
        self.face_up = False              # começa virada para baixo
        self.solitaire = solitaire        # referência ao tabuleiro
        self.slot = None                  # slot onde a carta está
        self.left = None
        self.top = None

        self.content = self._verso()

        # cartas que serão arrastadas juntas (esta + as de cima dela)
        self.draggable_pile = [self]

    def _verso(self):
        """visual da carta virada para baixo"""
        return ft.Container(
            width=CARD_WIDTH,
            height=CARD_HEIGHT,
            bgcolor=COR_VERSO,
            border=ft.Border.all(1, "white"),
            border_radius=ft.BorderRadius.all(6),
        )

    def _frente(self):
        """visual da carta virada para cima: a imagem do jogador"""
        return ft.Container(
            width=CARD_WIDTH,
            height=CARD_HEIGHT,
            border_radius=ft.BorderRadius.all(6),
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=ft.Image(
                src=self.image,
                width=CARD_WIDTH,
                height=CARD_HEIGHT,
                fit=ft.ImageFit.COVER,
            ),
        )

    def get_draggable_pile(self):
        """monta a lista de cartas arrastadas, começando por esta carta"""
        if self.slot is not None:
            self.draggable_pile = self.slot.pile[self.slot.pile.index(self):]
        else:
            # carta ainda sem slot (distribuição inicial)
            self.draggable_pile = [self]

    def move_on_top(self):
        """traz a pilha arrastada para o topo do Stack, mantendo a ordem"""
        for card in self.draggable_pile:
            self.solitaire.controls.remove(card)
            self.solitaire.controls.append(card)
        self.solitaire.update()

    def turn_face_up(self):
        """vira a carta para cima, mostrando a imagem"""
        self.face_up = True
        self.content = self._frente()
        self.solitaire.update()

    def place(self, slot):
        """coloca a pilha arrastada no slot, uma carta abaixo da outra"""
        # 1) tira todas as cartas dos slots antigos
        for card in self.draggable_pile:
            if card.slot is not None:
                card.slot.pile.remove(card)

        # 2) adiciona no slot novo, na ordem, e calcula a posição
        for card in self.draggable_pile:
            card.slot = slot
            slot.pile.append(card)
            if slot in self.solitaire.tableau:
                # colunas: cartas em leque
                card.top = slot.top + (len(slot.pile) - 1) * CARD_OFFSET
            else:
                # stock, waste e fundações: uma carta exatamente sobre a outra
                card.top = slot.top
            card.left = slot.left

        self.solitaire.update()

    def bounce_back(self):
        """devolve a pilha para a posição original, no slot de origem"""
        for card in self.draggable_pile:
            if card.slot in self.solitaire.tableau:
                card.top = card.slot.top + card.slot.pile.index(card) * CARD_OFFSET
            else:
                card.top = card.slot.top
            card.left = card.slot.left
        self.solitaire.update()

    def start_drag(self, e: ft.DragStartEvent):
        # pega as cartas que vão junto e leva para o topo
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
        # 1) tenta encaixar numa coluna (tableau), logo abaixo da última carta
        for slot in self.solitaire.tableau:
            alvo_top = slot.top + len(slot.pile) * CARD_OFFSET
            if (
                abs(self.top - alvo_top) < DROP_PROXIMITY
                and abs(self.left - slot.left) < DROP_PROXIMITY
            ):
                self.place(slot)
                return

        # 2) tenta encaixar numa fundação
        for slot in self.solitaire.foundations:
            if (
                abs(self.top - slot.top) < DROP_PROXIMITY
                and abs(self.left - slot.left) < DROP_PROXIMITY
            ):
                self.place(slot)
                return

        # 3) não encaixou em lugar nenhum: volta para a origem
        self.bounce_back()
