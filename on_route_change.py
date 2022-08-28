import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors


def main(page: Page):
    page.title = 'Routes Example'

    # home page
    text1 = Text(
        value='Flet app'
    )
    elevated_button1 = ElevatedButton(
        text='Visit Store',
        on_click=lambda _: page.go('/store')
    )
    app_bar1 = AppBar(
        title=text1,
        bgcolor=colors.SURFACE_VARIANT
    )
    view1 = View(
        route='/',
        controls=[
            app_bar1,
            elevated_button1
        ]
    )

    # store page
    text2 = Text(
        value='Store'
    )
    elevated_button2 = ElevatedButton(
        text='Go Home',
        on_click=lambda _: page.go('/')
    )
    app_bar2 = AppBar(
        title=text2,
        bgcolor=colors.SURFACE_VARIANT
    )
    view2 = View(
        route='/',
        controls=[
            app_bar2,
            elevated_button2
        ]
    )

    def route_change(router):
        page.views.clear()
        page.views.append(
            view1
        )
        if page.route == '/store':
            page.views.append(
                view2
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(target=main)
