import tkinter as tk

class MainWindow():
    def __init__(self, root):
        # core window characteristics
        self.root = root
        self.root.title("Morse Code Translator by @pwiez")
        self.root.geometry("1024x768")
        self.root.resizable(0,0)

        # introductory label at the top of the window
        self.intro_label = tk.Label(self.root, text="This is a simple Morse Code Translator.\nEnter your message in the box below and click the translate button! Messages are restricted to 250 characters max.", wraplength=1200)
        self.intro_label.place(relx=0.5, rely=0.1, anchor="center")

        # entry box for the message that will be translated
        self.message_box = tk.Text(self.root, width=75, height=6)
        self.message_box.place(relx=0.5, rely=0.25, anchor="center")

        # translation button
        self.translate_button = tk.Button(self.root, text="Translate to Morse code!")
        self.translate_button.place(relx=0.5, rely=0.363, anchor="center")

        # result label and box to display the translation
        self.result_label = tk.Label(self.root, text="Translated message:")
        self.result_label.place(relx=0.5, rely=0.515, anchor="center")
        self.result_box = tk.Label(self.root, width=100, height=12, bg="white")
        self.result_box.place(relx=0.5, rely=0.69, anchor="center")

        # exit button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.place(relx=0.92, rely=0.92, anchor="center")

root = tk.Tk()
app = MainWindow(root)
root.mainloop()