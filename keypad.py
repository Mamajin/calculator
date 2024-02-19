import tkinter as tk
from tkinter import ttk


class Keypad(tk.Frame):
    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        for i, keyname in enumerate(self.keynames):
            row, col = divmod(i, columns)
            button = tk.Button(self, text=keyname)
            button.grid(row=row, column=col, sticky="nsew")
            button.bind("<Button>", self.handle_press)


    def bind(self, sequence=None, func=None, add=None):
        for child in self.winfo_children():
            child.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        for child in self.winfo_children():
            child[key] = value

    def __getitem__(self, key):
        return self.winfo_children()[0][key]

    def configure(self, cnf=None, **kwargs):
        for child in self.winfo_children():
            child.configure(cnf, **kwargs)

    @property
    def frame(self):
        return super()

    @staticmethod
    def handle_press(event):
        print(f"Button {event.widget['text']} pressed.")


if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(expand=True, fill=tk.BOTH)

    # Example configurations
    keypad.bind('<Button>', keypad.handle_press)
    keypad.configure(foreground='red')
    keypad['font'] = ('Monospace', 16)
    keypad.frame.configure(background='light green')

    root.mainloop()
