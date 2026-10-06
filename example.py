"""
Name: Jaimee Molina
ID: 202514907
Date Created: 06-10-2026

Description...
"""
from tkinter import *

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

# Creates an entry widget that accepts a single-line of text input from the user
number_entry = Entry(window)
# Adds the entry widget to the application window
number_entry.pack()

# Starts the event loop, keeping the window responsive
window.mainloop()