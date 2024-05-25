import flet
from flet import (Column,Container,ElevatedButton,Row,Text,UserControl,border_radius,colors,Page,ButtonStyle)



class CalculatorApp(UserControl):
    def build(self):
        self.reset()
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
                                text="-",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="-",
                                on_click=self.button_click


                            ),
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="+",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="+",
                                on_click=self.button_click
                            ),
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="/",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="/",
                                on_click=self.button_click
                            ),
                            ElevatedButton(
                                style=ButtonStyle(padding=0),
                                text="*",
                                bgcolor=colors.YELLOW,
                                color = colors.BLACK,
                                expand = 1,
                                data="*",
                                on_click=self.button_click
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
                                data="C",
                                on_click=self.button_click


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
                                data="C",
                                on_click=self.button_click

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


    def format_number(self):
        pass
    def calculate(self,operand1,operand2,operator):
        if operator == "+":
            return operand1 + operand2 
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return operand1 / operand2

    def button_click(self,e):
        data = e.control.data
        print("data:",data)
        if self.result.value == "Error" or data =="C":
            self.result.value = "0"
            self.reset()
def new_page(page):
    calc = CalculatorApp()
    return calc


def main(page:Page):
    page.title = "Calculator"
    page.window_width = 400
    page.window_height = 400
    page.add(new_page(page))



flet.app(target=main)
