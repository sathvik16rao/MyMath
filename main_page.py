from tkinter import *
import MyMath
from tkinter import messagebox

main = Tk()
main.title('Scientific Calculator')
main.config(bg='#000000')
main.geometry('448x372')
main.resizable(FALSE,FALSE)

def open_ec():
    main.destroy()
    import extended_calc
def open_help():
    import instructions
def open_sc():
    main.destroy()
    import Simple_calc

my_menu = Menu(main)
main.config(menu=my_menu)

modules = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Menu", menu=modules)
modules.add_command(label='Simple Calculator', command=open_sc)
modules.add_command(label='Scientific Calculator 2.0', command=open_ec)
modules.add_separator()
modules.add_command(label='Exit', command=main.destroy)

instruction = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Help", menu=instruction)
instruction.add_command(label='How to use calculator', command=open_help)

entryField = Entry(main, font=('times new roman',20,'bold'), bg='#000000', fg='#F1DDCF', bd=5, relief=RIDGE, width = 31, insertbackground = 'white')
entryField.grid(row=0,column=0,columnspan=8)

angle_unit = "Deg"

def click(value):
    val = entryField.get()
    try:
        if value=='Del':                    
            val = val[0:len(val) - 1]
            entryField.delete(0,END)
            entryField.insert(0, val)
        elif value=='AC':
            entryField.delete(0,END)
        elif value=="√":
            result = MyMath.sqroot(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="π":
            result = MyMath.pi
            entryField.insert(END, result)
        elif value=="2π":
            result = 2*MyMath.pi
            entryField.insert(END, result)
        elif value==chr(8731):                  #cube root
            result = MyMath.nthroot(eval(val),3)
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="x\u02b8":                  #x^y
            entryField.insert(END, '**')
        elif value=="x\u00B3":                  #x^3
            result = MyMath.cube(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="x\u00B2":                  #x^2
            result = MyMath.square(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="ln":
            try:
                result = MyMath.ln(eval(val))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except MyMath.MathError:
                messagebox.showerror('Math Error','Logarithms of negative number or zero is not defined.')
        elif value=="Deg":
            result = MyMath.degrees(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="Rad":
            result = MyMath.radians(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="e":
            result = MyMath.e
            entryField.insert(END, result)
        elif value=="log":
            try:
                result = MyMath.log(eval(val))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except MyMath.MathError:
                messagebox.showerror('Math Error','Logarithms of negative number or zero is not defined.')
        elif value=="x!":
            try:
                result = MyMath.factorial(eval(val))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except MyMath.MathError:
                messagebox.showerror('Math Error','Sorry, factorial does not exist for negative numbers.')
        elif value=="%":
            result = (eval(val))*100
            entryField.delete(0,END)
            entryField.insert(0, result)
        
        
        #Trigonometric functions
        elif value=="sin":
            if angle_unit=="Deg":
                result = MyMath.sin(MyMath.radians(eval(val)))
            else:
                result = MyMath.sin(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cos":
            if angle_unit=="Deg":
                result = MyMath.cos(MyMath.radians(eval(val)))
            else:
                result = MyMath.cos(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="tan":
            if angle_unit=="Deg":
                result = MyMath.tan(MyMath.radians(eval(val)))
            else:
                result = MyMath.tan(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cosec":
            if angle_unit=="Deg":
                result = MyMath.cosec(MyMath.radians(eval(val)))
            else:
                result = MyMath.cosec(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="sec":
            if angle_unit=="Deg":
                result = MyMath.sec(MyMath.radians(eval(val)))
            else:
                result = MyMath.sec(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cot":
            if angle_unit=="Deg":
                result = MyMath.cot(MyMath.radians(eval(val)))
            else:
                result = MyMath.cot(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        
        
        #Arithmetic operations
        elif value==chr(247):
            entryField.insert(END, "/")
            return
        elif value=="×":
            entryField.insert(END, "*")
            return
        elif value=="=":
            result = eval(val)
            entryField.delete(0,END)
            entryField.insert(0, result)
        else:
            entryField.insert(END, value)
    except SyntaxError:
        messagebox.showerror('Syntax Error', "Oops! Please check the entered expression.")
    except ZeroDivisionError:
        messagebox.showerror('Math Error', "Oops! Division by zero will break math and we don't want that now, do we?")

button_text_list = ["Del", "AC", "√", "+", "π", "sin", "cos", "tan",
                    "7", "8", "9", "-", "2π", "cosec", "sec", "cot",
                    "4", "5", "6", "×", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "1", "2", "3", chr(247), "ln", "Deg", "Rad", "e",
                    "0", ".", "%", "=", "log", "(", ")", "x!"]

rowvalue = 2
columnvalue = 0
for i in button_text_list:
    if i in '0123456789':
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#faba0a' , activebackground='#CCA01D', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    elif i in ["Del", "AC", "√", "+", "-", "×",chr(247), ".", "%", "="]:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#98d8ce' , activebackground='#c3dad4', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    else:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#0eab8c' , activebackground='#65a897', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

def click_angle(string):
    global angle_unit
    if string =="Deg":
        angle_unit = "Deg"
        angle_label = Label(main, text='All input and output angles are in Degrees',font=('times new roman',10, 'bold'), bg='#000000', fg='#F1DDCF', bd=5)
        angle_label.grid(row=1, column=2, columnspan=6)
    else:
        angle_unit = "Rad"
        angle_label = Label(main, text='All input and output angles are in Radians',font=('times new roman',10, 'bold'), bg='#000000', fg='#F1DDCF', bd=5)
        angle_label.grid(row=1, column=2, columnspan=6)

angle_button1 = Button(main, font=('calibri', 12 ,'bold'), width=5, height=0, bd=4, relief=RIDGE, text="Rad", bg='#AB274F' , activebackground='#AB274F', command=lambda button="Rad": click_angle(button))
angle_button1.grid(row=1, column=0, padx=1,pady=1)
angle_button2 = Button(main, font=('calibri', 12 ,'bold'), width=5, height=0, bd=4, relief=RIDGE, text="Deg", bg='#AB274F' , activebackground='#AB274F', command=lambda button="Deg": click_angle(button))
angle_button2.grid(row=1, column=1, padx=1,pady=1)
angle_label = Label(main, text='All input and output angles are in Degrees',font=('times new roman',10, 'bold'), bg='#000000', fg='#F1DDCF', bd=5)
angle_label.grid(row=1, column=2, columnspan=6)

def func(x):
    click("=")
main.bind('<Return>', func)

main.mainloop()