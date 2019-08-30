import tkinter as tk
from tkinter import *
import random
import time

win = tk.Tk()
expression = ""
l = '1234567890'
random = ''.join(random.sample(l,4))
    
def press(num):
    global expression
    expression = expression+str(num)
    equation.set(expression)

def clear(): 
    global expression 
    expression = ''
    equation.set('')

def cow():
    global random
    c = 0
    d = 0
    for i in range(4):
        if random[i]==expression[i]:
            c = c+1
        else:
            d = d+1
    print(c)
    print(expression)
    q.set(c)
    b.set(d)
    r.set(random)
    
        
            
print(random)   
    
equation = StringVar()
q = StringVar()
b = StringVar()
r = StringVar()

    
canvas = tk.Canvas(win, height=700, width=800)
canvas.pack()

frame = tk.Frame(win,bg='black',bd=5)
frame.place(relx = 0, rely = 0, relwidth = 1, relheight=1)

frame1 = tk.Frame(win,bg='blue',bd=5)
frame1.place(relx = 0.01, rely = 0.01, relwidth = 1, relheight=0.1)

frame2 = tk.Frame(frame,bd=5)
frame2.place(relx = 0.1,rely=0.35,relwidth = 0.8,relheight =0.5)

label = tk.Label(frame1, text='COW BULL GAME',font=200,bg='blue')
label.place(relx = 0.4, rely = 0.3)

label1 = tk.Label(frame,text='Guess 4 Digits : ',bg='blue',font=40)
label1.place(relx = 0.1,rely = 0.3)


entry = tk.Entry(frame,textvariable=equation,font=40)
entry.place(relx = 0.4, rely = 0.3)

entry1 = tk.Entry(frame2, textvariable=q,font = 40)
entry1.place(relx = 0.1, rely = 0.1)

entry2 = tk.Entry(frame2, textvariable=b,font = 40)
entry2.place(relx = 0.1, rely = 0.2)

entry3 = tk.Entry(frame2, textvariable=r,font = 40)
entry3.place(relx = 0.25, rely = 0.8)

button1 = tk.Button(frame,text='1',font=40,command = lambda:press(1))
button1.place(relx=0.1, rely=0.2)

button2 = tk.Button(frame,text='2',font=40,command = lambda:press(2))
button2.place(relx=0.15, rely=0.2)

button3 = tk.Button(frame,text='3',font=40,command = lambda:press(3))
button3.place(relx=0.20, rely=0.2)

button4 = tk.Button(frame,text='4',font=40,command = lambda:press(4))
button4.place(relx=0.25, rely=0.2)

button5 = tk.Button(frame,text='5',font=40,command = lambda:press(5))
button5.place(relx=0.30, rely=0.2)

button6 = tk.Button(frame,text='6',font=40,command = lambda:press(6))
button6.place(relx=0.35, rely=0.2)

button7 = tk.Button(frame,text='7',font=40,command = lambda:press(7))
button7.place(relx=0.40, rely=0.2)

button8 = tk.Button(frame,text='8',font=40,command = lambda:press(8))
button8.place(relx=0.45, rely=0.2)

button9 = tk.Button(frame,text='9',font=40,command = lambda:press(9))
button9.place(relx=0.50, rely=0.2)

button0 = tk.Button(frame,text='0',font=40,command = lambda:press(0))
button0.place(relx=0.55, rely=0.2)

buttonc = tk.Button(frame,text='CLEAR',font=40,bg='blue',command = clear)
buttonc.place(relx=0.60, rely=0.2)

label2 = tk.Label(frame2,text='Cow',bg='grey',font=40)
label2.place(relx = 0,rely = 0.1)

label3 = tk.Label(frame2,text='Bull',bg='grey',font=40)
label3.place(relx = 0,rely = 0.2)

label4 = tk.Label(frame2,text='Correct Guess:',bg='green',font=40)
label4.place(relx = 0,rely = 0.8)


buttons = tk.Button(frame,text='START',bg='green',font=40,command = cow)
buttons.place(relx=0.80,rely=0.3)

buttond = tk.Button(frame2,text='EXIT',font=40,bg='red',command = win.destroy)
buttond.place(relx=0.80,rely=0.8)

label4 = tk.Label(frame,text='RULES: Guess 4 Digits where Cow will display for correct digit and Bull will display for wrong digit.',font=40)
label4.place(relx = 0.01,rely = 0.1)



win.mainloop()
