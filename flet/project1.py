import flet as ft

def main(page: ft.Page):
    welcomeTxt = ft.Text(value="به اپ من خوش آمدید", color="black")
    page.controls.append(welcomeTxt)
    page.update()

ft.app(target=main)