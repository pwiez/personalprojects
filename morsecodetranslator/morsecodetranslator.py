import tkinter as tk
import re
import pyperclip

MORSE_CODE_TABLE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

class MainWindow():
    def __init__(self, root):
        # core window characteristics
        self.root = root
        self.root.title("Morse Code Translator by @pwiez")
        self.root.geometry("800x600")
        self.root.resizable(0,0)

        # introductory label at the top of the window
        self.intro_label = tk.Label(self.root, text="This is a simple Morse Code Translator.\nEnter your message in the box below and click the translate button!", wraplength=1200)
        self.intro_label.place(relx=0.5, rely=0.1, anchor="center")

        # entry box for the message that will be translated
        self.message_box = tk.Text(self.root, width=75, height=6, border=3)
        self.message_box.place(relx=0.5, rely=0.25, anchor="center")

        # translation button
        self.translate_button = tk.Button(self.root, text="Translate to Morse code!", command= lambda: self.translate_message())
        self.translate_button.place(relx=0.5, rely=0.385, anchor="center")

        # result label and box to display the translation
        self.result_label = tk.Label(self.root, text="Your translated message will appear in the box below.")
        self.result_label.place(relx=0.5, rely=0.56, anchor="center")
        self.result_box = tk.Label(self.root, width=75, height=6, borderwidth=3, relief="sunken", bg="white", anchor="nw", justify="left", wraplength=600)
        self.result_box.place(relx=0.5, rely=0.70, anchor="center")

        # copy to clipboard button
        self.copy_button = tk.Button(self.root, text="Copy translation to clipboard", state=tk.DISABLED, command= lambda : pyperclip.copy(self.result_box.cget("text")))
        self.copy_button.place(relx=0.5, rely=0.85, anchor="center")

        # exit button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.place(relx=0.938, rely=0.93, anchor="center")

    # returns the corresponding morse code character
    def lookup(self, dictionary, key):
        return dictionary.get(key)
    
    # checks each character in the string returned from the textbox.
    # if the message is empty or contains invalid characters, returns.
    # a valid result enables the copy button, otherwise it is disabled
    def translate_message(self):
        message = self.message_box.get("1.0", tk.END).strip().upper()
        translated_message = []
        if len(message) == 0:
            self.result_label.config(fg="red", text="Empty message. Type something in the box above and try again!")
            self.result_box.config(text="")
            self.copy_button.config(state=tk.DISABLED)
            return
        for char in message:
            if char not in MORSE_CODE_TABLE:
                self.result_label.config(fg="red", text="Invalid characters detected. Please use only alphanumerical characters, space and punctuation in your message!")
                self.result_box.config(text="")
                self.copy_button.config(state=tk.DISABLED)
                break
            elif re.search('[\t\n\r\f\v]', message):
                self.result_label.config(fg="red", text="Invalid whitespace character detected. Please use only alphanumerical characters, space and punctuation in your message!")
                self.result_box.config(text="")
                self.copy_button.config(state=tk.DISABLED)
                break
            else:
                translated_message.append((self.lookup(MORSE_CODE_TABLE, char)))
                self.result_label.config(fg="black", text="Message translated successfully! Here it is:")
                self.result_box.config(text=translated_message)
                self.copy_button.config(state=tk.ACTIVE)

if __name__ == '__main__' :
    pyperclip.copy('')
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()