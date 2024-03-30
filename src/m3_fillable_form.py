import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# Done: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()

window.title("Form")

tk.Label(window, text = "Name:", fg = "red").pack()
tk.Entry(window).pack()

tk.Label(window, text = "Address Line 1:", fg = "orange").pack()
tk.Entry(window).pack()

tk.Label(window, text = "Address Line 2:", fg = "gold").pack()
tk.Entry(window).pack()

tk.Label(window, text = "City:", fg = "olive").pack()
tk.Entry(window).pack()

tk.Label(window, text = "State:", fg = "green").pack()
tk.Entry(window).pack()

tk.Label(window, text = "Zip Code:", fg = "Aqua").pack()
tk.Entry(window).pack()

tk.Label(window, text = "Phone Number:", fg = "DodgerBlue").pack()
tk.Entry(window).pack()

tk.Label(window, text = "Email Address:", fg = "Navy").pack()
tk.Entry(window).pack()

button = tk.Button(window, text ="Submit", fg = "black")
button.pack()

window.mainloop()