import flet
from flet import (Column,Container,ElevatedButton,Row,Text,UserControl,border_radius,colors,Page,ButtonStyle)



class CalculatorApp(UserControl):
    def build(self):
        self.reset()cacc
        self.result = Text(value='0',color=colors.WHITE,size=20)


        return Container(
            bgcolor = colors.BLACK,
            border_radius = border_radius.all(20),
            padding = 20,
            content = Column(
                controls = [
                    Row(controls=[self.result],alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="C",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="C"


                            ),
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="+",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="+"
                            ),
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="/",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="/"
                            ),
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="*",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="*"
                            )
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="C",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="C"


                            ),
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="+",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="+"
                            ),
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="/",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="/"
                            ),
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="*",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="*"
                            )
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="C",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="C"


                            ),
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="+",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="+"
                            ),
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="/",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="/"
                            ),
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="*",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="*"
                            )
                        ],
                    ),
                    

                ]
            )
        )

    def reset(self):
        self.operator = '+'
        self.operand = 0
        self.new_operand = True
def new_page(page):
    calc = CalculatorApp()
    return calc


def main(page:flet.Page):
    page.title = "Calculator"
    page.window_width = 400
    page.window_height = 400
    page.add(new_page(page))



flet.app(target=main)
