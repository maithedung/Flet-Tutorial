from time import sleep

import flet
from flet import Page, Text, Row, TextField, ElevatedButton


def main(page: Page):
    def button_clicked(e):
        page.add(Text('Clicked!'))

    page.add(ElevatedButton(text='Click me!', on_click=button_clicked))


flet.app(target=main)
