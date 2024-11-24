import tkinter.ttk
from tkinter import messagebox
import random
runs=0
runs_comp=0
def batting():
    
    list1=[1,2,3,4,5]
    win2=tkinter.Tk()
    win2.geometry("800x500")
    win2.config(bg='black')
    win2.title("Batting")
    label2=tkinter.Label(win2,text="You Are Batting",font=('Arial',40,'bold'),bg='black',fg='green')
    label2.pack()
    def but1():
        x=random.choice(list1)
        val1=1
        if x==1:
            messagebox.showinfo("Round-1 is over","Your are Out")
            win2.destroy()
        else:
            global runs 
            runs=runs+1
            
    def but2():
        x=random.choice(list1)
        val2=2
        if x==2:
            messagebox.showinfo("Round-1 is over","Your are Out")
            win2.destroy()
        else:
            global runs 
            runs=runs+2
    def but3():
        x=random.choice(list1)
        val3=3
        if x==3:
            messagebox.showinfo("Round-1 is over","Your are Out")
            win2.destroy()
        else:
            global runs 
            runs=runs+3
    def but4():
        x=random.choice(list1)
        val4=4
        if x==4:
            messagebox.showinfo("Round-1 is over","Your are Out")
            win2.destroy()
        else:
            global runs 
            runs=runs+4
    def but5():
        x=random.choice(list1)
        val5=5
        if x==5:
            messagebox.showinfo("Round-1 is over","Your are Out")
            win2.destroy()
        else:
            global runs 
            runs=runs+5

    b1=tkinter.Button(win2,text="1",font=('Arial',30,'bold'),command=but1)
    b1.place(x=100,y=200)
    b2=tkinter.Button(win2,text="2",font=('Arial',30,'bold'),command=but2)
    b2.place(x=235,y=200)
    b3=tkinter.Button(win2,text="3",font=('Arial',30,'bold'),command=but3)
    b3.place(x=370,y=200)
    b4=tkinter.Button(win2,text="4",font=('Arial',30,'bold'),command=but4)
    b4.place(x=505,y=200)
    b5=tkinter.Button(win2,text="5",font=('Arial',30,'bold'),command=but5)
    b5.place(x=640,y=200)

    win2.mainloop()
    #----------------------------------
    win3=tkinter.Tk()
    win3.geometry("800x500")
    list1=[1,2,3,4,5]
    win3.config(bg='black')
    win3.title("Bowling")
    label2=tkinter.Label(win3,text="You Are Bowling",font=('Arial',40,'bold'),bg='black',fg='red')
    label2.pack()
    def but1():
        x=random.choice(list1)
        val1=1
        if x==1:
            messagebox.showinfo("Round-2 is over","Your are Out")
            win3.destroy()
        else:
            global runs_comp
            runs_comp=runs_comp+x
    def but2():
        x=random.choice(list1)
        val2=2
        if x==2:
            messagebox.showinfo("Round-2 is over","Computer Is Out")
            win3.destroy()
        else:
           global runs_comp
           runs_comp=runs_comp+x
    def but3():
        x=random.choice(list1)
        val3=3
        if x==3:
            messagebox.showinfo("Round-2 is over","Computer Is Out")
            win3.destroy()
        else:
            global runs_comp
            runs_comp=runs_comp+x
    def but4():
        x=random.choice(list1)
        val4=4
        if x==4:
            messagebox.showinfo("Round-2 is over","Computer Is Out")
            win3.destroy()
        else:
            global runs_comp
            runs_comp=runs_comp+x
    def but5():
        x=random.choice(list1)
        val5=5
        if x==5:
            messagebox.showinfo("Round-2 is over","Computer Is Out")
            win3.destroy()
        else:
            global runs_comp
            runs_comp=runs_comp+x

    b1=tkinter.Button(win3,text="1",font=('Arial',30,'bold'),command=but1)
    b1.place(x=100,y=200)
    b2=tkinter.Button(win3,text="2",font=('Arial',30,'bold'),command=but2)
    b2.place(x=235,y=200)
    b3=tkinter.Button(win3,text="3",font=('Arial',30,'bold'),command=but3)
    b3.place(x=370,y=200)
    b4=tkinter.Button(win3,text="4",font=('Arial',30,'bold'),command=but4)
    b4.place(x=505,y=200)
    b5=tkinter.Button(win3,text="5",font=('Arial',30,'bold'),command=but5)
    b5.place(x=640,y=200)

    win3.mainloop()


def bowling():
    win3=tkinter.Tk()
    win3.geometry("800x500")
    list1=[1,2,3,4,5]
    win3.config(bg='black')
    win3.title("Bowling")
    label2=tkinter.Label(win3,text="You Are Bowling",font=('Arial',40,'bold'),bg='black',fg='red')
    label2.pack()
    def but1():
        x=random.choice(list1)
        val1=1
        if x==1:
            messagebox.showinfo("Round-1 is over","Computer Is Out")
            win3.destroy()
        else:
            global runs_comp
            runs_comp=runs_comp+x
    def but2():
        x=random.choice(list1)
        val2=2
        if x==2:
            messagebox.showinfo("Round-1 is over","Computer Is Out")
            win3.destroy()
        else:
           global runs_comp
           runs_comp=runs_comp+x
    def but3():
        x=random.choice(list1)
        val3=3
        if x==3:
            messagebox.showinfo("Round-1 is over","Computer Is Out")
            win3.destroy()
        else:
            global runs_comp
            runs_comp=runs_comp+x
    def but4():
        x=random.choice(list1)
        val4=4
        if x==4:
            messagebox.showinfo("Round-1 is over","Computer Is Out")
            win3.destroy()
        else:
            global runs_comp
            runs_comp=runs_comp+x
    def but5():
        x=random.choice(list1)
        val5=5
        if x==5:
            messagebox.showinfo("Round-1 is over","Computer Is Out")
            win3.destroy()
        else:
            global runs_comp
            runs_comp=runs_comp+x

    b1=tkinter.Button(win3,text="1",font=('Arial',30,'bold'),command=but1)
    b1.place(x=100,y=200)
    b2=tkinter.Button(win3,text="2",font=('Arial',30,'bold'),command=but2)
    b2.place(x=235,y=200)
    b3=tkinter.Button(win3,text="3",font=('Arial',30,'bold'),command=but3)
    b3.place(x=370,y=200)
    b4=tkinter.Button(win3,text="4",font=('Arial',30,'bold'),command=but4)
    b4.place(x=505,y=200)
    b5=tkinter.Button(win3,text="5",font=('Arial',30,'bold'),command=but5)
    b5.place(x=640,y=200)

    win3.mainloop()
    #------------------------
    win2=tkinter.Tk()
    win2.geometry("800x500")
    win2.config(bg='black')
    win2.title("Batting")
    label2=tkinter.Label(win2,text="You Are Batting",font=('Arial',40,'bold'),bg='black',fg='green')
    label2.pack()
    def but1():
        x=random.choice(list1)
        val1=1
        if x==1:
            messagebox.showinfo("Round-2 is over","Your are Out")
            win2.destroy()
        else:
            global runs 
            runs=runs+1
            
    def but2():
        x=random.choice(list1)
        val2=2
        if x==2:
            messagebox.showinfo("Round-2 is over","Your are Out")
            win2.destroy()
        else:
            global runs 
            runs=runs+2
    def but3():
        x=random.choice(list1)
        val3=3
        if x==3:
            messagebox.showinfo("Round-2 is over","Your are Out")
            win2.destroy()
        else:
            global runs 
            runs=runs+3
    def but4():
        x=random.choice(list1)
        val4=4
        if x==4:
            messagebox.showinfo("Round-2 is over","Your are Out")
            win2.destroy()
        else:
            global runs 
            runs=runs+4
    def but5():
        x=random.choice(list1)
        val5=5
        if x==5:
            messagebox.showinfo("Round-2 is over","Your are Out")
            win2.destroy()
        else:
            global runs 
            runs=runs+5

    b1=tkinter.Button(win2,text="1",font=('Arial',30,'bold'),command=but1)
    b1.place(x=100,y=200)
    b2=tkinter.Button(win2,text="2",font=('Arial',30,'bold'),command=but2)
    b2.place(x=235,y=200)
    b3=tkinter.Button(win2,text="3",font=('Arial',30,'bold'),command=but3)
    b3.place(x=370,y=200)
    b4=tkinter.Button(win2,text="4",font=('Arial',30,'bold'),command=but4)
    b4.place(x=505,y=200)
    b5=tkinter.Button(win2,text="5",font=('Arial',30,'bold'),command=but5)
    b5.place(x=640,y=200)

    win2.mainloop()

win1=tkinter.Tk()
win1.title("Hand Cricket")
win1.config(bg="black")
win1.geometry("800x500")
label1=tkinter.Label(win1,text="Hand Circket With Computer",font=('Arial',40,'bold'),fg="blue",bg="black")
label1.pack()
button1=tkinter.Button(win1,text="Batting",font=('Arial',40,'bold'),bg='green',command=batting)
button1.place(x=80,y=100)
button2=tkinter.Button(win1,text="Bowling",font=('Arial',40,'bold'),bg='red',command=bowling)
button2.place(x=460,y=100)

tkinter.mainloop()

r1=(runs)
r2=(runs_comp)
if runs>runs_comp:
    messagebox.showinfo("Results",f"""You Won the Match
    
    Your Score {r1}
    
    Compter Score {r2}""")
elif runs_comp>runs:
    messagebox.showinfo("Results",f"""You Lost the Match
       
    Your Score {r1}
    
    Compter Score {r2}""")
else:
    messagebox.showinfo("Results",f"""The Match Is Tie
    
    Your Score {r1}
    
    Compter Score {r2}""")


