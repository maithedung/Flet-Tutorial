import flet
from flet import Page, Text


def main(page: Page):
    # add/update controls on Page

    t = Text(value="maithedung", color='blue')

    c = Text(value="maithedung", color='yellow')

    text = Text(
        value="This is a Text control sample",
        size=30,
        color="white",
        bgcolor="pink",
        weight="bold",
        italic=True,
    )

    page.add(t, c, text)


flet.app(target=main)
