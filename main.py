from tkinter import *
import pygame
from gtts import gTTS
import os

# Create a GUI window
pygame.init()
root = Tk()
root.title("Alphabet_app")
root.geometry('1352x652+0+0')
root.configure(background='white')
 #def Alphabet_H
str1 = StringVar()
str1.set('Welcome To Alphabet App')

ABC = Frame(root, bg='white')
ABC.grid()
#def Alphabet_Home
cont = Canvas(ABC, width=160, height=120, bg="white", )
cont.grid(row=3, column=3)
image1 = PhotoImage(file='icons.png')
image = cont.create_image(300, 175, image=image1)
imgClear = PhotoImage(file='icons.png')

#clear button
def Clear():
    str1.set("Welcome To alphabet App ")
    image = cont.create_image(80, 70, image=imgClear)


#a button
imageA = PhotoImage(file='img/a.png')


def Alphabet_A():
    str1.set("A Is For Apple")
    image = cont.create_image(80, 70, image=imageA)
    tts = gTTS(text="A Is For Apple", lang='en')
    tts.save("Alphabet_A.mp3")
    os.system("Start Alphabet_A.mp3")


#b button
imageB = PhotoImage(file='img/ball.png')


def Alphabet_B():
    str1.set("B Is For Ball")
    image = cont.create_image(80, 70, image=imageB)
    tts = gTTS(text="B Is For Ball", lang='en')
    tts.save("Alphabet_b.mp3")
    os.system("Start Alphabet_b.mp3")

#c button
imageC = PhotoImage(file='img/cherry.png')


def Alphabet_C():
    str1.set("C Is For Cherry")
    image = cont.create_image(80, 70, image=imageC)
    tts = gTTS(text="C Is For Cherry", lang='en')
    tts.save("Alphabet_c.mp3")
    os.system("Start Alphabet_c.mp3")

# d button
imageD = PhotoImage(file='img/d.png')


def Alphabet_D():
    str1.set("D Is For Dog")
    image = cont.create_image(80, 70, image=imageD)
    tts = gTTS(text="D Is For Dog", lang='en')
    tts.save("Alphabet_d.mp3")
    os.system("Start Alphabet_d.mp3")

# e button
imageE = PhotoImage(file='img/eggplant.png')


def Alphabet_E():
    str1.set("E Is For Eggplant")
    image = cont.create_image(80, 70, image=imageE)
    tts = gTTS(text="E Is For Eggplant", lang='en')
    tts.save("Alphabet_e.mp3")
    os.system("Start Alphabet_e.mp3")

# f button
imageF = PhotoImage(file='img/fish.png')


def Alphabet_F():
    str1.set("F Is For Fish")
    image = cont.create_image(80, 70, image=imageF)
    tts = gTTS(text="F Is For Fish", lang='en')
    tts.save("Alphabet_f.mp3")
    os.system("Start Alphabet_f.mp3")



# g button
imageG = PhotoImage(file='img/grape.png')

def Alphabet_G():
        str1.set("G Is For Grape")
        image = cont.create_image(80, 70, image=imageG)
        tts = gTTS(text="G Is For Grape", lang='en')
        tts.save("Alphabet_g.mp3")
        os.system("Start Alphabet_g.mp3")

# h button
imageH = PhotoImage(file='img/horse.png')

def Alphabet_H():
            str1.set("H Is For Horse")
            image = cont.create_image(80, 70, image=imageH)
            tts = gTTS(text="H Is For Horse", lang='en')
            tts.save("Alphabet_h.mp3")
            os.system("Start Alphabet_h.mp3")

# I button
imageI = PhotoImage(file='img/ice.png')


def Alphabet_I():
    str1.set("I Is For Ice")
    image = cont.create_image(80, 70, image=imageI)
    tts = gTTS(text="I Is For Ice", lang='en')
    tts.save("Alphabet_i.mp3")
    os.system("Start Alphabet_i.mp3")


    # J button
imageJ = PhotoImage(file='img/j.png')


def Alphabet_J():
    str1.set("J Is For Jacket")
    image = cont.create_image(80, 70, image=imageJ)
    tts = gTTS(text="J Is For Jacket", lang='en')
    tts.save("Alphabet_j.mp3")
    os.system("Start Alphabet_j.mp3")

# K button
imageK = PhotoImage(file='img/kiwi.png')


def Alphabet_K():
    str1.set("K Is For Kiwi")
    image = cont.create_image(80, 70, image=imageK)
    tts = gTTS(text="K Is For Kiwi", lang='en')
    tts.save("Alphabet_k.mp3")
    os.system("Start Alphabet_k.mp3")

# L button
imageL = PhotoImage(file='img/lime.png')


def Alphabet_L():
    str1.set("L Is For Lime")
    image = cont.create_image(80, 70, image=imageL)
    tts = gTTS(text="L Is For Lime", lang='en')
    tts.save("Alphabet_l.mp3")
    os.system("Start Alphabet_l.mp3")

# M button
imageM = PhotoImage(file='img/monkey.png')


def Alphabet_M():
    str1.set("M Is For Monkey")
    image = cont.create_image(80, 70, image=imageM)
    tts = gTTS(text="M Is For Monkey", lang='en')
    tts.save("Alphabet_m.mp3")
    os.system("Start Alphabet_m.mp3")

# N button
imageN = PhotoImage(file='img/nose.png')


def Alphabet_N():
    str1.set("N Is For Nose")
    image = cont.create_image(80, 70, image=imageN)
    tts = gTTS(text="N Is For Nose", lang='en')
    tts.save("Alphabet_n.mp3")
    os.system("Start Alphabet_n.mp3")
# O button
imageO = PhotoImage(file='img/orange.png')


def Alphabet_O():
    str1.set("O Is For Orange")
    image = cont.create_image(80, 70, image=imageO)
    tts = gTTS(text="O Is For Orange", lang='en')
    tts.save("Alphabet_o.mp3")
    os.system("Start Alphabet_o.mp3")

# P button
imageP = PhotoImage(file='img/pear.png')


def Alphabet_P():
    str1.set("P Is For Pear")
    image = cont.create_image(80, 70, image=imageP)
    tts = gTTS(text="P Is For Pear", lang='en')
    tts.save("Alphabet_p.mp3")
    os.system("Start Alphabet_p.mp3")

# Q button
imageQ = PhotoImage(file='img/queen.png')


def Alphabet_Q():
    str1.set("Q Is For Queen")
    image = cont.create_image(80, 70, image=imageQ)
    tts = gTTS(text="Q Is For Queen", lang='en')
    tts.save("Alphabet_q.mp3")
    os.system("Start Alphabet_q.mp3")

# R button
imageR = PhotoImage(file='img/rabbit.png')


def Alphabet_R():
    str1.set("R Is For Rabbit")
    image = cont.create_image(80, 70, image=imageR)
    tts = gTTS(text="R Is For Rabbit", lang='en')
    tts.save("Alphabet_r.mp3")
    os.system("Start Alphabet_r.mp3")

# S button
imageS = PhotoImage(file='img/str.png')


def Alphabet_S():
    str1.set("S Is For Strawberry")
    image = cont.create_image(80, 70, image=imageS)
    tts = gTTS(text="S Is For Strawberry", lang='en')
    tts.save("Alphabet_s.mp3")
    os.system("Start Alphabet_s.mp3")

# T button
imageT = PhotoImage(file='img/tomato.png')


def Alphabet_T():
    str1.set("T Is For Tomato")
    image = cont.create_image(80, 70, image=imageT)
    tts = gTTS(text="T Is For Tomato", lang='en')
    tts.save("Alphabet_t.mp3")
    os.system("Start Alphabet_t.mp3")

# U button
imageU = PhotoImage(file='img/u.png')


def Alphabet_U():
    str1.set("U Is For Umbrella")
    image = cont.create_image(80, 70, image=imageU)
    tts = gTTS(text="U Is For Umbrella", lang='en')
    tts.save("Alphabet_u.mp3")
    os.system("Start Alphabet_u.mp3")

# V button
imageV = PhotoImage(file='img/v.png')


def Alphabet_V():
    str1.set("V Is For Van")
    image = cont.create_image(80, 70, image=imageV)
    tts = gTTS(text="V Is For Van", lang='en')
    tts.save("Alphabet_v.mp3")
    os.system("Start Alphabet_v.mp3")

# W button
imageW = PhotoImage(file='img/watermelon.png')


def Alphabet_W():
    str1.set("W Is For Watermelon")
    image = cont.create_image(80, 70, image=imageW)
    tts = gTTS(text="W Is For Watermelon", lang='en')
    tts.save("Alphabet_w.mp3")
    os.system("Start Alphabet_w.mp3")

# X button
imageX = PhotoImage(file='img/x.png')


def Alphabet_X():
    str1.set("X Is For X-Ray")
    image = cont.create_image(80, 70, image=imageX)
    tts = gTTS(text="X Is For X-Ray", lang='en')
    tts.save("Alphabet_x.mp3")
    os.system("Start Alphabet_x.mp3")

# Y button
imageY = PhotoImage(file='img/yellow.png')


def Alphabet_Y():
    str1.set("Y Is For Yellow")
    image = cont.create_image(80, 70, image=imageY)
    tts = gTTS(text="Y Is For Yellow", lang='en')
    tts.save("Alphabet_y.mp3")
    os.system("Start Alphabet_y.mp3")

# Z button
imageZ = PhotoImage(file='img/zoo.png')


def Alphabet_Z():
    str1.set("Z Is For Zoo")
    image = cont.create_image(80, 70, image=imageZ)
    tts = gTTS(text="Z Is For Zoo", lang='en')
    tts.save("Alphabet_z.mp3")
    os.system("Start Alphabet_z.mp3")

# row 0
txtDisplay = Entry(ABC, textvariable=str1, font=('arial', 44, 'bold'), bg="powder blue", bd=34, width=39,
                   justify=CENTER)
txtDisplay.grid(row=0, column=0, columnspan=7, pady=1)
# row 1
btnA = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="A", bg="CornSilk",
              command=Alphabet_A).grid(row=1, column=0)
btnB = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="B", bg="powder blue",
              command=Alphabet_B).grid(row=1,
                                       column=1)
btnC = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="C", bg="powder blue",
              command=Alphabet_C).grid(row=1,
                                       column=2)
btnD = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="D", bg="powder blue",
              command=Alphabet_D).grid(row=1,
                                       column=3)
btnE = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="E", bg="powder blue",
              command=Alphabet_E).grid(row=1,
                                       column=4)
btnF = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="F", bg="powder blue",command=Alphabet_F).grid(row=1,
                                                                                                                  column=5)
btnG = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="G", bg="powder blue",command=Alphabet_G).grid(row=1,
                                                                                                                  column=6)
# row 2
btnH = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="H", bg="CornSilk",command=Alphabet_H).grid(row=2,
                                                                                                               column=0)
btnI = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="I", bg="powder blue",command=Alphabet_I).grid(row=2,
                                                                                                                  column=1)
btnJ = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="J", bg="powder blue",command=Alphabet_J).grid(row=2,
                                                                                                                  column=2)
btnK = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="K", bg="powder blue",command=Alphabet_K).grid(row=2,
                                                                                                                  column=3)
btnL = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="L", bg="powder blue",command=Alphabet_L).grid(row=2,
                                                                                                                  column=4)
btnM = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="M", bg="powder blue",command=Alphabet_M).grid(row=2,
                                                                                                                  column=5)
btnN = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="N", bg="powder blue",command=Alphabet_N).grid(row=2,
                                                                                                                  column=6)
# row 3
btnO = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="O", bg="CornSilk",command=Alphabet_O).grid(row=3,
                                                                                                               column=0)
btnP = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="P", bg="powder blue",command=Alphabet_P).grid(row=3,
                                                                                                                  column=1)
btnQ = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Q", bg="powder blue",command=Alphabet_Q).grid(row=3,
                                                                                                                  column=2)
btnR = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="R", bg="powder blue",command=Alphabet_R).grid(row=3,
                                                                                                                  column=4)
btnS = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="S", bg="powder blue",command=Alphabet_S).grid(row=3,
                                                                                                                  column=5)
btnT = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="T", bg="powder blue",command=Alphabet_T).grid(row=3,
                                                                                                                  column=6)

# row 4
btnU = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="U", bg="powder blue",command=Alphabet_U).grid(row=4,
                                                                                                                  column=0)
btnV = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="V", bg="CornSilk",command=Alphabet_V).grid(row=4,
                                                                                                               column=1)
btnW = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="W", bg="powder blue",command=Alphabet_W).grid(row=4,
                                                                                                                  column=2)
btnX = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="X", bg="powder blue",command=Alphabet_X).grid(row=4,
                                                                                                                  column=3)
btnY = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Y", bg="powder blue",command=Alphabet_Y).grid(row=4,
                                                                                                                  column=4)
btnZ = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Z", bg="powder blue",command=Alphabet_Z).grid(row=4,
                                                                                                                  column=5)
btnClear = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Clear", bg="powder blue",
                  command=Clear).grid(row=4, column=6)

root.mainloop()
