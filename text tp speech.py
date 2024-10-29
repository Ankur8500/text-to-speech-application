import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import pyttsx3

# Initialize Tkinter
root = Tk()
root.title("Text to Speech")
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg="#305065")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def Speaknow():
    text = text_area.get(1.0, END).strip()  # Get text and remove any extra whitespace
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty("voices")

    if not text:  # Check if text is empty
        print("No text provided")
        return  # Exit if there's no text

    def setvoice():
        if gender == "Male":
            engine.setProperty("voice", voices[0].id)
        else:
            engine.setProperty("voice", voices[1].id)

    # Set speech rate based on selected speed
    if speed == "Fast":
        engine.setProperty('rate', 100)
    elif speed == "Normal":
        engine.setProperty('rate', 100)
    else:  # Default to slow
        engine.setProperty('rate', 100)


       



    print("Speaking...")
    engine.say(text)
    engine.runAndWait()
    print("Finished speaking.")
              

    setvoice()  # Set the voice based on gender
    print("Speaking...")  # Debugging statement
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Wait until speech is finished
    print("Finished speaking.")  # Debugging statement

# GUI Setup
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)
Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black").place(x=100, y=30)

text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)
text_area.focus()  # Set focus on the text area

Label(root, text="VOICE", font="arial 15 bold", bg="#305065", fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(x=760, y=160)

gender_combobox = Combobox(root, values=["Male", "Female"], font="arial 14", state="readonly", width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set("Male")

speed_combobox = Combobox(root, values=["Fast", "Normal", "Slow"], font="arial 14", state="readonly", width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set("Normal")

btn = Button(root, text="Speak", width=10, font="arial 14 bold", command=Speaknow)
btn.place(x=550, y=280)

root.mainloop()
