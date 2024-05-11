import flet as ft

def main(page: ft.Page):
    page.title = "DIALOGS Name"

    dlg = ft.AlertDialog(title=ft.Text("سلام به تو خوش آمدید!"), on_dismiss=lambda e: x())
    def x():
        print("close_dl1")

    def z():
        print("close_dl2")    

    def close_dlg1(e):
        dlg_modal.open = False
        page.update()
        print("human")

    def close_dlg2(e):
        dlg_modal.open = False
        page.update()
        print("robot")    

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("اعتبارسنجی"),
        content=ft.Text("مطمئنی که ربات نیستی؟"),
        actions=[
            ft.TextButton("بله", on_click=close_dlg1),
            ft.TextButton("نه", on_click=close_dlg2),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: z(),
    )

    def dl1(e):
        page.dialog = dlg
        dlg.open = True
        page.update()
        print("dl1 opened")

    def dl2(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
        print("dl2 opened")

    page.add(
        ft.ElevatedButton("دیالوگ 1", on_click=dl1),
        ft.ElevatedButton("دیالوگ 2", on_click=dl2),
    )

ft.app(target=main)