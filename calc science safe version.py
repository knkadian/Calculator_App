import tkinter as tk
from math import sqrt, sin, cos, tan, radians, log, pi

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator Project")
        self.geometry("600x600")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # display and input
        entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 20), bd=10, insertwidth=4, width=14,
                         justify='right')
        entry.grid(row=0, column=0, columnspan=5)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sqrt', 'C',
            'sin', 'cos', 'tan',
            '^', 'log', 'pi'
        ]

        # button click
        def button_click(value):
            current = self.result_var.get()

            if value == 'C':
                self.result_var.set('')
            elif value == '=':
                try:
                    result = eval(current)
                    self.result_var.set(result)
                except Exception as e:
                    self.result_var.set('Error')
            elif value == 'sqrt':
                try:
                    result = sqrt(eval(current))
                    self.result_var.set(result)
                except Exception as e:
                    self.result_var.set('Error')
            elif value == 'sin':
                try:
                    result = sin(radians(eval(current)))
                    self.result_var.set(result)
                except Exception as e:
                    self.result_var.set('Error')
            elif value == 'cos':
                try:
                    result = cos(radians(eval(current)))
                    self.result_var.set(result)
                except Exception as e:
                    self.result_var.set('Error')
            elif value == 'tan':
                try:
                    result = tan(radians(eval(current)))
                    self.result_var.set(result)
                except Exception as e:
                    self.result_var.set('Error')
            elif value == '^':
                self.result_var.set(current + '**')
            elif value == 'log':
                try:
                    result = log(eval(current))
                    self.result_var.set(result)
                except Exception as e:
                    self.result_var.set('Error')
            elif value == 'pi':
                self.result_var.set(current + str(pi))
            else:
                self.result_var.set(current + str(value))

        # Add buttons 
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val >= 4:
                col_val = 0
                row_val += 1

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()