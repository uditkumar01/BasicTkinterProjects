from tkinter import *
from tkinter import ttk
import math
import tkinter.messagebox as msg
root=Tk()
root.title('Calculator 2.0')
root.geometry('222x222')

values=StringVar()
values.set("")
f1=Frame(root,bg='maroon',borderwidth=9)
f1.pack(side=TOP)
scroll1=Scrollbar(orient=HORIZONTAL)
screen = Entry(f1,width=25,textvariable=values,borderwidth=8,xscrollcommand=scroll1.set)
screen.focus()
screen.pack(side=LEFT)

def submit(a):
    result=0
    numbers=[]
    oper=[]
    for i in a:
        if (not (48<=ord(i)<=58)) :
            oper.append(i)
            numbers.append(int(result))
            result=0
        else:
            result=10*result+int(i)
    result=numbers[0]
    p=0
    for i in range(len(oper)):
        c=oper[i]
        p+=1
        if c=='=':
            break
        elif(c=='+'):
            result+=numbers[p]
        elif(c=='-'):
            result-=numbers[p]
        elif(c=='/'):
            result/=numbers[p]
        elif(c=='x'):
            result*=numbers[p]
        elif(c=='^'):
            result=math.pow(result,numbers[p])
        elif(c=='`'):
            q=1/numbers[p]
            result=math.pow(result,q)
        elif(c=='l'):
            result=math.log(result,numbers[p])
        elif(c=='L'):
            result=math.log(result)
        elif(c=='s'):
            result=result*(math.pi/180)
            result=math.sin(result)
        elif(c=='c'):
            result=result*(math.pi/180)
            result=math.cos(result)
        elif(c=='S'):
            result=math.asin(result)
            result=result*(180/math.pi)
        elif(c=='C'):
            result=math.acos(result)
            result=result*(180/math.pi)
    values.set(result)
    screen.update()
    screen.focus()

def functions():
    msg.showinfo(title='All Functions',message='Here, you can do a number of Operations like \"  + , x , / , -  \" simultaneously. Hope you like it.')

def Quit():
    ans=msg.askyesno(title='Terminating Application !!!',message='Do You Want To Quit ?')
    if ans:
        quit()
    else:
        pass

def about():
    msg.showinfo(title='About Us',message='Calculator 1.0 (colored version) By UDIT KUMAR')

def rating():
    win=Tk()
    win.title('Rate Us Or Comment Too !!!')
    label1=Label(win,text="Plz rate us!!!",bg='light yellow',fg='maroon')
    label1.pack()
    rater=Scale(win,from_=1,to_=5,orient=HORIZONTAL)
    rater.pack(anchor=CENTER)
    rater.set(3)
    label2=Label(win,text="Plz Comment Now !!!", fg='green')
    label2.pack()
    f1=Frame(win,bg='light green',borderwidth=6)
    f1.pack(anchor=CENTER)
    entry=Entry(f1,width=20)
    entry.pack()
    b1=Button(win,text='Submit',command=quit,bg='light blue',fg='blue')
    b1.pack(anchor=CENTER)
    win.mainloop()

def cal(event):
    global values
    cal_string=event.widget.cget('text')
    values.set(values.get()+cal_string)
    screen.update()
    m=''
    m=values.get()
    if '=' in m:
        submit(m)
f2=Frame(root,bg='red',borderwidth=10,relief=GROOVE)
f2.pack(side=TOP)
button9 = Button(f2,text='9',padx=7,pady=4)
button9.bind('<Button-1>',cal)
button9.pack(side=LEFT,padx=2,pady=1)
button8 = Button(f2,text='8',padx=7,pady=4)
button8.bind('<Button-1>',cal)
button8.pack(side=LEFT,padx=2,pady=1)
button7 = Button(f2,text='7',padx=7,pady=4)
button7.pack(side=LEFT,padx=2,pady=1)
button7.bind('<Button-1>',cal)

f3=Frame(root,bg='orange',borderwidth=10,relief=GROOVE)
f3.pack(side=TOP)
button6 = Button(f2,text='6',padx=7,pady=4)
button6.bind('<Button-1>',cal)
button6.pack(side=LEFT,padx=2,pady=1)
button5 = Button(f2,text='5',padx=7,pady=4)
button5.bind('<Button-1>',cal)
button5.pack(side=LEFT,padx=2,pady=1)

button4 = Button(f3,text='4',padx=7,pady=4)
button4.pack(side=LEFT,padx=2,pady=1)
button4.bind('<Button-1>',cal)
button3 = Button(f3,text='3',padx=7,pady=4)
button3.pack(side=LEFT,padx=2,pady=1)
button3.bind('<Button-1>',cal)
button2 = Button(f3,text='2',padx=7,pady=4)
button2.pack(side=LEFT,padx=2,pady=1)
button2.bind('<Button-1>',cal)
button1 = Button(f3,text='1',padx=7,pady=4)
button1.pack(side=LEFT,padx=2,pady=1)
button1.bind('<Button-1>',cal)
button0 = Button(f3,text='0',padx=7,pady=4)
button0.pack(side=LEFT,padx=2,pady=1)
button0.bind('<Button-1>',cal)
 
# 0-9 button made above
f4=Frame(root,bg='yellow',borderwidth=10,relief=GROOVE)
f4.pack(side=TOP)
button_add = Button(f4,text='+',padx=7,pady=4)
button_add.pack(side=LEFT,padx=2,pady=1)
button_add.bind('<Button-1>',cal)
button_minus = Button(f4,text='-',padx=7,pady=4)
button_minus.pack(side=LEFT,padx=2,pady=1)
button_minus.bind('<Button-1>',cal)
button_Mul = Button(f4,text='x',padx=7,pady=4)
button_Mul.pack(side=LEFT,padx=2,pady=1)
button_Mul.bind('<Button-1>',cal)
button_div = Button(f4,text='/',padx=7,pady=4)
button_div.pack(side=LEFT,padx=2,pady=1)
button_div.bind('<Button-1>',cal)
button_eq = Button(f4,text='=',padx=7,pady=4)
button_eq.pack(side=LEFT,padx=2,pady=1)
button_eq.bind('<Button-1>',cal)

# button(+,-,/,x) added

f5=Frame(root,bg='yellow',borderwidth=10,relief=GROOVE)
f5.pack(side=TOP)
button_sq = Button(f5,text='^',padx=7,pady=4)
button_sq.pack(side=LEFT,padx=2,pady=1)
button_sq.bind('<Button-1>',cal)
button_root = Button(f5,text='`',padx=7,pady=4)
button_root.pack(side=LEFT,padx=2,pady=1)
button_root.bind('<Button-1>',cal)
button_log = Button(f5,text='l',padx=7,pady=4)
button_log.pack(side=LEFT,padx=2,pady=1)
button_log.bind('<Button-1>',cal)
button_ln = Button(f5,text='L',padx=7,pady=4)
button_ln.pack(side=LEFT,padx=2,pady=1)
button_ln.bind('<Button-1>',cal)

f6=Frame(root,bg='light yellow',borderwidth=10,relief=GROOVE)
f6.pack(side=TOP)
button_sin = Button(f6,text='s',padx=7,pady=4)
button_sin.pack(side=LEFT,padx=2,pady=1)
button_sin.bind('<Button-1>',cal)
button_cos = Button(f6,text='c',padx=7,pady=4)
button_cos.pack(side=LEFT,padx=2,pady=1)
button_cos.bind('<Button-1>',cal)
button_asin = Button(f6,text='C',padx=7,pady=4)
button_asin.pack(side=LEFT,padx=2,pady=1)
button_asin.bind('<Button-1>',cal)
button_acos = Button(f6,text='S',padx=7,pady=4)
button_acos.pack(side=LEFT,padx=2,pady=1)
button_acos.bind('<Button-1>',cal)

file_menu=Menu(root, borderwidth=5, bg='yellow', fg= 'green', activebackground='orange',activeforeground='red',relief=RAISED)
file=Menu(file_menu,tearoff=0)
file.add_command(label='Functions',command=functions)
file.add_command(label='Close',command=Quit)
file_menu.add_cascade(label='File',menu=file)


m=Menu(file_menu,tearoff=0)
m.add_command(label='About Us',command=about)
m.add_command(label='Rate Us',command=rating)
file_menu.add_cascade(label='More',menu=m)
root.config(menu=file_menu)

root.mainloop()
