import flet
from flet import FloatingActionButton, KeyboardEvent, Page, Text, icons


def main(page: Page):
    page.title = 'Flet counter example'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    txt_number = Text(0, size=40)

    def on_keyboard(e: KeyboardEvent):
        print(e)
        if e.key == 'S' and e.ctrl:
            page.show_semantics_debugger = not page.show_semantics_debugger
            page.update()

    page.on_keyboard_event = on_keyboard

    def button_click(e):
        txt_number.value = int(txt_number.value) + 1
        page.update()

    page.add(
        txt_number,
        Text('Press CTRL+S to toggle semantics debugger'),
        FloatingActionButton(
            icon=icons.ADD,
            tooltip='Increment number',
            on_click=button_click
        )
    )


flet.app(target=main)
