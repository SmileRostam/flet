from flet import *


def main(page):
    def checkbox_changed(e):
        output_text.value = (f"Text :  {todo_check.value}.")
        page.update()

    output_text = Text()
    todo_check = Checkbox(label="CheckBox", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)

app(target=main)