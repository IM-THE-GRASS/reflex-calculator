import reflex as rx

class Calculator(rx.State):
    result: float = 0
    operation: str = ""
    current_input: str = ""
    buttons = [
            1,2,3,"*",
            4,5,6,"-",
            7,8,9,"+",
            0,".","/","="
        ]
    def button(self, button_num:int):
        button = self.buttons[button_num]
        if type(button) == int:
            return self.update_input(button)
        elif button == "=":
            return self.calculate()
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
                rx.heading("Calculator"),
                width="100%"
            ),
            rx.center(
                rx.input(value=Calculator.current_input, is_read_only=True),
                width="100%",
            ),
            rx.grid(
                rx.foreach(
                    rx.Var.range(16),
                    lambda i: rx.button(
                    rx.heading(f"{Calculator.buttons[i]}", size="6"),
                    color_scheme="green",
                    radius="large",
                    align="center",
                    variant="surface",
                    height="10vh",
                    min_width="10vh",
                    on_click=Calculator.button(i)
                    ),
                ),
                columns="4",
                flow="row",
                spacing="4",
                max_width="50vw",
            ),
        ),
        padding_top = "20vh"
    )


app = rx.App()
app.add_page(index)