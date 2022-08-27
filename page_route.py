import flet
from flet import Page, Text, ElevatedButton


def main(page: Page):
    def route_change(route):
        text1 = Text(f'New route: {route}')
        page.add(text1)

    def go_store(e):
        page.route = '/store'
        page.update()

    text = Text(f'Initial route: {page.route}')
    store_button = ElevatedButton(
        'Go to Store',
        on_click=go_store
    )

    page.on_route_change = route_change
    page.add(
        text,
        store_button
    )


flet.app(target=main, view=flet.WEB_BROWSER)
