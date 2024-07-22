import reflex as rx
from reflex_motion import motion

class Calculator(rx.State):
    result: float = 0
    operation: str = ""
    current_input: str = ""
    buttons = [
            1,2,3,"*",
            4,5,6,"-",
            7,8,9,"+",
            0,".","/","=", "Clear"
        ]
    def button(self, button_num:int):
        button = self.buttons[button_num]
        if type(button) == int:
            return self.update_input(button)
        elif button == "=":
            return self.calculate()
        elif button == "Clear":
            return self.clear()
        elif type(button) is str:
            return self.set_operation(button)
            
                
    def update_input(self, value):
        value = str(value)
        self.current_input += value

    def clear(self):
        self.result = 0
        self.operation = ""
        self.current_input = ""

    def set_operation(self, op: str):
        if self.current_input:
            self.result = float(self.current_input)
            self.current_input = ""
        self.operation = op

    def calculate(self):
        if self.operation and self.current_input:
            second_num = float(self.current_input)
            if self.operation == "+":
                self.result += second_num
            elif self.operation == "-":
                self.result -= second_num
            elif self.operation == "*":
                self.result *= second_num
            elif self.operation == "/":
                if second_num != 0:
                    self.result /= second_num
                else:
                    self.result = "Error"
            self.current_input = str(self.result)
            self.operation = ""

def index():
    return rx.center(
        rx.vstack(
            rx.center(
                rx.heading("Calculator", size="9", color_scheme="green"),
                width="100%"
            ),
            rx.center(
                rx.input(value=Calculator.current_input, is_read_only=True, size="3", color_scheme="green", width="24.5vw", height = "6vh"),
                width="100%",
            ),
            rx.grid(
                rx.foreach(
                    rx.Var.range(17),
                    lambda i: motion(
                        rx.button(
                            rx.heading(f"{Calculator.buttons[i]}", size="6"),
                            color_scheme="green",
                            radius="large",
                            align="center",
                            variant="surface",
                            height="10vh",
                            min_width="10vh",
                            on_click=Calculator.button(i)
                        ),
                        while_hover={"scale": 1.1},
                        while_tap={"scale": 0.9},
                        transition={"type": "spring", "stiffness": 400, "damping": 17},
                    ),
                ),
                columns="4",
                flow="row",
                spacing="2",
                max_width="50vw",
                padding_left = "1vw"
            ),
        ),
        padding_top = "12vh"
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="green",
    )
)
app.add_page(index)