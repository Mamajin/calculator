"""This is the calculator ui"""
import tkinter as tk
from keypad import Keypad
from tkinter import ttk
from tkinter import messagebox


class CalculatorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.display_str = tk.StringVar()
        self.display = None
        self.keys = list('789456123 0.')
        self.op_keys = list('*/+-^=')
        self.init_component()
        self.keypad = None

    def init_component(self):
        columns = 3
        self.title("Calculator")

        display = self.make_display()
        display.pack(side=tk.TOP, expand=True, fill="y")
        self.display_str.set("")

        cal_numpad = self.make_numpad(3)
        cal_numpad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        cal_operator = self.make_operator()
        cal_operator.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        for i in range(len(self.keys) // columns + 1):
            cal_numpad.rowconfigure(i, weight=1)
            cal_operator.rowconfigure(i, weight=1)


        display.columnconfigure(0, weight=1)
        cal_numpad.columnconfigure((0, 1, 2), weight=1)
        cal_operator.columnconfigure(3, weight=1)

    def make_numpad(self, columns) -> tk.Frame:
        numpad = tk.Frame()
        col_val = 0
        row_val = 0
        for key in self.keys:
            button = tk.Button(numpad, text=key, padx=2, pady=2,
                               width=5, height=2,
                               command=lambda new_string=key: self.on_button_click(new_string))
            button.grid(row=row_val, column=col_val,
                        padx=2, pady=2, sticky="news")
            col_val += 1
            if col_val > columns - 1:
                col_val = 0
                row_val += 1
        return numpad

    def make_operator(self) -> tk.Frame:
        operator = tk.Frame()
        current_row = 0
        for op in self.op_keys:
            op_button = tk.Button(operator, text=op, padx=2, pady=2, width=5,
                                  command=lambda new_string=op: self.on_button_click(new_string))
            op_button.grid(row=current_row, column=3,
                           padx=2, pady=2, sticky="news")
            current_row += 1
        return operator

    def make_display(self) -> tk.Frame:
        display = tk.Frame()
        self.display = tk.Entry(display, textvariable=self.display_str,
                                width=30, justify="right", bg="black",
                                fg="yellow", font=("Arial", 13))
        self.display.grid(padx=2, pady=2, sticky="e")
        return display

    def on_button_click(self, new_string):
        current_string = self.display_str.get()
        if new_string == "=":
            try:
                result = eval(current_string)
                self.display_str.set(result)
            except Exception as e:
                self.display_str.set("Error")
        else:
            updated_string = current_string + new_string
            self.display_str.set(updated_string)

    def run(self):
        self.mainloop()


cal = CalculatorUI()
cal.run()