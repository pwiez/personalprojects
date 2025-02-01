import tkinter as tk
import pyperclip
import random

#character sets to choose from later on
NUMBERS_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
UPPERCASE_LETTERS_LIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
LOWERCASE_LETTERS_LIST = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
SYMBOLS_LIST = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "+", "=", "{", "}", "[", "]", "'", "<", ">", "?"]

class PasswordApp:
    def __init__(self, root):
        # defining the window's core characteristics
        self.root = root
        self.root.title("Python Password Generator by @pwiez")
        self.root.geometry("600x480")
        self.root.resizable(0, 0)

        # configuring the intro label
        self.intro_label = tk.Label(root, text="This is a very simple Python app (with a tkinter GUI :D) to generate passwords.\nYou can choose the generated password's length and complexity.\nPasswords can be from 8 to 64 characters in length.", wraplength=500, justify="center")
        self.intro_label.place(relx=0.5, rely=0.1, anchor="center")

        # configuring the character type checkboxes
        self.numbers_flag = tk.BooleanVar()
        self.lowercase_letters_flag = tk.BooleanVar()
        self.uppercase_letters_flag = tk.BooleanVar()
        self.symbols_flag = tk.BooleanVar()

        self.numbers_checkbox = tk.Checkbutton(root, text="Include numbers", variable=self.numbers_flag, onvalue=True, offvalue=False)
        self.lowercase_letters_checkbox = tk.Checkbutton(root, text="Include lowercase letters", variable=self.lowercase_letters_flag, onvalue=True, offvalue=False)
        self.uppercase_letters_checkbox = tk.Checkbutton(root, text="Include uppercase letters", variable=self.uppercase_letters_flag, onvalue=True, offvalue=False)
        self.symbols_checkbox = tk.Checkbutton(root, text="Include symbols", variable=self.symbols_flag, onvalue=True, offvalue=False)

        self.numbers_checkbox.place(x=55, y=107)
        self.lowercase_letters_checkbox.place(x=55, y=137)
        self.uppercase_letters_checkbox.place(x=55, y=167)
        self.symbols_checkbox.place(x=55, y=197)

        # configuring the password length slider
        self.password_length = tk.IntVar()

        self.password_length_label = tk.Label(root, text="Password length:")
        self.password_length_label.place(x=365, y=135)

        self.password_length_scale = tk.Scale(root, length=230, from_=8, to=64, orient="horizontal", variable=self.password_length)
        self.password_length_scale.place(relx=0.51, y=155)

        # configuring the button to generate the password, it calls generate_password on click
        self.generate_button = tk.Button(root, text="Generate password", command=self.generate_password)
        self.generate_button.place(relx=0.5, y=265, width=160, height=30, anchor="center")
    
        # configuring the field for the generated password
        self.result_label = tk.Label(root, bg="white", padx=10, text="Your password will appear here.")
        self.result_label.place(relx=0.5, y=340, anchor="center")

        # configuring the button for copying the result to the clipboard
        self.copy_button = tk.Button(root, state=tk.DISABLED, text="Copy password to clipboard", command= lambda : pyperclip.copy(self.result_label.cget("text")))
        self.copy_button.place(relx=0.5, y=385, width=220, height=30, anchor="center")

        # configuring the exit button
        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.place(relx=0.9, rely=0.9, anchor="center")

    def generate_password(self):
        password = ''
        character_choice_array = []

        if self.numbers_flag.get() : character_choice_array.extend(NUMBERS_LIST)
        if self.lowercase_letters_flag.get(): character_choice_array.extend(LOWERCASE_LETTERS_LIST)
        if self.uppercase_letters_flag.get(): character_choice_array.extend(UPPERCASE_LETTERS_LIST)
        if self.symbols_flag.get(): character_choice_array.extend(SYMBOLS_LIST)

        if len(character_choice_array) == 0:
            self.result_label.config(fg="red", text="Please choose the character types for your password!")
            self.copy_button.config(state=tk.DISABLED)
        else: self.copy_button.config(state=tk.NORMAL)

        for char in range(self.password_length.get()):
            password += str(random.choice(character_choice_array))
        self.result_label.config(fg="black",text=password)

# running the app!
if __name__ == "__main__":
    pyperclip.copy('')
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()