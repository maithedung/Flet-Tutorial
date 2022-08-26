import flet
from flet import Page, TextField, IconButton, icons, Row


def main(page: Page):
    page.title = 'Counter Flet App'
    page.vertical_alignment = 'center'

    txt_numer = TextField(value=0, text_align='right', width=100)

    def minus_click(e):
        txt_numer.value = txt_numer.value - 1
        page.update()

    def plus_click(e):
        txt_numer.value = txt_numer.value + 1
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_numer,
                IconButton(icons.ADD, on_click=plus_click)
            ],
            alignment='center'
        )
    )


flet.app(target=main)
