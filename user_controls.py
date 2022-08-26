import flet
from flet import Page, UserControl, Text, Row, ElevatedButton


class GreeterControl(UserControl):
    def __init__(self, text='Hello!'):
        super().__init__()
        self.text = Text(text)

    def build(self):
        return self.text


class CounterControl(UserControl):
    def __init__(self, initial_count=0):
        super().__init__()
        self.counter = initial_count
        self.text = Text(str(self.counter))

    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
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
        GreeterControl('Start'),
        CounterControl(100),
        CounterControl(500),
        GreeterControl('End')
    )


flet.app(target=main)
