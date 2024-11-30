from tkinter import*
import math
exp=""
def press(num):
    global exp
    exp=exp+str(num)
    equation.set(exp)
def equal_press():
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
        exp=""
    except:
        equation.set("error")
        exp=""
def cl():
    global exp
    exp=""
    equation.set("")
def delete_char():
    global exp
    exp = exp[:-1] 
    equation.set(exp)
def sqrt():
    global exp
    try:
        result = str(math.sqrt(float(exp)))
        equation.set(result)
        exp = result
    except:
        equation.set("error")
        exp = ""
def pi_value():
    global exp
    exp = exp + str(math.pi) 
    equation.set(exp)
def percentage():
    global exp
    try:
        result = str(float(exp) / 100)
        equation.set(result)
        exp = result
    except:
        equation.set("error")
        exp = ""
def exponentiation():
    global exp
    exp = exp + '**'
    equation.set()
def log():
    global exp
    try:
        result = str(math.log(float(exp)))  
        equation.set(result)
        exp = result
    except:
        equation.set("error")
        exp = ""

root=Tk()
root.title("Calculator")
root.geometry("400x400")
equation=StringVar()
txt=Entry(root,textvariable=equation)
txt.grid(columnspan=4,row=1,ipadx=30)
button1=Button(root,text='1',fg='black',command=lambda: press(1),height=4,width=8)
button1.grid(row=5,column=0)
button2=Button(root,text='2',fg='black',command=lambda: press(2),height=4,width=8)
button2.grid(row=5,column=1)
button3=Button(root,text='3',fg='black',command=lambda: press(3),height=4,width=8)
button3.grid(row=5,column=2)
button4=Button(root,text='4',fg='black',command=lambda: press(4),height=4,width=8)
button4.grid(row=4,column=0)
button5=Button(root,text='5',fg='black',command=lambda: press(5),height=4,width=8)
button5.grid(row=4,column=1)
button6=Button(root,text='6',fg='black',command=lambda: press(6),height=4,width=8)
button6.grid(row=4,column=2)
button7=Button(root,text='7',fg='black',command=lambda: press(7),height=4,width=8)
button7.grid(row=3,column=0)
button8=Button(root,text='8',fg='black',command=lambda: press(8),height=4,width=8)
button8.grid(row=3,column=1)
button9=Button(root,text='9',fg='black',command=lambda: press(9),height=4,width=8)
button9.grid(row=3,column=2)
button0=Button(root,text='0',fg='black',command=lambda: press(0),height=4,width=8)
button0.grid(row=6,column=1)
Add=Button(root,text='+',fg='black',command=lambda: press('+'),height=4,width=8)
Add.grid(row=5,column=4)
minus=Button(root,text='-',fg='black',command=lambda: press('-'),height=4,width=8)
minus.grid(row=4,column=4)
multiply=Button(root,text='*',fg='black',command=lambda: press('*'),height=4,width=8)
multiply.grid(row=3,column=4)
divide=Button(root,text='/',fg='black',command=lambda: press('/'),height=4,width=8)
divide.grid(row=2,column=4)
equal=Button(root,text='=',fg='black',command=equal_press,height=4,width=8)
equal.grid(row=6,column=4)
clear=Button(root,text='Clear',fg='black',command=cl,height=4,width=8)
clear.grid(row=2,column=0)
Decimal=Button(root,text='.',fg='black',command=lambda: press('.'),height=4,width=8)
Decimal.grid(row=6,column=2)
left_paren = Button(root, text='(', fg='black', command=lambda: press('('), height=4, width=8)
left_paren.grid(row=2, column=2)
right_paren = Button(root, text=')', fg='black', command=lambda: press(')'), height=4, width=8)
right_paren.grid(row=2, column=3)
sqrt_btn = Button(root, text='√', fg='black', command=sqrt, height=4, width=8)
sqrt_btn.grid(row=4, column=3)
pi_btn = Button(root, text='π', fg='black', command=pi_value, height=4, width=8)
pi_btn.grid(row=3, column=3)
Delete = Button(root, text='del', fg='black', command=delete_char, height=4, width=8)
Delete.grid(row=2, column=1)
percent_btn = Button(root, text='%', fg='black', command=percentage, height=4, width=8)
percent_btn.grid(row=6, column=0)
exponent_btn = Button(root, text='^', fg='black', command=exponentiation, height=4, width=8)
exponent_btn.grid(row=5, column=3)
log_btn = Button(root, text='log', fg='black', command=log, height=4, width=8)
log_btn.grid(row=6, column=3)
root.mainloop()