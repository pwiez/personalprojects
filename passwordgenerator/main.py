import tkinter as tk

#configuration of the window itself (for now the geometry is fixed)
app = tk.Tk()
app.title("Password Generator")
app.geometry("600x480")
app.resizable(0, 0)

#configuring the window elements (more stuff will be added here)
intro_label = tk.Label(app, text="This is a very simple Python app (with a GUI! :D) to generate passwords.\nYou can choose the generated password's length and complexity.", wraplength=500, justify="center")
intro_label.place(relx=0.5, rely=0.1, anchor="center")

#quitting the app
exit_button = tk.Button(app, text="Exit", command=app.destroy)
exit_button.place(relx=0.5, rely=0.9, anchor="center")

#######
#running the app
app.mainloop()