from flet import *

def main(page: Page):
    page.title = "COUNTER APP"
    page.vertical_alignment = MainAxisAlignment.START

    txt_number = TextField(value="0", text_align="right", width=200)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):   
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment=MainAxisAlignment.START,
        )
    )

app(target=main)