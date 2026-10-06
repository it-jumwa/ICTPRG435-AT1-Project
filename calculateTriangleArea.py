"""
Name: Jaimee Molina
ID: 202514907
Date Created: 06-10-2026

Calculates the area of a triangle with a given base and height.
User input is accepted through tkinter GUI
"""
from tkinter import *


def calculate_button():
    """
    Updates the result label text when the button is clicked
    :return: None
    """
    base = base_entry.get()
    try:
        base = check_for_float_value(base)
        base = check_for_integer_value(base)
    except TypeError:
        return

    base = check_for_positive_value(base)
    if base is None:
        print("Invalid Input...")
        return

    # Hide the error label when inputs pass the validation checks
    error.pack_forget()
    area = 0.5 * base * int(height_entry.get())
    result.config(text="Your input is: " + f"{area}")


def exit_button():
    window.destroy()


def clear():
    result.config(text="Your input is: ")
    base_entry.delete(0, "end")
    height_entry.delete(0, "end")


def check_for_float_value(val):
    try:
        val = float(val)
        return val
    except ValueError:
        error.config(text="Enter a numeric value")
        error.pack()
        return None


def check_for_integer_value(val):
    try:
        if (val % 1) > 0:
            return val
        else:
            return int(val)
    except ValueError:
        error.config(text="Enter an integer value")
        error.pack()
        return None


def check_for_positive_value(val):
    if val > 0:
        return val
    else:
        error.config(text="Enter a positive value greater than 0")
        error.pack()
        return None


"""Initialise the application"""

# Creates the main application window
window = Tk()

# Adds a title to the application window
window.title("Calculate Triangle Area")

# Sets the size of the application window
window.geometry("360x360")

# Blank Error Label
error = Label(text="Error: ...")

"""Base Length"""

# Creates a text label
base_label = Label(window, text="Enter base length of triangle: ")
# Adds the label to the application window
base_label.pack()

# Creates an entry widget that accepts a single-line of text input from
# the user
base_entry = Entry(window)
# Adds the entry widget to the application window
base_entry.pack()

"""Height Length"""

# Creates a text label
height_label = Label(window, text="Enter height length of triangle: ")
# Adds the label to the application window
height_label.pack()

# Creates an entry widget that accepts a single-line of text input from
# the user
height_entry = Entry(window)
# Adds the entry widget to the application window
height_entry.pack()

"""Result"""

# Creates a label widget
result = Label(window, text="The area is: ...")
# Adds the label widget to the application window
result.pack()

"""Buttons"""

# Creates a button widget, for outputting the user's input
button = Button(window, text="Calculate", command=calculate_button)
# Adds the button widget to the application window
button.pack()

clear_button = Button(window, text="Clear", command=clear)
clear_button.pack()

# Creates a button widget, for closing the application
exit_button = Button(window, text="Exit", command=exit_button)
# Adds the button widget to the application window
exit_button.pack()

# Starts the event loop, keeping the window responsive
window.mainloop()
