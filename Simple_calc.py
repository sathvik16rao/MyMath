from tkinter import *
import MyMath
from tkinter import messagebox

main = Tk()
main.title('Simple Calculator')
main.config(bg='#000000')
main.geometry('225x335')
main.resizable(FALSE,FALSE)

def open_mc():
    main.destroy()
    import main_page

my_menu = Menu(main)
main.config(menu=my_menu)

back = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Go Back", menu=back)
back.add_command(label='Go Back to Calculator', command=open_mc)
back.add_separator()
back.add_command(label='Exit', command=main.destroy)

entryField = Entry(main, font=('times new roman',20,'bold'), bg='#000000', fg='#F1DDCF', bd=5, relief=RIDGE, width = 15, insertbackground = 'white')
entryField.grid(row=0,column=0,columnspan=8)

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
        elif value=="%":
            result = (eval(val))*100
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
        pass
    except ZeroDivisionError:
        messagebox.showerror('Math Error', "Oops! Division by zero will break math and we don't want that now, do we?")

button_text_list = ["Del", "AC", "√", "+",
                    "7", "8", "9", "-",
                    "4", "5", "6", "×",
                    "1", "2", "3", chr(247),
                    "0", ".", "%", "="]

rowvalue = 1
columnvalue = 0
for i in button_text_list:
    if i in '0123456789':
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#faba0a' , activebackground='#CCA01D', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    elif i in ["√", "+", "-", "×",chr(247), ".", "%", "="]:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#98d8ce' , activebackground='#c3dad4', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    else:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#CE2029' , activebackground='#8B0000', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    columnvalue += 1
    if columnvalue > 3:
        rowvalue += 1
        columnvalue = 0

main.mainloop()