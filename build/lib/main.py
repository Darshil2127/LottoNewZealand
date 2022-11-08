#widgets:
import random
from tkinter import *
window = Tk()
img = PhotoImage(file="lotto.png")

imgLabel1 = Label(window, image= img, width=200, height=200)

label1 = Label(window, relief="ridge", width=4)
label2 = Label(window, relief="ridge", width=4)
label3 = Label(window, relief="ridge", width=4)
label4 = Label(window, relief="ridge", width=4)
label5 = Label(window, relief="ridge", width=4)
label6 = Label(window, relief="ridge", width=4)
getBtn = Button(window)
retBtn = Button(window)

imgLabel1.grid(row=1, column=1, rowspan=2)
label1.grid(row=1, column=2, padx=10)
label2.grid(row=1, column=3, padx=10)
label3.grid(row=1, column=4, padx=10)
label4.grid(row=1, column=5, padx=10)
label5.grid(row=1, column=6, padx=10)
label6.grid(row=1, column=7, padx=(10,20))
getBtn.grid(row=2, column=2, columnspan=4)
retBtn.grid(row=2, column=6,columnspan=2)

#Static Properties
window.title("Lotto Number Picker")
window.resizable(0,0) #disable window's resize button
getBtn.configure(text="Get My Lucky Number")
retBtn.configure(text="Reset")

#initial properties
label1.configure(text="...")
label2.configure(text="...")
label3.configure(text="...")
label4.configure(text="...")
label5.configure(text="...")
label6.configure(text="...")
retBtn.configure(state=DISABLED)

#Dynamic Properties
from random import  sample

def pick():
    nums = sample(range(1,40),6)
    label1.configure(text= nums[0])
    label2.configure(text=nums[1])
    label3.configure(text=nums[2])
    label4.configure(text=nums[3])
    label5.configure(text=nums[4])
    label6.configure(text=nums[5])
    getBtn.configure(state=DISABLED)
    retBtn.configure(state=NORMAL)

def reset():
    label1.configure(text="...")
    label2.configure(text="...")
    label3.configure(text="...")
    label4.configure(text="...")
    label5.configure(text="...")
    label6.configure(text="...")
    getBtn.configure(state= NORMAL)
    retBtn.configure(state=DISABLED)

getBtn.configure(command=pick)
retBtn.configure(command=reset)

window.mainloop()

