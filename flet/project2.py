from flet import *

def main(page):
    def add_task(event):
        page.add(Checkbox(label=new_task.value))
        print(new_task.value)
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = TextField(hint_text="کارتو وارد کن", width=300)
    page.add(Row([new_task, ElevatedButton("اضافه کردن", on_click=add_task)]))

app(target=main)