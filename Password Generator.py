import random
import tkinter as tk
from tkinter import messagebox
def generate_password():
    try:
        number_of_chars = int(entry.get())
        if number_of_chars <= 0:
            raise ValueError("The number of characters must be greater than 0.")
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
        return
    
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";"]
    list_chars = []
    for i in range(number_of_chars):
        z = random.randint(0, 2)
        if z == 0:
            char = random.choice(alphabet)
            list_chars.append(char)
        elif z == 1:
            char = str(random.choice(numbers))
            list_chars.append(char)
        elif z == 2:
            char = random.choice(special)
            list_chars.append(char)

    result = ''.join(list_chars)
    messagebox.showinfo("Generated Password", f"Your generated password is: {result}")
root = tk.Tk()
root.title("Funky Password Generator")
root.geometry("1024x768")
funky_bg_color = "#003366"
funky_fg_color = "#FFD700"
funky_font = ("Comic Sans MS", 26, "bold")
button_font = ("Comic Sans MS", 24, "bold")
root.configure(bg=funky_bg_color)
label = tk.Label(root, text="Enter the number of characters:", bg=funky_bg_color, fg=funky_fg_color, font=funky_font)
label.pack(pady=20)
entry = tk.Entry(root, font=funky_font, width=20)
entry.pack(pady=5)
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg=funky_fg_color, fg=funky_bg_color, font=button_font)
generate_button.pack(pady=20)
label2 = tk.Label(root, text="PASSWORD!", bg=funky_bg_color, fg=funky_fg_color, font=funky_font)
label2.pack(pady=10)
root.mainloop()
