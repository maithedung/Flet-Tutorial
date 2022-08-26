import flet
from flet import Page, Text, KeyboardEvent


def main(page: Page):
    def on_keyboard(e: KeyboardEvent):
        page.add(
            Text(
                f'Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}'
            )
        )

    page.on_keyboard_event = on_keyboard
    page.add(
        Text('Press any key with a combination of CTRL, ALT, SHIFT, META keys and then press Enter.')
    )


flet.app(target=main)
