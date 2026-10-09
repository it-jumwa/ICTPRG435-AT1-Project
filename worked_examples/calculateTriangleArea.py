"""
Name: Jaimee Molina
ID: 202514907
Date Created: 06-10-2026

Calculates the area of a triangle with a given base and height.
User input is accepted through tkinter GUI and validated prior to calculation
"""
from tkinter import *


def calculate_area():
    """
    Calculates the area of a triangle and updates the result label text when
    the button is clicked

    :return: None
    """
    base = validate_input(base_entry.get())
    height = validate_input(height_entry.get())

    # If the input is invalid, do not calculate the area
    if (base is None) or (height is None):
        return

    # Hide the error label when inputs pass the validation checks
    error.pack_forget()

    # Calculate the area of the triangle
    area = 0.5 * base * height
    # Update the result label text
    if (area % 1) == 0:
        result.config(text="The area is: " + f"{area:.0f}")
    else:
        result.config(text="The area is: " + f"{area}")


def exit_button():
    """
    Closes the application window

    :return: None
    """
    window.destroy()


def clear():
    """
    Resets the result label text and clears the entry widgets

    :return: None
    """
    result.config(text="The area is: ")
    base_entry.delete(0, "end")
    height_entry.delete(0, "end")


def check_for_float_value(val: str):
    """
    Attempts to convert a string value to a float

    :param val: The string value to convert to a float
    :return: The value as a float if the conversion is successful, otherwise
    None.
    """
    try:
        # Attempts to convert the string input to a float
        val = float(val)
        return val
    # If the parameter can not be converted to a float
    except ValueError:
        # Prompt the user to enter a numeric value
        error.config(text="Enter a numeric value")
        error.pack()
        # Reset the result label
        result.config(text="The area is: ")
        return None


def check_for_integer_value(val):
    """
    Checks whether a numeric value contains a decimal component

    :param val: The numeric value to check
    :return: The value as an integer if it is a whole number, otherwise the
    original value
    """
    try:
        # Check if the value has decimals and is greater than 0
        if (val % 1) > 0:
            return val
        else:
            # Return the value as an integer
            return int(val)
    except ValueError:
        error.config(text="Enter an integer value")
        error.pack()
        result.config(text="The area is: ")
        return None


def check_for_positive_value(val):
    """
    Checks whether a numeric value is greater than zero

    :param val: The numeric value to check
    :return: The original value if it is greater than zero, otherwise None.
    """
    if val > 0:
        return val
    else:
        error.config(text="Enter a positive value")
        error.pack()
        result.config(text="The area is: ")
    return None


def validate_input(val):
    """
    Validates that an input is numeric and greater than zero

    :param val: The value to validate
    :return: The validated numeric value, otherwise None
    """
    val = check_for_float_value(val)
    if val is None:
        return None

    val = check_for_integer_value(val)
    if val is None:
        return None

    val = check_for_positive_value(val)
    if val is None:
        return None

    return val


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
result = Label(window, text="The area is: ")
# Adds the label widget to the application window
result.pack()

"""Buttons"""

# Creates a button widget, for outputting the user's input
button = Button(window, text="Calculate", command=calculate_area)
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
