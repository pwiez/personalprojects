import tkinter as tk

def generate_password():
    pass

#configuration of the window itself
#we only have one window, this is a simple application - no frames, just the root window
app = tk.Tk()
app.title("Password Generator")
app.geometry("600x480")
app.resizable(0, 0)

#program intro text at the top of the window
intro_label = tk.Label(app, text="This is a very simple Python app (with a GUI! :D) to generate passwords.\nYou can choose the generated password's length and complexity.", wraplength=500, justify="center")
intro_label.place(relx=0.5, rely=0.1, anchor="center")

#password complexity switches
numbers_flag = tk.IntVar()
letters_flag = tk.IntVar()
symbols_flag = tk.IntVar()
numbers_checkbox = tk.Checkbutton(app, text="Include numbers", variable=numbers_flag, onvalue=1, offvalue=0)
letters_checkbox = tk.Checkbutton(app, text="Include letters", variable=letters_flag, onvalue=1, offvalue=0)
symbols_checkbox = tk.Checkbutton(app, text="Include symbols", variable=symbols_flag, onvalue=1, offvalue=0)
numbers_checkbox.place(x=80, y=135)
letters_checkbox.place(x=80, y=165)
symbols_checkbox.place(x=80, y=195)

#password length scale
password_length = tk.IntVar()
password_length_label = tk.Label(app, text="Password length:")
password_length_label.place(x=337, y=145)
password_length_scale = tk.Scale(app, length=250, from_=8, to=64, orient="horizontal", variable=password_length)
password_length_scale.place(relx=0.45, y=165)

#quitting the app
exit_button = tk.Button(app, text="Exit", command=app.destroy)
exit_button.place(relx=0.5, rely=0.9, anchor="center")

#######
#running the app
app.mainloop()