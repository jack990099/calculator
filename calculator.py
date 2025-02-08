import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(True, True)
        self.expression = ""
        self.input_text = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_columnconfigure(0, weight=1)

        input_frame = tk.Frame(self, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.grid(row=0, column=0, sticky="nsew")
        input_frame.grid_rowconfigure(0, weight=1)
        input_frame.grid_columnconfigure(0, weight=1)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0, ipady=10, sticky="nsew")

        btns_frame = tk.Frame(self, bg="grey")
        btns_frame.grid(row=1, column=0, sticky="nsew")
        for i in range(5):
            btns_frame.grid_rowconfigure(i, weight=1)
            for j in range(4):
                btns_frame.grid_columnconfigure(j, weight=1)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('%', 0, 3)
        ]

        for (text, row, col) in buttons:
            self.create_button(btns_frame, text, row, col)

    def create_button(self, parent, text, row, col):
        button = tk.Button(parent, text=text, fg="black", bg="#fff", cursor="hand2",
                           font=('arial', 18), bd=1, relief="raised",
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '=':
            try:
                expression = self.expression.replace('%', '/100')
                result = str(eval(expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("错误")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
