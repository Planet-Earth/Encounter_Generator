#########################################################################
# Going through a gui turtorial found here:
# https://realpython.com/python-gui-tkinter/
#########################################################################

import tkinter as tk

# This block creates a window and populates it with the text found in greeting
window = tk.Tk()
greeting = tk.Label(text="Hello. Tkinter")
greeting.pack()

# Creating Label
label = tk.Label(
    text="Hello, Moto",
    foreground="red", # Set the text color to white
    background="orange", # Set the background color to black
    width=10,
    height=10
)
label.pack()

# The following allows the created window tk to exist longer than a fraction of a second
# Everything must be .pack() before this point in the code
window.mainloop()
