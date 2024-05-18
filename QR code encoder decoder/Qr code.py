# import qrcode
# from customtkinter import *
# #from tkinter import messagebox as msg
# from PIL import Image,ImageTk
# import re
# import cv2

# '''
# read = cv2.imread('go.png')
# detector = cv2.QRCodeDetector()
# v1,v2,v3 = detector.detectAndDecode(read)
# print(v1)
# '''
# root = CTk()
# root.geometry('700x700')
# root.title("QR Code Encoder Decoder ")
# root.configure(bg="aqua")

# gen_var = StringVar()
# qrname_var = StringVar()
# read_var = StringVar()

# global img_ref
# img_ref = None

# def encode():
#     choice_lab.destroy()
#     encode_but.destroy()
#     decode_but.destroy()
#     root.configure(bg="black")
#     global gen_lab,gen_ent,save_but

#     gen_lab = CTkLabel(root,text="Enter Text Or link : ",font=("arieal", 20 ,"bold"))
#     gen_lab.place(x=200,y=150)

#     gen_ent = CTkEntry(root,textvariable=gen_var,width=270)
#     gen_ent.place(x=200,y=230)

#     save_but = CTkButton(root,text="Save QrCode ",font=("arieal", 20 ,"bold"),command=save_Qr)
#     save_but.place(x=260,y=350)

# def generate_qr():
#     win = CTk()
#     #a = input("enter file Name : ")
#     #img = CTkImage(light_image=Image.open("demo3.png"),size=(100,100))
#     image = Image.open("demo3.png")
#     img = ImageTk.PhotoImage(image)
#     label = CTkLabel(win,text=" ",image=img)
#     label.pack()
#     win.mainloop()


# def save_Qr():
#     gen_lab.configure(text="Enter Name to Save Qr Image (.PNG) : ",font=("areial",13 ,'italic',"underline"))
#     gen_ent.configure(textvariable=qrname_var)
#     gen_ent.place(x=200,y=200)

#     if gen_var.get() == ' ':
#         pass
#         #msg.showerror('Error','Invalid Text !!!!')
#     else:
#         print(gen_var.get())
#         img = qrcode.make(gen_var.get())
        
#         if qrname_var.get() == ' ':
#             pass
#         else:
#             check = re.search('.png$',qrname_var.get())
#             if check:
#                 #img.save(qrname_var.get())
#                 save_but.configure(text="GENERATE QRCode ",command=generate_qr)
                
                
#             else:
#                 print('Noooooooooooo')




# def decode():
#     '''
#     choice_lab.destroy()
#     encode_but.destroy()
#     decode_but.destroy()'''
#     pass


# header = CTkLabel(root,text="QR Code ",font=("arieal", 20 ,"bold","italic","underline"),text_color="aqua")
# header.pack()

# choice_lab = CTkLabel(root,text="Click The Button You Want : ",font=("arieal", 20 ,"bold"),text_color="aqua")
# choice_lab.place(x=170,y=150)

# encode_but = CTkButton(root,text="Encode",font=("arieal", 20 ,"bold"),command=encode)
# encode_but.place(x=150,y=250)

# decode_but = CTkButton(root,text="Decode",font=("arieal", 20 ,"bold"),command=decode)
# decode_but.place(x=430,y=250)


# root.mainloop()

from customtkinter import *
from tkinter import messagebox as msg 
from tkinter.messagebox import askyesno
import qrcode
import cv2
from PIL import Image
import re

root = CTk()
root.geometry("600x600")

def submit_qr():
    ent_lab.configure(state='disabled')
    global img_name
    diag = CTkInputDialog(text="Enter File name To Save(.PNG)",title="Save")
    img_name = diag.get_input()
    if img_name:
        qr_img = qrcode.make(qrname_var.get())
        print(img_name)
        if img_name == ' ':
            msg.showerror("Error","Enter Valid Text ")
        else:
            check = re.search('.png$',img_name)
            if check:
                #qr_img.save(img_name)
                msg.showinfo("Message","Image Saved Sucessfully !!!")

        sub_but.configure(text="Generate QR ",command=generate_qr)
    else:
        msg.showerror("Error","Enter Valid Text ")

def encode():
    label.destroy()
    encode_but.destroy()
    decode_but.destroy()
    qrname_var.set("")
    sub_but.configure(text="Submit",command=submit_qr)

def dir_decode():
    ent_lab.destroy()
    qr_ent.destroy()
    sub_but.destroy()
    di_decode_but.destroy()

    
    global decode_lab,decode_ent_lab,decode_qr_ent,decode_sub_but

    decode_lab = CTkLabel(root,text="Decode",font=("timer",30,"bold","underline"))
    decode_lab.place(x=245,y=20)

    decode_ent_lab = CTkLabel(root,text="Enter Img Name To Decode (.PNG) : ",font=("timer",20,"bold","underline"))
    decode_ent_lab.place(x=160,y=120)

    global decode_img_var
    decode_img_var = StringVar()

    decode_qr_ent = CTkEntry(root,textvariable=decode_img_var,width=270)
    decode_qr_ent.place(x=180,y=170)

    decode_sub_but = CTkButton(root,text="Decode",font=("timer",20),command=decode_text)
    decode_sub_but.place(x=230,y=220)

def decode():
    encode_lab.destroy()
    ent_lab.destroy()
    qr_ent.destroy()
    sub_but.destroy()
    encode_but.destroy()
    decode_but.destroy()
    di_decode_but.destroy()
    label.destroy()

    
    global decode_lab,decode_ent_lab,decode_qr_ent,decode_sub_but

    decode_lab = CTkLabel(root,text="Decode",font=("timer",30,"bold","underline"))
    decode_lab.place(x=245,y=20)

    decode_ent_lab = CTkLabel(root,text="Enter Img Name To Decode (.PNG) : ",font=("timer",20,"bold","underline"))
    decode_ent_lab.place(x=160,y=120)

    global decode_img_var
    decode_img_var = StringVar()

    decode_qr_ent = CTkEntry(root,textvariable=decode_img_var,width=270)
    decode_qr_ent.place(x=180,y=170)

    decode_sub_but = CTkButton(root,text="Decode",font=("timer",20),command=decode_text)
    decode_sub_but.place(x=230,y=220)

def decode_text():
    global text_show_lab,text_show,de_encode_but,exit_but
    if decode_img_var.get() == ' ':
        msg.showerror("Error","Enter Valid Text ")
    else:
        check = re.search('.png$',decode_img_var.get())
        if check:
            show_text = cv2.imread(decode_img_var.get())
            detector = cv2.QRCodeDetector()
            v1,v2,v3 = detector.detectAndDecode(show_text)

            text_show_lab = CTkLabel(root,text="Decode Text Is : ",font=("timer",30,"bold","underline"))
            text_show_lab.place(x=180,y=320)

            decoded_var = StringVar()
            text_show = CTkEntry(root,textvariable=decoded_var,width=400,height=20,state='disabled',font=("timer",20))
            text_show.place(x=130,y=370)
            decoded_var.set(v1)

            exit_but = CTkButton(root,text="Exit",font=("timer",20),command=Exit)
            exit_but.place(x=200,y=500)

        else:
            msg.showerror("Error","Enter Valid Text ")   

def Exit():
    exit_game = askyesno(title='confirmation',message='Are you sure that you want to quit game?')

    if exit_game:
        root.destroy()


def generate_qr():
    global label,encode_but,decode_but

    img = CTkImage(light_image=Image.open(f"{img_name}"),size=(200,200))
    label = CTkLabel(root,text=" ",image=img)
    label.place(x=200,y=300)

    encode_but = CTkButton(root,text="Encode",font=("timer",20),command=encode)
    encode_but.place(x=130,y=500)

    decode_but = CTkButton(root,text="Decode",font=("timer",20),command=decode)
    decode_but.place(x=330,y=500)

encode_lab = CTkLabel(root,text="Encode",font=("timer",30,"bold","underline"))
encode_lab.place(x=245,y=20)

ent_lab = CTkLabel(root,text="Enter Text Or Link : ",font=("timer",20,"bold","underline"))
ent_lab.place(x=180,y=120)

qrname_var = StringVar()

qr_ent = CTkEntry(root,textvariable=qrname_var,width=270)
qr_ent.place(x=180,y=170)

sub_but = CTkButton(root,text="Submit",font=("timer",20),command=submit_qr)
sub_but.place(x=230,y=220)

di_decode_but = CTkButton(root,text="Decode",font=("timer",20),command=dir_decode)
di_decode_but.place(x=230,y=500)

root.mainloop()

