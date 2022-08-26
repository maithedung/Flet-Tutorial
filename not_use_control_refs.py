import flet
from flet import Checkbox, ElevatedButton, Row, TextField, Page, Column, Text


def main(page: Page):
    first_name = TextField(label='First name', autofocus=True)
    last_name = TextField(label='Last name')
    greetings = Column()

    def btn_click(e):
        text = Text(f'Hello, {first_name.value} {last_name.value}!')
        greetings.controls.append(text)
        first_name.value = ''
        last_name.value = ''
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ElevatedButton('Say hello!', on_click=btn_click),
        greetings
    )


flet.app(target=main)
