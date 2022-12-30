from tkinter import *
import MyMath

root = Tk()
root.title('Scientific Calculator')
root.config(bg='#000000')
root.geometry('450x335')
root.resizable(FALSE,FALSE)

entryField = Entry(root, font=('times new roman',20,'bold'), bg='#000000', fg='#F1DDCF', bd=5, relief=RIDGE, width = 31)
entryField.grid(row=0,column=0,columnspan=8)

def click(value):
    val = entryField.get()
    if value=='Del':                    
        val = val[0:len(val) - 1]
        entryField.delete(0,END)
        entryField.insert(0, val)
    elif value=='AC':
        entryField.delete(0,END)
    elif value=="√":
        val = MyMath.sqroot(eval(val))
        entryField.delete(0,END)
        entryField.insert(0, val)
    elif value=="π":
        val = MyMath.pi
        entryField.delete(0,END)
        entryField.insert(0, val)
    elif value=="sinθ":
        val = MyMath.sin(eval(val))
        entryField.delete(0,END)
        entryField.insert(0, val)

        

button_text_list = ["Del", "AC", "√", "+", "π", "sinθ", "cosθ", "tanθ",
                    "1", "2", "3", "-", "2π", "cosecθ", "secθ", "cotθ",
                    "4", "5", "6", "×", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
button_bg1 = '#faba0a'
button_bg2 = '#0eab8c'
button_bg3 = '#98d8ce'
rowvalue = 1
columnvalue = 0
for i in button_text_list:
    if i in '0123456789':
        button_clear = Button(root, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg=button_bg1 , activebackground='#CCA01D', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    elif i in ["Del", "AC", "√", "+", "-", "×",chr(247), ".", "%", "="]:
        button_clear = Button(root, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg=button_bg3 , activebackground='#c3dad4', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    else:
        button_clear = Button(root, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg=button_bg2 , activebackground='#65a897', command=lambda button=i: click(button)).grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0


root.mainloop()
