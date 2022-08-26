from time import sleep

import flet
from flet import Page, Text


def main(page: Page):
    for i in range(7):
        page.controls.append(Text(f'Line {i}'))
        if i > 4:
            page.controls.pop(0)
        page.update()
        sleep(0.3)


flet.app(target=main)
