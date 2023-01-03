from tkinter import *
import MyMath
from tkinter import messagebox

main = Tk()
main.title('Scientific Calculator 2.0')
main.config(bg='#000000')
main.geometry('448x565')
main.resizable(FALSE,FALSE)

def open_mc():
    main.destroy()
    import main_page
def open_help():
    import instructions

my_menu = Menu(main)
main.config(menu=my_menu)

back = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Go Back", menu=back)
back.add_command(label='Back to Calculator', command=open_mc)
back.add_separator()
back.add_command(label='Exit', command=main.destroy)

instruction = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Help", menu=instruction)
instruction.add_command(label='How to use calculator', command=open_help)

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
            except ValueError:
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
            except ValueError:
                messagebox.showerror('Math Error','Logarithms of negative number or zero is not defined.')
        elif value=="x!":
            try:
                result = MyMath.factorial(eval(val))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error','Sorry, factorial does not exist for negative numbers.')
        elif value=="logn":
            try:
                l=val.split(',')
                result = MyMath.logn(eval(l[0]),eval(l[1]))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error','Logarithms of negative number is not defined.')
        elif value=="\u207F√":
            l=val.split(',')
            result = MyMath.nthroot(eval(l[0]),eval(l[1]))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="eˣ":
            result = MyMath.exp(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="Fact":
            result = MyMath.factors(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, str(result))
        
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
            try:
                result=MyMath.degrees(MyMath.sin_inv(eval(val)))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error','x cannot be outside the range [-1,1].')
        elif value=="cos\u207B\u00B9":
            try:
                result=MyMath.degrees(MyMath.cos_inv(eval(val)))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('x cannot be outside the range [-1,1].')
        elif value=="tan\u207B\u00B9":
            result=MyMath.degrees(MyMath.tan_inv(eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cosec\u207B\u00B9":
            try:
                result=MyMath.degrees(MyMath.cosec_inv(eval(val)))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error', 'x cannot be in the range (-1,1).')
        elif value=="sec\u207B\u00B9":
            try:
                result=MyMath.degrees(MyMath.sec_inv(eval(val)))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error','x cannot be in the range (-1,1).')
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
            try:
                result = MyMath.cosech((eval(val)))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error','Domain of cosech is R-{0}.')
        elif value=="sech":
            result = MyMath.sech((eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="coth":
            try:
                result = MyMath.coth((eval(val)))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error','Domain of coth is R-{0}.')
        elif value=="sinh\u207B\u00B9":
            result = MyMath.sinh_inv((eval(val)))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="cosh\u207B\u00B9":
            try:
                result = MyMath.cosh_inv((eval(val)))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error','Domain of cosh\u207B\u00B9 is [1,∞).')
        elif value=="tanh\u207B\u00B9":
            try:
                result = MyMath.tanh_inv((eval(val)))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error','Domain of tanh\u207B\u00B9 is (-1,1).')
        elif value=="csch\u207B\u00B9":
            try:
                result = MyMath.cosech_inv((eval(val)))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error','Domain of cosech_inv is R-{0}.')
        elif value=="sech\u207B\u00B9":
            try:
                result = MyMath.sech_inv((eval(val)))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error', 'Domain of sech_inv is (0,1].')
        elif value=="coth\u207B\u00B9":
            try:
                result = MyMath.coth_inv((eval(val)))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error','Domain of coth_inv is (-∞,-1)u(1,+∞).')

            
        #Special Functions
        elif value=="nCr":
            try:
                if 'C' in val:
                    l=val.split('C')
                else:
                    l=val.split('c')
                result=MyMath.nCr(eval(l[0]), eval(l[1]))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error','r cannot be greater than n.')
        elif value=="nPr":
            try:
                if 'P' in val:
                    l=val.split('P')
                else:
                    l=val.split('p')
                result=MyMath.nPr(eval(l[0]), eval(l[1]))
                entryField.delete(0,END)
                entryField.insert(0, result)
            except ValueError:
                messagebox.showerror('Math Error','r cannot be greater than n.')
        elif value=="LCM":
            l=val.split(',')
            for i in range(len(l)):
                l[i]=int(l[i])
            result=MyMath.lcm(l)
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="HCF":
            l=val.split(',')
            for i in range(len(l)):
                l[i]=int(l[i])
            result=MyMath.hcf(l)
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="Inv":
            result = MyMath.inv(eval(val))
            entryField.delete(0,END)
            entryField.insert(0, result)
        elif value=="Abs":
            result = MyMath.abs(eval(val))
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
        
        elif value=="CONST":
            messagebox.showinfo('Under Construction', 'Button does not have a function yet.')
        elif value==" ":
            messagebox.showinfo('Under Construction', 'Button does not have a function yet.')
        else:
            entryField.insert(END, value)
    except SyntaxError:
        pass
    except IndexError:
        pass
    except NameError:
        pass
    except ZeroDivisionError:
        messagebox.showerror('Math Error', 'Division by zero is not possible.')
    except ValueError:
        pass

button_text_list = ["Del", "AC", "√", "+", "π", "sin", "cos", "tan",
                    "7", "8", "9", "-", "2π", "cosec", "sec", "cot",
                    "4", "5", "6", "×", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "1", "2", "3", chr(247), "ln", "Deg", "Rad", "e",
                    "0", ".", "%", "=", "log", "(", ")", "x!",
                    "sin\u207B\u00B9","cos\u207B\u00B9","tan\u207B\u00B9","cosec\u207B\u00B9","sec\u207B\u00B9","cot\u207B\u00B9","nCr","nPr",
                    "sinh","cosh","tanh","cosech","sech","coth","LCM","HCF",
                    "sinh\u207B\u00B9","cosh\u207B\u00B9","tanh\u207B\u00B9","csch\u207B\u00B9","sech\u207B\u00B9","coth\u207B\u00B9","Inv","Abs",
                    "CONST"," "," ",",","Fact","eˣ","\u207F√","logn"]

rowvalue = 1
columnvalue = 0
for i in button_text_list:
    if i in '0123456789':
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#faba0a' , activebackground='#CCA01D', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    elif i in ["Del", "AC", "√", "+", "-", "×",chr(247), ".", "%", "="]:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#98d8ce' , activebackground='#c3dad4', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    elif i in ["sin\u207B\u00B9","cos\u207B\u00B9","tan\u207B\u00B9","cosec\u207B\u00B9","sec\u207B\u00B9","cot\u207B\u00B9",
                "sinh","cosh","tanh","cosech","sech","coth","sinh\u207B\u00B9","cosh\u207B\u00B9","tanh\u207B\u00B9","csch\u207B\u00B9","sech\u207B\u00B9","coth\u207B\u00B9"]:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#DB2D43' , activebackground='#F19CBB', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    elif i in ["nCr","nPr","LCM","HCF","Inv","Abs","Fact","eˣ","\u207F√","logn",","]:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#007FFF' , activebackground='#89CFF0', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    elif i in [" ","CONST"]:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='grey' , activebackground='grey', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    else:
        button = Button(main, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg='#0eab8c' , activebackground='#65a897', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

main.mainloop()