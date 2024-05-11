import random 
from tkinter import *
from tkinter.messagebox import askyesno
from tkinter import messagebox

root = Tk()
root.geometry('800x700')
root.resizable(False,False)
root.title("Rock Paper Sciccor Game")
root.configure(bg='Black')

comp_op = ('ROCK','PAPER',"SCICCORS")
user_var = StringVar()
comp_var = StringVar()
winner_var = StringVar()
uscore_var = IntVar()
cscore_var = IntVar()

global user_score ,comp_score
user_score = 0
comp_score = 0

def winner():
    global user_score ,comp_score

    if user_var.get() == comp_var.get():
        print("Tie !!!")
        winner_var.set('Tie !!!!')

    elif (user_var.get() == 'ROCK' and  comp_var.get() == 'SCICCORS') or \
        (user_var.get() == 'PAPER' and comp_var.get() == 'ROCK') or \
        (user_var.get() == 'SCICCORS' and comp_var.get() == 'PAPER'):
            print("user winner")
            winner_var.set('User Win !!!!')    
            user_score += 10
            uscore_var.set(user_score)

    else:
        print("Computer Win !!!")
        winner_var.set('Computer Win !!!!')
        comp_score += 10
        cscore_var.set(comp_score)

    if comp_score == 100 or user_score == 100:
        if comp_score == user_score:
            messagebox.showinfo('RESULT',"MATCH IS TIE !!!!!")
        elif user_score > comp_score:
            messagebox.showinfo('RESULT',"USER WIN MATCH !!!!!")
        else:
            messagebox.showinfo('RESULT',"COMPUTER WIN MATCH !!!!!")
        



def rock_choice():
    user_var.set('ROCK')
    comp_choice = random.choice(comp_op)
    comp_var.set(comp_choice)
    rock_but.configure(bg="red")
    rock_but.configure(state='disabled')
    paper_but.configure(state='disabled')
    sciccors_but.configure(state='disabled')
    winner()


def paper_choice():
    user_var.set('PAPER')
    comp_choice = random.choice(comp_op)
    comp_var.set(comp_choice)
    paper_but.configure(bg="red")
    paper_but.configure(state='disabled')
    rock_but.configure(state='disabled')
    sciccors_but.configure(state='disabled')
    winner()

def sciccors_choice():
    user_var.set('SCICCORS')
    comp_choice = random.choice(comp_op)
    comp_var.set(comp_choice)
    sciccors_but.configure(bg="red")
    sciccors_but.configure(state='disabled')
    rock_but.configure(state='disabled')
    paper_but.configure(state='disabled')
    winner()

def nextround():
    rock_but.configure(state='active',bg="white",fg="black")
    paper_but.configure(state='active',bg="white",fg="black")
    sciccors_but.configure(state='active',bg="white",fg="black")

    user_var.set('')
    comp_var.set('')
    winner_var.set('')

def Exit():
    exit_game = askyesno(title='confirmation',message='Are you sure that you want to quit game?')

    if exit_game:
        root.destroy()

def restart():
    global user_score ,comp_score
    rock_but.configure(state='active',bg="white",fg="black")
    paper_but.configure(state='active',bg="white",fg="black")
    sciccors_but.configure(state='active',bg="white",fg="black")

    user_var.set('')
    comp_var.set('')
    winner_var.set('')
    user_score = 0
    comp_score = 0 
    uscore_var.set(user_score)
    cscore_var.set(comp_score)

def gameloop():
    root.configure(bg="#A9B388")
    head.destroy()
    instruction.destroy()
    inst_lab.destroy()
    rules.destroy()
    rul_lab.destroy()
    next.destroy()
    note.destroy()
    note_lab.destroy()

    global rock_but,paper_but,sciccors_but

    heading = Label(root,text= "WELCOME TO ROCK PAPER SCICCOR GAME ",font="Arieal 20 italic bold underline",bg="#A9B388")
    heading.place(x=120,y=10)

    choice = Label(root,text="Choice Any One : ",font="Arieal 20 bold",bg='#B2C8BA')
    choice.place(x=50,y=100)

    rock_but = Button(root,text = "ROCK",font="Arieal 16 bold",command=rock_choice,bg='#EEF5FF')
    rock_but.place(x=320,y=100)

    paper_but = Button(root,text = "PAPER",font="Arieal 16 bold",command=paper_choice,bg='#EEF5FF')
    paper_but.place(x=430,y=100)

    sciccors_but = Button(root,text = "SCICCORS",font="Arieal 16 bold",command=sciccors_choice,bg='#EEF5FF')
    sciccors_but.place(x=550,y=100)

    user_lab = Label(root,text="User Choice ",font="Arieal 16 bold",bg='#B99470',width=15)
    user_lab.place(x=100,y=190)

    computer_lab = Label(root,text="Computer Choice ",font="Arieal 16 bold",bg='#B99470',width=15)
    computer_lab.place(x=450,y=190)

    user_ent = Entry(root,textvariable=user_var,font="Arieal 18 bold",state="disabled",width=10)
    user_ent.place(x=125,y=250,height=30)

    comp_ent = Entry(root,textvariable=comp_var,font="Arieal 18 bold",state="disabled",width=10)
    comp_ent.place(x=490,y=250,height=30)

    score_lab = Label(root,text="SCORE : ",font="Arieal 16 bold",bg='#A9B388')
    score_lab.place(x=10,y=360)

    uscore_ent = Entry(root,textvariable=uscore_var,font="Arieal 18 bold",state="disabled",width=10)
    uscore_ent.place(x=130,y=360)

    cscore_ent = Entry(root,textvariable=cscore_var,font="Arieal 18 bold",state="disabled",width=10)
    cscore_ent.place(x=530,y=360)

    winner_lab = Label(root,text="WINNER",font="arieal 16 bold",bg="#F4CE14")
    winner_lab.place(x=340,y=440)

    winner_res = Entry(root,textvariable = winner_var,state="disabled",font="Arieal 18 bold",width=17)
    winner_res.place(x=280,y=480,height=30)

    round_but = Button(root,text="Next Round",font="Arieal 16 bold",command=nextround)
    round_but.place(x=340,y=540)

    exit_but = Button(root,text="EXIT",font="Arieal 16 bold",command=Exit)
    exit_but.place(x=530,y=590)
        
    restart_but = Button(root,text="RESTART",font="Arieal 16 bold",command=restart)
    restart_but.place(x=150,y=590)  

head = Label(root,text= "WELCOME TO ROCK PAPER SCICCOR GAME ",font="Arieal 20 bold",bg="orange")
#head.place(x=120,y=10)
head.pack(fill=X,pady=5)

instruction = Label(root,text="INSTRUCTION :",font='arieal 15 bold')
instruction.place(x=10,y=80)

inst_lab = Label(root,text="\n1. Choose your move: At the start of each round, you will be prompted to choose your move between Rock, Paper, or Scissors. You can make your selection by clicking the name of your move in the window .\n\n2. Computer move: After you have made your selection, the computer will make its move. The result of the round will then be displayed on the screen .\n\n3. Repeat: The game continues for multiple rounds, and you can choose a different move each time if you wish if not then click same button. The player with the most wins at the end of the game is the winner.",wraplength=750,bg="black",fg="white",font='CourierNew 15')
inst_lab.place(x=30,y=110)

rules = Label(root,text="RULES :",font='arieal 15 bold')
rules.place(x=10,y=385)

rul_lab = Label(root,text="1. Rock beats Scissors\n\n2.Scissors beats Paper\n\n3. Paper beats Rock.",bg="black",fg="white",font='5')
rul_lab.place(x=50,y=435)

note = Label(root,text="NOTE :",font='arieal 15 bold')
note.place(x=10,y=570)

note_lab = Label(root,text="The first player to reach a total of 100 ,will be the winner of the game.",bg="black",fg="white",font='5')
note_lab.place(x=30,y=630,anchor='w')

next = Button(root,text="NEXT ->",font="Arieal 16 bold",command=gameloop,fg="blue")
next.place(x=660,y=640)


root.mainloop()