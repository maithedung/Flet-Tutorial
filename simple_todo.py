import flet
from flet import Checkbox, ElevatedButton, Row, TextField, Page


def main(page: Page):
    def add_clicked(e):
        page.add(Checkbox(label=new_task.value))

    new_task = TextField(hint_text='Whats needs to be done?', width=300)
    page.add(
        Row(
            [
                new_task,
                ElevatedButton("Add", on_click=add_clicked)
            ]
        )
    )


flet.app(target=main)
