from customtkinter import *
import time  

root = CTk()
root.geometry('400x300')
root.title("Countdowm Timer ")
paused = False
remaining_time = 0

def start_countdown():
    global remaining_time , count_lab ,pause_but
    label.destroy()
    time_ent.destroy()
    submit_but.destroy()
    #count_lab.destroy()
    #pause_but.destroy()
    remaining_time = int(time_var.get())

    if remaining_time <= 0:
        raise ValueError("Countdown time must be greater than 0.")

    count_lab = CTkLabel(root,text=" ",font=('Arieal',50,'bold'))
    count_lab.place(x=140,y=100)

    pause_but = CTkButton(root,text="Pause",font=('Arieal',15,'bold'),command=pause_countdown)
    pause_but.place(x=130,y=200)

    countdown(remaining_time)

def countdown(time_sec):
    global paused, remaining_time
    if paused:
        root.after(1000, countdown, remaining_time)
        return

    if time_sec <= 0:
        count_lab.configure(text="Time's up!")
        count_lab.place(x=100,y=120)

        return

    count_lab.configure(text=f"{time_sec // 60:02d}:{time_sec % 60:02d}")
    remaining_time = time_sec
    root.after(1000, countdown, time_sec - 1)

def pause_countdown():
    count_lab.configure(text_color='red')
    global paused
    paused = True
    pause_but.configure(text="Resume",command=resume)

def resume():
    count_lab.configure(text_color="white")
    global paused
    pause_but.configure(text="Pause",command=pause_countdown)
    paused = False
    countdown(remaining_time)

time_var = StringVar()
time_var.set('')

header = CTkLabel(root,text="Countdown Timer ",font=('Arieal',20,'bold','underline'))
header.place(x=130,y=10)

label = CTkLabel(root,text="Enter The Time Value In Seconds : ",font=('Arieal',15,'bold'))
label.place(x=80,y=70)

time_ent = CTkEntry(root,textvariable=time_var,width=190)
time_ent.place(x=115,y=120)

submit_but = CTkButton(root,text="Submit",font=('Arieal',15,'bold'),command=start_countdown)
submit_but.place(x=130,y=200)

root.mainloop() 