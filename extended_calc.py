from tkinter import *
import MyMath

main = Tk()
main.title('Extended Scientific Calculator')
main.config(bg='#000000')
main.geometry('450x450')
main.resizable(FALSE,FALSE)

entryField = Entry(main, font=('times new roman',20,'bold'), bg='#000000', fg='#F1DDCF', bd=5, relief=RIDGE, width = 31, insertbackground = 'white')
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
        elif value=="π":
            result = MyMath.pi
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="2π":
            result = 2*MyMath.pi
            entryField.delete(0,END)
            entryField.insert(0, result)
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
            result = MyMath.ln(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
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
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="log":
            result = MyMath.log(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="x!":
            result = MyMath.factorial(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        
        
        #Trigonometric functions (All inputs/outputs are in degrees)
        elif value=="sin":
            result = MyMath.sin(MyMath.radians(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cos":
            result = MyMath.cos(MyMath.radians(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="tan":
            result = MyMath.cos(MyMath.radians(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cosec":
            result = MyMath.cosec(MyMath.radians(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="sec":
            result = MyMath.sec(MyMath.radians(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cot":
            result = MyMath.cot(MyMath.radians(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="sin\u207B\u00B9":
            result=MyMath.degrees(MyMath.sin_inv(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cos\u207B\u00B9":
            result=MyMath.degrees(MyMath.cos_inv(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="tan\u207B\u00B9":
            result=MyMath.degrees(MyMath.tan_inv(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cosec\u207B\u00B9":
            result=MyMath.degrees(MyMath.cosec_inv(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="sec\u207B\u00B9":
            result=MyMath.degrees(MyMath.sec_inv(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cot\u207B\u00B9":
            result=MyMath.degrees(MyMath.cot_inv(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="sinh":
            result = MyMath.sinh((eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cosh":
            result = MyMath.cosh((eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="tanh":
            result = MyMath.tanh((eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cosech":
            result = MyMath.cosech((eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="sech":
            result = MyMath.sech((eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="coth":
            result = MyMath.coth((eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)

            
        #Special Functions
        elif value=="nCr":
            if 'C' in val:
                l=val.split('C')
            else:
                l=val.split('c')
            result=MyMath.nCr(eval(l[0]), eval(l[1]))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="nPr":
            if 'P' in val:
                l=val.split('P')
            else:
                l=val.split('p')
            result=MyMath.nPr(eval(l[0]), eval(l[1]))
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

button_text_list = ["Del", "AC", "√", "+", "π", "sin", "cos", "tan",
                    "7", "8", "9", "-", "2π", "cosec", "sec", "cot",
                    "4", "5", "6", "×", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "1", "2", "3", chr(247), "ln", "Deg", "Rad", "e",
                    "0", ".", "%", "=", "log", "(", ")", "x!",
                    "sin\u207B\u00B9","cos\u207B\u00B9","tan\u207B\u00B9","cosec\u207B\u00B9","sec\u207B\u00B9","cot\u207B\u00B9","nCr","nPr",
                    "sinh","cosh","tanh","cosech","sech","coth"]

rowvalue = 1
columnvalue = 0
for i in button_text_list:
    if i in '0123456789':
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#faba0a' , activebackground='#CCA01D', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    elif i in ["Del", "AC", "√", "+", "-", "×",chr(247), ".", "%", "="]:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#98d8ce' , activebackground='#c3dad4', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    elif i in ["sin\u207B\u00B9","cos\u207B\u00B9","tan\u207B\u00B9","cosec\u207B\u00B9","sec\u207B\u00B9","cot\u207B\u00B9",
                "sinh","cosh","tanh","cosech","sech","coth"]:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#DB2D43' , activebackground='#F19CBB', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    elif i in ["nCr","nPr"]:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#007FFF' , activebackground='#89CFF0', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    else:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#0eab8c' , activebackground='#65a897', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

main.mainloop()