import tkinter as tk 
from tkinter import ttk
import tkinter.messagebox as msg
import sys
import os
l = []
def restart_program():

    global l
    l.clear()
    l = [['.' for j in range(3)] for i in range(3)]
    button00.config(text='')
    button01.config(text='')
    button02.config(text='')
    button10.config(text='')
    button11.config(text='')
    button12.config(text='')
    button20.config(text='')
    button21.config(text='')
    button22.config(text='')
    label_box.config(text=" Let's begin !!! ")

def functions():
    msg.showinfo(title='Game Info',message='Always "X" starts the game and all the info will be show below while playing .')

def Quit():
    ans=msg.askyesno(title='Terminating Application !!!',message='Do You Want To Quit ?')
    if ans:
        quit()
    else:
        pass

def about():
    msg.showinfo(title='About Us',message='TIC - TAC - TOE (colored version) By UDIT KUMAR')

def rating():
    win=tk.Tk()
    win.title('Rate Us Or Comment Too !!!')
    mf = tk.Frame(win,bg = "orange",borderwidth = 6,relief = tk.GROOVE)
    mf.pack(side=tk.TOP,padx = 20,pady = 30)
    label1=tk.Label(mf,text="Plz rate us!!!",bg='light yellow',fg='maroon')
    label1.pack()
    rater=tk.Scale(mf,from_=1,to_=5,orient=tk.HORIZONTAL)
    rater.pack(anchor=tk.CENTER,pady =5)
    rater.set(3)
    label2=tk.Label(mf,text="Plz Comment Now !!!", fg='green')
    label2.pack()
    f1=tk.Frame(mf,bg='yellow',borderwidth=6)
    f1.pack(side=tk.TOP,padx = 10,pady = 5)
    entry=tk.Entry(f1,width=20)
    entry.pack()
    b1=tk.Button(mf,text='Submit',command=quit,bg='light blue',fg='blue')
    b1.pack(anchor=tk.CENTER)
    win.mainloop()


def won(c):
    msg.showinfo(title = "Winner Winner Chicken Dinner !!!",message="Congrats, {} won !!!".format(c))

def game_fun():
    global l
    h_count ,v_count= [],[]

    # vertical checking
    for i in range(3):
        x,o = 0,0
        for j in range(3):
            if l[j][i] == 'X':
                x+=1
            elif l[j][i] == 'O':
                o+=1
        h_count.append([str(x),str(o)])
    # print(h_count)


    X,O,dots = 0,0,0
    for i in range(3):
        v_count.append([str(l[i].count('X')),str(l[i].count('O'))])

        X += l[i].count('X')
        O += l[i].count('O')
        dots += l[i].count('.')

    if (X < O) and (X > O+1):
        print('INVALID INPUT: Code 1')
        label_box.config(text = "INVALID INPUT: Code 1")
        exit()
    # print(v_count)

    x,o,p,q = 0,0,0,0
    for i in range(3):
        if h_count[i][0] == '3':
            x+=1
        if h_count[i][1] == '3':
            o+=1
        if v_count[i][0] == '3':
            p+=1
        if v_count[i][1] == '3':
            q+=1
    if (x == 1 and o == 1) or (p == 1 and q == 1):
        print("INVALID INPUT: Code 2")
        label_box.config(text = "INVALID INPUT: Code 2")
    elif (x == 1 and o == 0) or (p == 1 and q == 0) and (O == X-1):
        print("X won.")
        label_box.config(text = "X won !!!")
        won('X')
        restart_program()
    elif ((x == 0 and o == 1) or (p == 0 and q == 1)) and (X == O):
        print("O won.")
        label_box.config(text = "O won !!!")
        won('O')
        restart_program()
    elif (l[0][2] == 'X' and l[1][1] == 'X' and l[2][0] == 'X') and (O >= X):
        print("INVALID INPUT: Code 3")
        label_box.config(text = "INVALID INPUT: Code 3")
    elif (l[0][2] == 'O' and l[1][1] == 'O' and l[2][0] == 'O') and (X != O):
        print("INVALID INPUT: Code 4")
        label_box.config(text = "INVALID INPUT: Code 4")
    elif (l[0][0] == 'X' and l[1][1] == 'X' and l[2][2] == 'X') and (O == 3):
        print("INVALID INPUT: Code 5")
        label_box.config(text = "INVALID INPUT: Code 5")
    elif (l[0][0] == 'O' and l[1][1] == 'O' and l[2][2] == 'O') and (X >= 3):
        print("INVALID INPUT: Code 6")
        label_box.config(text = "INVALID INPUT: Code 6")
    elif (l[0][2] == 'X' and l[1][1] == 'X' and l[2][0] == 'X') and (X > O):
        print("X won.")
        label_box.config(text = "X won !!!")
        won('X')
        restart_program()
    elif (l[0][2] == 'O' and l[1][1] == 'O' and l[2][0] == 'O') and (O <= X):
        print("O won.")
        label_box.config(text = "O won !!!")
        won('O')
        restart_program()
    elif (l[0][0] == 'X' and l[1][1] == 'X' and l[2][2] == 'X') and (X > O):
        print("X won.")
        label_box.config(text = "X won !!!")
        won('X')
        restart_program()
    elif (l[0][0] == 'Y' and l[1][1] == 'Y' and l[2][2] == 'Y') and (O < X):
        print("O won.")
        label_box.config(text = "O won !!!")
        won('O')
        restart_program()
    elif ((x == 0 and o == 1) or (p == 0 and q == 1)) and (X != O):
        print("INVALID INPUT: Code 7")
        label_box.config(text = "INVALID INPUT: Code 7")
    elif ((x == 1 and o == 0) or (p == 1 and q == 0)) and (O != X-1):
        print("INVALID INPUT: Code 8")
        label_box.config(text = "INVALID INPUT: Code 8")
    elif (X == O and dots != 0):
        print("X's turn.")
        label_box.config(text = " X 's Turn ")
    elif (X-1 == O and dots != 0):
        print("O's turn.")
        label_box.config(text = " O 's Turn ")
    elif (X-1 == O and dots == 0):
        print("It's a draw.")
        label_box.config(text = " It's a draw. ")
    else:
        print("INVALID INPUT: Code 9")
        label_box.config(text = "INVALID INPUT: Code 9")






















l = [['.' for j in range(3)] for i in range(3)]
x = 0
def button_00(event):
    global l
    global x
    if x == 0 and l[0][0] == ".":
        l[0][0] = 'X'
        button00.config(text="X")
        x = 1
        game_fun()
    elif x == 1 and l[0][0] == ".":
        l[0][0] = 'O'
        button00.config(text="O")
        x = 0
        game_fun()
    else:
        print("already Occupied")
    print(l)
def button_01(event):
    global l
    global x
    if x == 0 and l[0][1] == ".":
        l[0][1] = 'X'
        button01.config(text="X")
        x = 1
        game_fun()
    elif x == 1 and l[0][1] == ".":
        l[0][1] = 'O'
        button01.config(text="O")
        x = 0
        game_fun()
    else:
        print("already Occupied")
    print(l)
def button_02(event):
    global l
    global x
    if x == 0 and l[0][2] == ".":
        l[0][2] = 'X'
        button02.config(text="X")
        x = 1
        game_fun()
    elif x == 1 and l[0][2] == ".":
        l[0][2] = 'O'
        button02.config(text="O")
        x = 0
        game_fun()
    else:
        print("already Occupied")
    print(l)

def button_10(event):
    global l
    global x
    if x == 0 and l[1][0] == ".":
        l[1][0] = 'X'
        button10.config(text="X")
        x = 1
        game_fun()
    elif x == 1 and l[1][0] == ".":
        l[1][0] = 'O'
        button10.config(text="O")
        x = 0
        game_fun()
    else:
        print("already Occupied")
    print(l)

def button_11(event):
    global l
    global x
    if x == 0 and l[1][1] == ".":
        l[1][1] = 'X'
        button11.config(text="X")
        x = 1
        game_fun()
    elif x == 1 and l[1][1] == ".":
        l[1][1] = 'O'
        button11.config(text="O")
        x = 0
        game_fun()
    else:
        print("already Occupied")
    print(l)

def button_12(event):
    global l
    global x
    if x == 0 and l[1][2] == ".":
        l[1][2] = 'X'
        button12.config(text="X")
        x = 1
        game_fun()
    elif x == 1 and l[1][2] == ".":
        l[1][2] = 'O'
        button12.config(text="O")
        x = 0
        game_fun()
    else:
        print("already Occupied")
    print(l)

def button_20(event):
    global l
    global x
    if x == 0 and l[2][0] == ".":
        l[2][0] = 'X'
        button20.config(text="X")
        x = 1
        game_fun()
    elif x == 1 and l[2][0] == ".":
        l[2][0] = 'O'
        button20.config(text="O")
        x = 0
        game_fun()
    else:
        print("already Occupied")
    print(l)

def button_21(event):
    global l
    global x
    if x == 0 and l[2][1] == ".":
        l[2][1] = 'X'
        button21.config(text="X")
        x = 1
        game_fun()
    elif x == 1 and l[2][1] == ".":
        l[2][1] = 'O'
        button21.config(text="O")
        x = 0
        game_fun()
    else:
        print("already Occupied")
    print(l)

def button_22(event):
    global l
    global x
    if x == 0 and l[2][2] == ".":
        l[2][2] = 'X'
        button22.config(text="X")
        x = 1
        game_fun()
    elif x == 1 and l[2][2] == ".":
        l[2][2] = 'O'
        button22.config(text="O")
        x = 0
        game_fun()
    else:
        print("already Occupied")
    print(l)

print(l)
root = tk.Tk()
root.title("TIC - TAC - TOE")
title_frame = tk.Frame(root,bg = "light blue",borderwidth = 6,relief = tk.GROOVE)
title_frame.pack(side = tk.TOP)
label_title = tk.Label(title_frame,text = " TIC - TAC - TOE ")
label_title.pack(side = tk.TOP)
label_title.config(font=("Courier",12, 'bold'))
root.geometry("300x400")

main_frame = tk.Frame(root,bg = "light blue",borderwidth = 6,relief = tk.GROOVE)
main_frame.pack(side = tk.TOP,pady=10)
row1 = tk.Frame(main_frame,bg = "orange",borderwidth = 6,relief = tk.GROOVE)
row1.pack(side=tk.TOP)
button00 = tk.Button(row1,text = "",padx=30,pady=10,relief = tk.RAISED)
button00.pack(side = tk.LEFT,padx=6,pady=6)
button00.bind('<Button-1>',button_00)
button01 = tk.Button(row1,text = "",padx=30,pady=10,relief = tk.RAISED)
button01.pack(side = tk.LEFT,padx=4,pady=6)
button01.bind('<Button-1>',button_01)
button02 = tk.Button(row1,text = "",padx=30,pady=10,relief = tk.RAISED)
button02.pack(side = tk.LEFT,padx=6,pady=6)
button02.bind('<Button-1>',button_02)



row2 = tk.Frame(main_frame,bg = "Yellow",borderwidth = 6,relief = tk.GROOVE)
row2.pack(side=tk.TOP)
button10 = tk.Button(row2,text = "",padx=30,pady=10,relief = tk.RAISED)
button10.pack(side = tk.LEFT,padx=6,pady=6)
button10.bind('<Button-1>',button_10)
button11 = tk.Button(row2,text = "",padx=30,pady=10,relief = tk.RAISED)
button11.pack(side = tk.LEFT,padx=4,pady=6)
button11.bind('<Button-1>',button_11)
button12 = tk.Button(row2,text = "",padx=30,pady=10,relief = tk.RAISED)
button12.pack(side = tk.LEFT,padx=6,pady=6)
button12.bind('<Button-1>',button_12)



row3 = tk.Frame(main_frame,bg = "orange",borderwidth = 6,relief = tk.GROOVE)
row3.pack(side=tk.TOP)
button20 = tk.Button(row3,text = "",padx=30,pady=10,relief = tk.RAISED)
button20.pack(side = tk.LEFT,padx=6,pady=6)
button20.bind('<Button-1>',button_20)
button21 = tk.Button(row3,text = "",padx=30,pady=10,relief = tk.RAISED)
button21.pack(side = tk.LEFT,padx=4,pady=6)
button21.bind('<Button-1>',button_21)
button22 = tk.Button(row3,text = "",padx=30,pady=10,relief = tk.RAISED)
button22.pack(side = tk.LEFT,padx=6,pady=6)
button22.bind('<Button-1>',button_22)


row4 = tk.Frame(root,bg = "orange",borderwidth = 6,relief = tk.GROOVE)
row4.pack(side=tk.TOP,padx = 20,pady = 30)
label_box = tk.Label(row4,text = "Let's Begin !!!")
label_box.pack(side = tk.TOP,padx = 5,pady = 5)


file_menu=tk.Menu(root, borderwidth=5, bg='yellow', fg= 'green', activebackground='orange',activeforeground='red',relief=tk.RAISED)
file=tk.Menu(file_menu,tearoff=0)
file.add_command(label='New Game',command=restart_program)
file.add_command(label='Game info',command=functions)
file.add_command(label='Close',command=Quit)
file_menu.add_cascade(label='File',menu=file)


m=tk.Menu(file_menu,tearoff=0)
m.add_command(label='About Us',command=about)
m.add_command(label='Rate Us',command=rating)
file_menu.add_cascade(label='More',menu=m)
root.config(menu=file_menu)


root.mainloop()

