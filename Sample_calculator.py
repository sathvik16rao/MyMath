from tkinter import *
root = Tk()
root.title('Scientific Calculator')
root.config(bg='#000000')
root.geometry('680x486')

EntryField = Entry(root, font=('times new roman',20,'bold'), bg='#000000', fg='#F1DDCF', bd=5, relief=RIDGE, width = 31).grid(row=0,column=0,columnspan=10)

button_text_list = ["C", "AC", "√", "+", "π", "sinθ", "cosθ", "tanθ",
                    "1", "2", "3", "-", "2π", "cosecθ", "secθ", "cotθ",
                    "4", "5", "6", "×", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
button_bg1 = '#faba0a'
button_bg2 = '#0eabcancel8c'
button_bg3 = '#98d8ce'
rowvalue = 1
columnvalue = 0
for i in button_text_list:
    if i in '0123456789':
        button_clear = Button(root, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg=button_bg1 , activebackground='#CCA01D').grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    elif i in ["C", "AC", "√", "+", "-", "×",chr(247), ".", "%", "="]:
        button_clear = Button(root, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg=button_bg3 , activebackground='#c3dad4').grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    else:
        button_clear = Button(root, font=('calibri', 12 ,'bold'), width=5, height=2, bd=4, relief=RIDGE, text=i, bg=button_bg2 , activebackground='#65a897').grid(row=rowvalue, column=columnvalue, padx=1,pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0


root.mainloop()
