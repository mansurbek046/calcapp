import flet as ft

def main(page: ft.Page):
    page.title='Calculator'
    page.update()

    text_result=ft.TextField(text_align=ft.TextAlign.RIGHT, expand=1, read_only=True)

    page.add(text_result)

    def btn_click(e):
        if e.control.text=='C':
            text_result.value=''
        elif e.control.text=='=':
            try:
                text_result.value=str(eval(text_result.value))
            except:
                text_result.value='Error'
        else:
            text_result.value+=e.control.text

        text_result.update()

    buttons=['789/','456*','123-', '0.C+', '=']
    for row in buttons:
        row_controls=[]
        for btn_text in row:
            btn=ft.TextButton(text=btn_text, on_click=btn_click, expand=1)
            row_controls.append(btn)
        page.add(ft.Row(controls=row_controls, expand=1))

ft.app(main)
