import tkinter as NewWindow

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# Done: 1. (2 pts)
#
#   First, create a tkinter window called window and give it the title "Custom
#   Widgets"
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 2. (2 pts)
#
#   Create a label called label with the text "My Custom Label" in it.
#
#   Give the label these attributes:
#       - foreground = "purple"
#       - background = "green"
#       - width = 15
#       - height = 3
#
#   Make sure you use the label's pack() method to add it to your window.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 3. (2 pts)
#
#   Create a button called button with the text "My Custom Button" in it.
#
#   Give the button these attributes:
#       - foreground = "white"
#       - background = "black"
#       - width = 12
#       - height = 2
#
#   Make sure you use the button's pack() method to add it to your window.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 4. (2 pts)
#
#   Create an entry box called entry with this attribute:
#       - width = 20
#
#   Use entry's insert() method to insert your name by default in the entry
#   field
#
#   Make sure you use the entry's pack() method to add it to your window.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################


window = NewWindow.Tk()

window.title("Custon Widgets")

label = NewWindow.Label(
    window,
    text = "My Custom Label",
    foreground = "purple",
    background = "green",
    width = 15,
    height = 3,
)
label.pack()

button = NewWindow.Button(
    window,
    text="My Custom Button",
    fg = "white",
    bg = "black",
    width = 12,
    height = 2
)
button.pack()

entry = NewWindow.Entry(window, width = 20)
entry.pack()
entry.insert(0, "Olivia")

window.mainloop()