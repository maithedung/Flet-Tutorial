import flet
from flet import FloatingActionButton, KeyboardEvent, Page, Text, icons


def main(page: Page):
    page.title = 'Flet counter example'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    def on_keyboard(e: )