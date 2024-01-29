import tkinter as tk
from math import sqrt, pow

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # Entry widget to display and input
        self.display = tk.Entry(master, font=('Arial', 16), bd=10, insertwidth=4, width=20,
                                justify='right')
        self.display.grid(row=0, column=0, columnspan=5)

        # Buttons for digits and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('√', 5, 0), ('^', 5, 1) ,('exp', 5, 2)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, padx=20, pady=20, font=('Arial', 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)

    def on_button_click(self, text):
        current_display = self.display.get()

        if text == '=':
            try:
                result = eval(current_display)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == 'C':
            self.display.delete(0, tk.END)
        elif text == '√':
            try:
                result = sqrt(float(current_display))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == '^':
            self.display.insert(tk.END, '**')

        elif text == 'exp':
            result = eval(current_display)
            exp_result = result.math.exp(result)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(exp_result))
            
        else:
            self.display.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator_app = CalculatorApp(root)
    root.mainloop()