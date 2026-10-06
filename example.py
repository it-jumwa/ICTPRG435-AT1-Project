"""
Name: Jaimee Molina
ID: 202514907
Date Created: 06-10-2026

Description...
"""
from tkinter import *


def click_button():
    result = Label(window, text="Your input is: " + number_entry.get())
    result.pack()


if __name__ == "__main__":
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

    result = Label(window, text="Your input is: ...")
    result.pack()

    button = Button(window, text="Click Me!", command=click_button)
    button.pack()

    # Starts the event loop, keeping the window responsive
    window.mainloop()
