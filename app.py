from tkinter import *

main = Tk()

# Giving title
main.title("Basic Calculator")

# Creating input area
inputField = Text(main, height=2, width=70)
inputField.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Creating numeric buttons
button_0 = Button(main, text="0", padx=40, pady=20,)
button_1 = Button(main, text="1", padx=40, pady=20,)
button_2 = Button(main, text="2", padx=40, pady=20,)
button_3 = Button(main, text="3", padx=40, pady=20,)
button_4 = Button(main, text="4", padx=40, pady=20,)
button_5 = Button(main, text="5", padx=40, pady=20,)
button_6 = Button(main, text="6", padx=40, pady=20,)
button_7 = Button(main, text="7", padx=40, pady=20,)
button_8 = Button(main, text="8", padx=40, pady=20,)
button_9 = Button(main, text="9", padx=40, pady=20,)

# Putting buttons on screen
button_0.grid(row=2, column=0)
button_1.grid(row=3, column=4)
button_2.grid(row=3, column=3)
button_3.grid(row=3, column=2)
button_4.grid(row=3, column=1)
button_5.grid(row=3, column=0)
button_6.grid(row=2, column=4)
button_7.grid(row=2, column=3)
button_8.grid(row=2, column=2)
button_9.grid(row=2, column=1)


# Creating calculation buttons
button_add = Button(main, text="+", padx=38, pady=20)
button_sub = Button(main, text="−", padx=38, pady=20)
button_mul = Button(main, text="x", padx=40, pady=20)
button_div = Button(main, text="÷", padx=38, pady=20)
button_equal = Button(main, text="=", padx=156, pady=20)

# Putting calculation buttons on screen
button_add.grid(row=1, column=1)
button_sub.grid(row=1, column=2)
button_mul.grid(row=4, column=0)
button_div.grid(row=4, column=1)
button_equal.grid(row=4, column=2, columnspan=3)


# Creating special buttons
button_clear = Button(main, text="C", padx=40, pady=20)
button_off = Button(main, text="Off", padx=92, pady=20)

# Putting special buttons on screen
button_clear.grid(row=1, column=0)
button_off.grid(row=1, column=3, columnspan=2)

mainloop()
