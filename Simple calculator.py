import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ValueError("Division by zero is not allowed")
            result = num1 / num2
        elif operation == "^":
            result = num1 ** num2
        elif operation == "sqrt":
            result = math.sqrt(num1)
        else:
            raise ValueError("Invalid operation")

        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An error occurred")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create number entry fields
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=0, column=2)

# Create operation dropdown
operation_var = tk.StringVar()
operation_var.set("+")
operations = ["+", "-", "*", "/", "^", "sqrt"]
operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.grid(row=0, column=1)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=1)

# Create result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=1)

root.mainloop()