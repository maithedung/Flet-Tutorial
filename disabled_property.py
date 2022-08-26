import flet
from flet import Checkbox, ElevatedButton, Row, TextField, Page, Column


def main(page: Page):
    first_name = TextField()
    last_name = TextField()
    first_name.disabled = True

    page.add(first_name, last_name)

    c = Column(
        controls=[
            first_name,
            last_name
        ]
    )
    c.disabled = True
    page.add(c)


flet.app(target=main)
