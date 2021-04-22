from tkinter import *

main = Tk()

# Giving title
main.title("Basic Calculator")

# Giving background color
main.configure(bg="#313131")

mainFrame = Frame(main,)
mainFrame.configure(bg="#313131")
mainFrame.grid(row=0, column=0, padx=10, pady=10)

# Creating input area
inputField = Entry(mainFrame, width=70, bg="#f0ece2")
inputField.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=10)

# Creating numeric buttons
button_0 = Button(mainFrame, text="0", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_1 = Button(mainFrame, text="1", padx=43, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_2 = Button(mainFrame, text="2", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_3 = Button(mainFrame, text="3", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_4 = Button(mainFrame, text="4", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_5 = Button(mainFrame, text="5", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_6 = Button(mainFrame, text="6", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_7 = Button(mainFrame, text="7", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_8 = Button(mainFrame, text="8", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_9 = Button(mainFrame, text="9", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))

# Putting buttons on#1F1B24
button_0.grid(row=2, column=0, padx=5, pady=5)
button_1.grid(row=3, column=4, padx=5, pady=5)
button_2.grid(row=3, column=3, padx=5, pady=5)
button_3.grid(row=3, column=2, padx=5, pady=5)
button_4.grid(row=3, column=1, padx=5, pady=5)
button_5.grid(row=3, column=0, padx=5, pady=5)
button_6.grid(row=2, column=4, padx=5, pady=5)
button_7.grid(row=2, column=3, padx=5, pady=5)
button_8.grid(row=2, column=2, padx=5, pady=5)
button_9.grid(row=2, column=1, padx=5, pady=5)


# Creating calculation buttons
button_add = Button(mainFrame, text="➕", padx=38, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_sub = Button(mainFrame, text="−", padx=37, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_mul = Button(mainFrame, text="x", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_div = Button(mainFrame, text="÷", padx=38, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_equal = Button(mainFrame, text="=", padx=156, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))

# Putting calculation buttons on screen
button_add.grid(row=1, column=1, padx=5, pady=5)
button_sub.grid(row=1, column=2, padx=5, pady=5)
button_mul.grid(row=4, column=0, padx=0, pady=5)
button_div.grid(row=4, column=1, padx=5, pady=5)
button_equal.grid(row=4, column=2, columnspan=3, padx=5, pady=5)


# Creating special buttons
button_clear = Button(mainFrame, text="C", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))
button_off = Button(mainFrame, text="Off", padx=90, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,))

# Putting special buttons on screen
button_clear.grid(row=1, column=0, padx=5, pady=5)
button_off.grid(row=1, column=3, columnspan=2, padx=5, pady=5)

mainloop()
