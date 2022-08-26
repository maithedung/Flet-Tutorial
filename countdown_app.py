import threading
import time

import flet
from flet import Page, UserControl, Text


class CountdownControl(UserControl):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds
        self.countdown = Text()
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)

    def did_mount(self):
        self.th.start()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.countdown.value = '{:02d}:{:02d}'.format(mins, secs)
            self.update()
            time.sleep(1)
            self.seconds -= 1

    def build(self):
        return self.countdown


def main(page: Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    page.add(
        CountdownControl(120),
        CountdownControl(300)
    )


flet.app(target=main)
