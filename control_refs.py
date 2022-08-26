import flet
from flet import Checkbox, ElevatedButton, Row, TextField, Page, Column, Text, Ref


def main(page: Page):
    first_name = Ref[TextField]()
    last_name = Ref[TextField]()
    greetings = Ref[Column]()

    def btn_click(e):
        text = Text(f'Hello, {first_name.current.value} {last_name.current.value}!')
        greetings.current.controls.append(text)
        first_name.current.value = ''
        last_name.current.value = ''
        page.update()
        first_name.current.focus()

    page.add(
        TextField(ref=first_name, label='First name', autofocus=True),
        TextField(ref=last_name, label='Last Name'),
        ElevatedButton('Say hello!', on_click=btn_click),
        Column(ref=greetings)
    )


flet.app(target=main)
