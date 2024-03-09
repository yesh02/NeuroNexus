import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")

        self.result_var = tk.StringVar()

        self.result_entry = ttk.Entry(root, textvariable=self.result_var, font=('Arial', 18), justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Define buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Add buttons to the grid
        for (text, row, col) in buttons:
            ttk.Button(root, text=text, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Configure grid weights for resizing
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == 'C':
            self.result_var.set('')
        else:
            self.result_var.set(current_text + button_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
