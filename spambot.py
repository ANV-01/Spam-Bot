import pyautogui, time
from tkinter import *

def backbone():
    time.sleep(3)
    for _ in iter(int,1):
        word = spamtext.get()
        thetime = int(spamtime.get())
        time.sleep(thetime)
        pyautogui.typewrite(word)
        pyautogui.press("Enter")

spam = Tk()
spam.title("Spam Bot - Close application to stop")
spam.geometry("400x135")

first = Label(spam, text="Enter the text you would like to be spammed")
first.pack()

spamtext = Entry(spam,font=1)
spamtext.pack()

second = Label(spam, text="Set the delay between message sent (message per second)")
second.pack()

spamtime = Entry(spam)
spamtime.pack()

enter = Button(spam, text="Spam!", command=backbone)
enter.pack()

spam.mainloop()

