import tkinter
from tkinter import *


windows= Tk()
windows.geometry("800x600")

def calculate():

    Samosa=e1.get()   
    if (len(Samosa))>0 :
        Samosa=Samosa
     
    else:
        Samosa=0
       

    jaelibi=e2.get()  
    if (len(jaelibi))>0 :
        jaelibi=jaelibi
     
    else:
        jaelibi=0

    fafra=e3.get() 
    if (len(fafra))>0 :
        fafra=fafra
     
    else:
        fafra=0

    chat=e4.get()  
    if (len(chat))>0 :
        chat=chat
     
    else:
        chat=0


    total=((int(Samosa)*15)+(int(jaelibi)*10)+(int(fafra)*50)+(int(chat)*40))
    label12=Label(windows,text=total,font="times 18")
    label12.place(x=100,y=360)



label1=Label(windows,text="AB Star Street Food",font="times 30 bold")
label1.place(x=300,y=30,anchor="center")

# ----------menu section------------

label=Label(windows,text="--MENU--",font="times 28 bold")
label.place(x=550,y=70)

label2=Label(windows,text="Samosa       Rs 15",font="times 18")
label2.place(x=450,y=120)

label3=Label(windows,text="Jaelibi     Rs 10",font="times 18 ")
label3.place(x=450,y=150)

label4=Label(windows,text="Fafra       Rs 50",font="times 18 ")
label4.place(x=450,y=180)

label5=Label(windows,text="chat         Rs 40",font="times 18")
label5.place(x=450,y=210)

#-------BILLING SECTION------

label6=Label(windows,text="Select the items",font="times 19 bold")
label6.place(x=70,y=70)

label7=Label(windows,text="samosa",font="times 19 ")
label7.place(x=20,y=120)
e1=Entry(windows)
e1.place(x=20,y=150)

label8=Label(windows,text="jaelibi",font="times 19")
label8.place(x=250,y=120)
e2=Entry(windows)
e2.place(x=250,y=150)

label9=Label(windows,text="Fafra",font="times 19")
label9.place(x=20,y=200)
e3=Entry(windows)
e3.place(x=20,y=230)

label10=Label(windows,text="chat",font="times 19")
label10.place(x=250,y=200)
e4=Entry(windows)
e4.place(x=250,y=230)


b2=Button(windows,text='bill',width=20,command=calculate)
b2.place(x=100,y=300)

windows.mainloop()


#-------RECEIPT-------