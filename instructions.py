from tkinter import *

root = Tk()
root.title('Instuctions')
root.geometry('1010x280')
root.resizable(FALSE,FALSE)

l1 = Label(root, text='How to use the calculator', font=('Comic Sans MS',20,'bold'))
l1.place(x=350, y=0)

l2 = Label(root,text='\u2022 You can input complete Arithmetic expressions at once and find its value (Eg: 4-9+8*6).', font=('Times new roman',15))
l2.place(x = 20, y = 50)

l3 = Label(root,text='\u2022 "Del" removes the last character in the expression whereas "AC" clears all.', font=('Times new roman',15))
l3.place(x = 20, y = 75)

l4 = Label(root,text='\u2022 For the function x\u02b8 -> Input value of "x" and then click on the x\u02b8 button. Now input the value of "y". Click "=" for the result.', font=('Times new roman',15))
l4.place(x = 20, y = 100)

l5 = Label(root,text='\u2022 For nCr and nPr, input in the same format or input in the format "n,r" and click on the respective button for the result. (Eg: 6C2 or 6c2 or 6P2 or 6p2 or 6,2)', font=('Times new roman',15))
l5.place(x = 20, y = 125)

l6 = Label(root,text='\u2022 For LCM and HCF, input all th numbers seperated by commas and click on the respective button for the result.', font=('Times new roman',15))
l6.place(x = 20, y = 150)

l7 = Label(root,text='\u2022 For logn, input in the format "number,base" and click on the respective button for result.', font=('Times new roman',15))
l7.place(x = 20, y = 175)

l8 = Label(root,text='\u2022 For \u207F√, input in the format "number,n" and click on the respective button for the result.', font=('Times new roman',15))
l8.place(x = 20, y = 200)

b1 = Button(root, text="Let's Go!", command=root.destroy, font=('calibri', 12 ,'bold'), width=10, height=1, bd=4, relief=RAISED)
b1.place(x = 450, y = 225)

root.mainloop()