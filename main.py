from tkinter import *
from tkinter import ttk

morse_code = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

# Construct the GUI
window = Tk()
window.title('© Aaron Norfolk')
window.geometry("750x500")

# Add the image
bg = PhotoImage(file="morse_code.png")
label1 = Label( window, image = bg)
label1.place(relx=0.5, rely=0.5, anchor="center")

label = Label(window, text='Enter text', font="Courier 30 bold")
label.pack(ipadx=10, ipady=10)

#  Convert and display the input
def display_text():
    global entry
    string = entry.get()
    converted_message = [morse_code[letter] for letter in string]
    converted_message = ' '.join(converted_message)
    label.configure(text=converted_message)


# Initialize a label to display the user input
label = Label(window, text="", font="Courier 30 bold")
label.pack()

# Create an entry widget to accept user input
entry = Entry(window, width=40)
entry.focus_set()
entry.pack()

# Create a button that calls the display_text function
ttk.Button(window, text="Convert!", width=20, command=display_text).pack(pady=20)

window.mainloop()
