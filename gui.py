from tkinter import *
from classes import State, Machine


# colors: 293241,3d5a80, 98c1d9, e0fbfc

class GUI:
    def __init__(self):
        # Window
        self.root = Tk()
        self.root.title("Deterministic PDA")
        self.root.resizable(0, 0)
        self.root.geometry("640x490")
        self.root.config(bg="#3d5a80")

        # Frames
        self.leftFrame = Frame(self.root, bg="#3d5a80")
        self.leftFrame.pack(side="left", ipady=110, padx=(10, 0))
        self.rightFrame = Frame(self.root, bg="#3d5a80")
        self.rightFrame.pack(side="left", ipady=120, pady=60, ipadx=60)
        self.inputStrFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.inputStrFrame.pack(side="top", pady=10)
        self.currStFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.currStFrame.pack(side="top", pady=10)
        self.stepsFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.stepsFrame.pack(side="top", pady=10)
        self.ctrlsFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.ctrlsFrame.pack(side="top", pady=10)
        self.entryFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.entryFrame.pack(side="top", pady=10)

        # Machine Program
        self.label = Label(self.leftFrame, bg="#3d5a80", fg="#e0fbfc", text="Machine Program", font=('Arial', 13),
                           padx=20, pady=10)
        self.label.pack()
        self.scrollbar = Scrollbar(self.leftFrame, orient='vertical')
        self.scrollbar.pack(side=RIGHT, fill='y', pady=(0, 10))
        self.machineprog = Text(self.leftFrame, font=('Arial', 10), height=27, width=50,
                                yscrollcommand=self.scrollbar.set)
        self.machineprog.pack()

        # Given String
        self.label = Label(self.inputStrFrame, bg="#98c1d9", text="Given String", font=('Arial', 12), pady=2)
        self.label.pack(ipadx=67)
        self.label = Label(self.inputStrFrame, bg="#e0fbfc", text="10001", font=('Arial', 13), padx=20, pady=1)
        self.label.pack(ipadx=70)

        # Current State
        self.label = Label(self.currStFrame, bg="#98c1d9", text="Current State", font=('Arial', 12), pady=2)
        self.label.pack(ipadx=63)
        self.label = Label(self.currStFrame, bg="#e0fbfc", text="0", font=('Arial', 13), padx=20, pady=1)
        self.label.pack(ipadx=88)

        # Steps
        self.label = Label(self.stepsFrame, bg="#98c1d9", text="Steps", font=('Arial', 12), pady=2)
        self.label.pack(ipadx=90)
        self.label = Label(self.stepsFrame, bg="#e0fbfc", text="0", font=('Arial', 13), padx=20, pady=1)
        self.label.pack(ipadx=87)

        # Controls
        self.label = Label(self.ctrlsFrame, bg="#98c1d9", text="Controls", font=('Arial', 12), pady=2)
        self.label.pack(ipadx=80)
        self.run = Button(self.ctrlsFrame, text="Run", font=('Arial', 9), command=self.frun)
        self.run.pack(side="left", ipadx=9)
        self.pause = Button(self.ctrlsFrame, text="Pause", font=('Arial', 9), command=self.fpause)
        self.pause.pack(side="left", ipadx=8)
        self.step = Button(self.ctrlsFrame, text="Step", font=('Arial', 9), command=self.fstep)
        self.step.pack(side="left", ipadx=8)
        self.reset = Button(self.ctrlsFrame, text="Reset", font=('Arial', 9), command=self.freset)
        self.reset.pack(side="left", ipadx=8)

        # Input a String
        self.label = Label(self.entryFrame, bg="#98c1d9", text="Input a String", font=('Arial', 12), pady=2)
        self.label.pack(ipadx=50)
        self.input_str = Entry(self.entryFrame, bd=1, width=32, font=('Arial', 9))
        self.input_str.pack()

        self.root.mainloop()

    def fread(self):
        text_content = self.machineprog.get("1.0", END).strip()
        lines = text_content.split('\n')

        tuples_list = []

        # <current state> <current symbol> <new symbol> <direction> <new state>
        for line in lines:
            if line.startswith(';') or not line.strip():
                continue

            if ';' in line:
                line = line.split(';', 1)[0]

            tuple_items = tuple(line.split())
            tuples_list.append(tuple_items)

        return tuples_list

    def frun(self):
        # dpda = Machine()
        print("running")
            #
            # # run.config(state=DISABLED)
            # transitions_list = fread()
            #
            # for transition in transitions_list:
            #     curr_state, curr_symbol, input_symbol, direction, new_state = transition
            # #     dpda.add_transition(curr_state, curr_symbol, input_symbol, direction, new_state)
            # #
            # # dpda.print_transitions()
            #
            # input_string = input_str.get()
            #
            # result = dpda.run(input_string)
            #
            # print("Result:", result)

    def fpause(self):
        print("pausing")

    def fstep(self):
        print("stepping")

    def freset(self):
        print("resetting")



GUI()

