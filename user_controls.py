import flet
from flet import Page, UserControl, Text, Row, ElevatedButton


class GreeterControl(UserControl):
    def build(self):
        return Text("Hello!")


class CounterControl(UserControl):
    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        self.counter = 0
        self.text = Text(str(self.counter))
        return Row(
            [
                self.text,
                ElevatedButton(
                    'Add',
                    on_click=self.add_click
                )
            ]
        )


def main(page: Page):
    page.add(
        GreeterControl(),
        CounterControl(),
        CounterControl(),
        GreeterControl()
    )


flet.app(target=main)
