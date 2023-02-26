import requests
from tkinter import *


class Translator:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Morse Code Translator")
        self.window.config(height=400, width=600, background='black')
        self.wordtextentry = Entry(width=30)
        self.wordtextentry.place(x=220, y=165)
        self.translationtext = Entry(width=30)
        self.translationtext.place(x=220, y=245)
        translationlabel = Label(text="Translation:", background="black", fg="white")
        translationlabel.place(x=150, y=245) 
        textlabel = Label(text="Text: ", background="black", fg="white")
        textlabel.place(x=190, y=165) 
        title_label = Label(text="-- --- .-. ... . / -.-. --- -.. . / - .-. .- -. ... .-.. .- - --- .-.", background="black", fg="white")
        title_label.place(x=170, y=100)
        titletext = Label(text="Morse Code Translator", background="black", foreground="white", font=("Helvetica bold", 26))
        titletext.place(x=145, y=50)
        self.translate_button = Button(text="Translate", command=self.translate)
        self.translate_button.place(x=230, y=295)
        self.clear_button = Button(text="Clear", command=self.clear)
        self.clear_button.place(x=330, y=295)
        

        self.window.mainloop()

    def translate(self):
        params = {
            "text": self.wordtextentry.get()
        }
        response = requests.get(url="https://api.funtranslations.com/translate/morse.json",params=params)
        translated_response = response.json()["contents"]["translated"]
        return self.translationtext.insert(0, translated_response)
    

    def clear(self):
        self.translationtext.delete(0, END)
        self.wordtextentry.delete(0, END)


if __name__ == "__main__":
    p = Translator()