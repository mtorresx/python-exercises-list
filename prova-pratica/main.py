import flet as ft


class Solitaire:
    def __init__(self):
        self.start_top = 0
        self.start_left = 0


solitaire = Solitaire()


def main(page: ft.Page):
    def move_on_top(card, controls):
        """move a carta arrastada para o topo da pilha do Stack"""
        controls.remove(card)
        controls.append(card)
        page.update()

    def start_drag(e: ft.DragStartEvent):
        move_on_top(e.control, controls)
        solitaire.start_top = e.control.top
        solitaire.start_left = e.control.left
        e.control.update()

    def drag(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.local_delta.y)
        e.control.left = max(0, e.control.left + e.local_delta.x)
        e.control.update()

    def place(card, slot):
        """coloca a carta no slot"""
        card.top = slot.top
        card.left = slot.left
        page.update()

    def bounce_back(game, card):
        """devolve a carta para a posição original"""
        card.top = game.start_top
        card.left = game.start_left
        page.update()

    def drop(e: ft.DragEndEvent):
        if abs(e.control.top - slot.top) < 20 and abs(e.control.left - slot.left) < 20:
            place(e.control, slot)
        else:
            bounce_back(solitaire, e.control)
        e.control.update()

    slot = ft.Container(
        width=70,
        height=100,
        left=200,
        top=0,
        border=ft.Border.all(1),
    )

    card1 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=0,
        top=0,
        content=ft.Container(bgcolor=ft.Colors.GREEN, width=70, height=100),
    )

    card2 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=100,
        top=0,
        content=ft.Container(bgcolor=ft.Colors.YELLOW, width=70, height=100),
    )

    controls = [slot, card1, card2]
    page.add(ft.Stack(controls=controls, width=1000, height=500))


ft.run(main)