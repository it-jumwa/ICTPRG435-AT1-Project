"""
Name: Jaimee Molina
ID: 202514907
Date Created: 06-10-2026

A program demonstrating the basic of tkinter
"""
from tkinter import *


def click_button():
    result.config(text="Your input is: " + number_entry.get())

# Creates the main application window
window = Tk()

# Adds a title to the application window
window.title("Window :O")

# Sets the size of the application window
window.geometry("1080x720")

# Creates a text label
label = Label(window, text="Enter first value: ")
# Adds the label to the application window
label.pack()

# Creates an entry widget that accepts a single-line of text input from
# the user
number_entry = Entry(window)
# Adds the entry widget to the application window
number_entry.pack()

# Creates a label widget
result = Label(window, text="Your input is: ...")
# Adds the label widget to the application window
result.pack()

# Creates a button widget
button = Button(window, text="Click Me!", command=click_button)
# Adds the button widget to the application window
button.pack()

# Starts the event loop, keeping the window responsive
window.mainloop()
