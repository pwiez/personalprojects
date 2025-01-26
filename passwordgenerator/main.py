import tkinter as tk

app = tk.Tk()
app.title("Password Generator")
app.geometry("600x480")
app.resizable(0, 0)

intro = tk.Label(app, text="This is a very simple Python app (with a GUI! :D) to generate passwords.\nYou can choose the generated password's length and complexity.", wraplength=500, justify="center")
intro.place(relx=0.5, rely=0.1, anchor="center")

app.mainloop()