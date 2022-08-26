import flet
from flet import Page, TextField, Text, ElevatedButton


def main(page: Page):
    txt_name = TextField(label='Your name')

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = 'Please enter your name!'
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(Text(f'Hello, {name}!'))

    page.add(
        txt_name,
        ElevatedButton('Say hello!', on_click=btn_click)
    )


flet.app(target=main)
