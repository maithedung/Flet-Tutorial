from time import sleep

import flet
from flet import Page, Text, Row, TextField, ElevatedButton


def main(page: Page):
    # add/update controls on Page
    t = Text()
    page.add(t)  # it's a shortcut for page.controls.add(t) and then page.update()

    for i in range(2):
        t.value = f'Step {i}'
        page.update()
        sleep(1)

    page.add(
        Row(
            controls=[
                Text('A'),
                Text('B'),
                Text('C')
            ]
        )
    )

    page.add(
        Row(
            controls=[
                TextField(label='Your name'),
                ElevatedButton(text='Say my name!')
            ]
        )
    )


flet.app(target=main)
