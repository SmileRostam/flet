from flet import *

class MyButton(ElevatedButton):
    
    def __init__(self, x, on_click):
        super().__init__()
        self.bgcolor = colors.AMBER_100
        self.color = colors.CYAN_400
        self.text = x
        self.on_click = on_click
        


def main(page: Page):
    print("D")
    def ok_clicked(e):
        print("OK clicked")
    
    def cancel_clicked(e):
        print("Cancel clicked")

    page.add(
        MyButton(x="OK", on_click=ok_clicked),
        MyButton(x="Cancel", on_click=cancel_clicked),
    )
app(target=main)