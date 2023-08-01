from tkinter import *

# colors: 293241,3d5a80, 98c1d9, e0fbfc

# Window
root = Tk()
root.title("Deterministic PDA")
root.resizable(0, 0)
root.geometry("640x490")
root.config(bg="#3d5a80")

# Frames
leftFrame = Frame(root, bg="#3d5a80")
leftFrame.pack(side="left", ipady=110, padx=(10, 0))
rightFrame = Frame(root, bg="#3d5a80")
rightFrame.pack(side="left", ipady=120, pady=60, ipadx=60)
inputStrFrame = Frame(rightFrame, bg="#98c1d9")
inputStrFrame.pack(side="top", pady=10)
currStFrame = Frame(rightFrame, bg="#98c1d9")
currStFrame.pack(side="top", pady=10)
stepsFrame = Frame(rightFrame, bg="#98c1d9")
stepsFrame.pack(side="top", pady=10)
ctrlsFrame = Frame(rightFrame, bg="#98c1d9")
ctrlsFrame.pack(side="top", pady=10)
entryFrame = Frame(rightFrame, bg="#98c1d9")
entryFrame.pack(side="top", pady=10)

# Machine Program
label = Label(leftFrame, bg="#3d5a80", fg="#e0fbfc", text="Machine Program", font=('Arial', 13), padx=20, pady=10)
label.pack()
scrollbar = Scrollbar(leftFrame, orient='vertical')
scrollbar.pack(side=RIGHT, fill='y', pady=(0, 10))
textbox = Text(leftFrame, font=('Arial', 10), height=27, width=50, yscrollcommand=scrollbar.set)
textbox.pack()

# Given String
label = Label(inputStrFrame, bg="#98c1d9", text="Given String", font=('Arial', 12), pady=2)
label.pack(ipadx=67)
label = Label(inputStrFrame, bg="#e0fbfc", text="10001", font=('Arial', 13), padx=20, pady=1)
label.pack(ipadx=70)

# Current State
label = Label(currStFrame, bg="#98c1d9", text="Current State", font=('Arial', 12), pady=2)
label.pack(ipadx=63)
label = Label(currStFrame, bg="#e0fbfc", text="0", font=('Arial', 13), padx=20, pady=1)
label.pack(ipadx=88)

# Steps
label = Label(stepsFrame, bg="#98c1d9", text="Steps", font=('Arial', 12), pady=2)
label.pack(ipadx=90)
label = Label(stepsFrame, bg="#e0fbfc", text="0", font=('Arial', 13), padx=20, pady=1)
label.pack(ipadx=87)

# Controls
label = Label(ctrlsFrame, bg="#98c1d9", text="Controls", font=('Arial', 12), pady=2)
label.pack(ipadx=80)
run = Button(ctrlsFrame, text="Run", font=('Arial', 9))
run.pack(side="left", ipadx=9)
pause = Button(ctrlsFrame, text="Pause", font=('Arial', 9))
pause.pack(side="left", ipadx=8)
stop = Button(ctrlsFrame, text="Stop", font=('Arial', 9))
stop.pack(side="left", ipadx=8)
reset = Button(ctrlsFrame, text="Reset", font=('Arial', 9))
reset.pack(side="left", ipadx=8)

# Input a String
label = Label(entryFrame, bg="#98c1d9", text="Input a String", font=('Arial', 12), pady=2)
label.pack(ipadx=50)
str = Entry(entryFrame, bd=1, width=32, font=('Arial', 9))
str.pack()

root.mainloop()
