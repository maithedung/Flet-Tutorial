import os
import flet
from flet import Container, Page, Row, Text, alignment, border, border_radius, colors, GridView

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def main(page: Page):
    gv = GridView(expand=True, max_extent=100, child_aspect_ratio=1)
    page.add(gv)

    for i in range(5000):
        gv.controls.append(
            Container(
                Text(f'Item {i}', color='green'),
                alignment=alignment.center,
                bgcolor=colors.AMBER_100,
                border=border.all(1, colors.AMBER_400),
                border_radius=border_radius.all(5)
            )
        )

    page.update()


flet.app(target=main)
