from tkinter import *
import tkinter.messagebox

main = Tk()

# Giving title
main.title("Basic Calculator")

# Giving background color
main.configure(bg="#313131")

# Creating Frame
mainFrame = Frame(main)

# Giving background color to frame
mainFrame.configure(bg="#313131")

# Putting frame on screen
mainFrame.grid(row=0, column=0, padx=10, pady=10)

# Creating input field
inputField = Entry(mainFrame, width=70, bg="#f0ece2")
inputField.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=10)

# Creating functions

# For showing entered number
def click_button(number):
    current_value = inputField.get()
    inputField.delete(0, END)
    inputField.insert(0, str(current_value) + str(number))

# To clear entered input
def clear_button():
    inputField.delete(0, END)

# To shut the project
def power_off():
    popup = tkinter.messagebox.askquestion('Exit','Are you sure do you want to exit ?')
    if popup == 'yes':
        main.destroy()

# For adding numbers
def button_add():
    first_number = inputField.get()
    global num_first
    global calculation
    calculation = 'addition'
    num_first= int(first_number)
    inputField.delete(0, END)

# To get result
def button_equal():
    second_number = inputField.get()
    inputField.delete(0, END)
    if calculation == "addition":
        inputField.insert(0, num_first + int(second_number))
    elif calculation == "subtraction":
        inputField.insert(0, num_first - int(second_number))
    elif calculation == "division":
        inputField.insert(0, num_first / int(second_number))
    elif calculation == "multiplication":
        inputField.insert(0, num_first * int(second_number))

# To subtract
def button_subtract():
    first_number = inputField.get()
    global num_first
    global calculation
    calculation = 'subtraction'
    num_first= int(first_number)
    inputField.delete(0, END)

# To multiply
def button_multiply():
    first_number = inputField.get()
    global num_first
    global calculation
    calculation = 'multiplication'
    num_first= int(first_number)
    inputField.delete(0, END)

# To divide
def button_divide():
    first_number = inputField.get()
    global num_first
    global calculation
    calculation = 'division'
    num_first= int(first_number)
    inputField.delete(0, END)


# Creating numeric buttons
button_0 = Button(mainFrame, text="0", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), command =lambda: click_button(0))
button_1 = Button(mainFrame, text="1", padx=43, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), command =lambda: click_button(1))
button_2 = Button(mainFrame, text="2", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), command =lambda: click_button(2))
button_3 = Button(mainFrame, text="3", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), command =lambda: click_button(3))
button_4 = Button(mainFrame, text="4", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), command =lambda: click_button(4))
button_5 = Button(mainFrame, text="5", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), command =lambda: click_button(5))
button_6 = Button(mainFrame, text="6", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), command =lambda: click_button(6))
button_7 = Button(mainFrame, text="7", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), command =lambda: click_button(7))
button_8 = Button(mainFrame, text="8", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), command =lambda: click_button(8))
button_9 = Button(mainFrame, text="9", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), command =lambda: click_button(9))

# Putting buttons on screen
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
button_add = Button(mainFrame, text="➕", padx=38, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,), command= button_add)
button_sub = Button(mainFrame, text="−", padx=37, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,), command= button_subtract)
button_mul = Button(mainFrame, text="x", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,), command= button_multiply)
button_div = Button(mainFrame, text="÷", padx=38, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,), command= button_divide)
button_equal = Button(mainFrame, text="=", padx=156, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,), command= button_equal)

# Putting calculation buttons on screen
button_add.grid(row=1, column=1, padx=5, pady=5)
button_sub.grid(row=1, column=2, padx=5, pady=5)
button_mul.grid(row=4, column=0, padx=0, pady=5)
button_div.grid(row=4, column=1, padx=5, pady=5)
button_equal.grid(row=4, column=2, columnspan=3, padx=5, pady=5)

# Creating special buttons
button_clear = Button(mainFrame, text="C", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15, "bold"), command= clear_button)
button_off = Button(mainFrame, text="Off", padx=90, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,), command= power_off)

# Putting special buttons on screen
button_clear.grid(row=1, column=0, padx=5, pady=5)
button_off.grid(row=1, column=3, columnspan=2, padx=5, pady=5)


mainloop()
