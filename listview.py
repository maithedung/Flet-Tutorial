import flet
from flet import ListView, Page, Text


def main(page: Page):
    lv = ListView(expand=True, spacing=10)
    for i in range(5000):
        lv.controls.append(Text(f'Line {i}'))

    page.add(lv)


flet.app(target=main)