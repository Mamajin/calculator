import tkinter as tk
from tkinter import ttk


class Keypad(tk.Frame):
    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        # call the superclass constructor with all args except
        # keynames and columns
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        for i, keyname in enumerate(self.keynames):
            row, col = divmod(i, columns)
            button = tk.Button(self, text=keyname)
            button.grid(row=row, column=col, sticky="nsew")
            button.bind("<Button>", self.handle_press)

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        # Write a bind method with exactly the same parameters
        # as the bind method of Tkinter widgets.
        # Use the parameters to bind all the buttons in the keypad
        # to the same event handler.
        for child in self.winfo_children():
            child.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
               using dictionary syntax.
               Example: keypad['foreground'] = 'red'
               sets the font color on all buttons to red.
               """
        for child in self.winfo_children():
            child[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
                from buttons.
                Example: keypad['foreground'] would return 'red' if the button
                foreground color is 'red'.
                """
        return self.winfo_children()[0][key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.
               To configure properties of the frame that contains the buttons,
               use `keypad.frame.configure()`.
               """
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
