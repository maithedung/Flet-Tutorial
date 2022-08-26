import flet
from flet import Column, ElevatedButton, Page, Row, Text, TextField


def main(page: Page):
    page.title = 'Flet Chat App'
    messages = Column()
    user = TextField(hint_text='Your name', width=150)
    message = TextField(hint_text='Your message...', expand=True)

    # subscribe to broadcast messages
    def on_message(msg):
        text = Text(msg)
        messages.controls.append(text)
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(f'{user.value}: {message.value}')

    send = ElevatedButton('Send', on_click=send_click)
    page.add(
        messages,
        Row(
            controls=[
                user,
                message,
                send
            ]
        )
    )


flet.app(target=main)