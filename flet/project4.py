from flet import *

def main(page):
    def btn_click(e):
        if  txt_name.value:
            name = txt_name.value
            page.clean()
            page.add(Text(f"سلام {name}")) 
        else:
            txt_name.error_text = "لطفا نام خود را وارد کنید"
            page.update()
            

    txt_name = TextField(label="لطفا نام خود را وارد کنید")

    page.add(txt_name, ElevatedButton("میخوام بهت سلام کنم", on_click=btn_click))

app(target=main)