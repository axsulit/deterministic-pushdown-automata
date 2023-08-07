from tkinter import *
from classes import State, Machine
from utilities import get_machine

# Get list of states as defined by the given machine
states_list = get_machine("sample.txt")
print(states_list)

# Convert state list to state objects
states_obj_list = [State(s) for s in states_list]

# Create DPDA Machine
dpda = Machine(states_obj_list)

steps = 0
curr_state = set()

# colors: 293241,3d5a80, 98c1d9, e0fbfc

err = False
input_string = ""
str_len_edge = len(input_string) - 1
index = 0
steps = 0


class GUI:
    def __init__(self):
        # Window
        self.root = Tk()
        self.root.title("Deterministic PDA")
        self.root.resizable(0, 0)
        self.root.geometry("1000x520")
        self.root.config(bg="#3d5a80")

        # Frames
        self.leftFrame = Frame(self.root, bg="#3d5a80")
        self.leftFrame.pack(side="left", ipady=120, padx=(40, 0))
        self.programFrame = Frame(self.leftFrame, bg="#98c1d9")
        self.programFrame.pack(side="left", ipadx=5, pady=(5, 5))
        self.programDefFrame = Frame(self.programFrame, bg="#98c1d9")
        self.programDefFrame.pack(side="bottom", pady=(0, 5))
        self.rightFrame = Frame(self.root, bg="#3d5a80")
        self.rightFrame.pack(side="left", ipady=120, pady=60, ipadx=60)
        self.entryFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.entryFrame.pack(side="top", pady=10)
        self.ctrlsFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.ctrlsFrame.pack(side="top", pady=10)
        self.inputStrFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.inputStrFrame.pack(side="top", pady=10)
        self.currStFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.currStFrame.pack(side="top", pady=10)
        self.stepsFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.stepsFrame.pack(side="top", pady=10)

        # Machine Program
        self.label = Label(self.programFrame, bg="#98c1d9", text="Machine Program", font=('Arial', 13),
                           padx=20, pady=6)
        self.label.pack()
        self.scrollbar = Scrollbar(self.programDefFrame, orient='vertical')
        self.scrollbar.pack(side=RIGHT, fill='y', pady=0)
        self.machineprog = Text(self.programDefFrame, font=('Fixedsys', 10), height=27, width=75,
                                yscrollcommand=self.scrollbar.set)
        self.machineprog.pack()

        # Input a String
        self.label = Label(self.entryFrame, bg="#98c1d9", text="Input a String", font=('Arial', 12), pady=2)
        self.label.pack(ipadx=50)
        self.input_str = Entry(self.entryFrame, bd=1, width=32, font=('Arial', 9))
        self.input_str.pack()

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

        # Given String
        self.label = Label(self.inputStrFrame, bg="#98c1d9", text="Given String", font=('Arial', 12), pady=2)
        self.label.pack(ipadx=67)
        self.label = Label(self.inputStrFrame, bg="#e0fbfc", text="10001", font=('Arial', 13), padx=20, pady=1)
        self.label.pack(ipadx=70)

        # Current State
        self.currstatelbl = Label(self.currStFrame, bg="#98c1d9", text="Current State", font=('Arial', 12), pady=2)
        self.currstatelbl.pack(ipadx=63)
        self.currstateval = Label(self.currStFrame, bg="#e0fbfc", text="0", font=('Arial', 13), padx=20, pady=1)
        self.currstateval.pack(ipadx=88)

        # Steps
        self.stepslbl = Label(self.stepsFrame, bg="#98c1d9", text="Steps", font=('Arial', 12), pady=2)
        self.stepslbl.pack(ipadx=90)
        self.stepsval = Label(self.stepsFrame, bg="#e0fbfc", text="0", font=('Arial', 13), padx=20, pady=1)
        self.stepsval.pack(ipadx=87)

        self.root.mainloop()

    def frun(self):
        print("running")

        self.step.config(state=DISABLED)
        self.run.config(state=DISABLED)
        self.reset.config(state=DISABLED)
        self.input_str.config(state=DISABLED)

        global input_string, str_len_edge, index, steps, err, curr_state

        input_string = self.input_str.get()
        str_len_edge = len(input_string) - 1
        print("Input: ", input_string)

        curr_state = dpda.current

        while not (dpda.is_final() and index == str_len_edge) and not err:
            self.fstep()
            self.root.update_idletasks()
            self.root.after(100)

        print("done")
        #
        self.step.config(state=ACTIVE)
        self.run.config(state=ACTIVE)
        self.reset.config(state=ACTIVE)
        self.input_str.config(state=NORMAL)
        if dpda.is_final() and index == str_len_edge:
            self.step.config(state=DISABLED)

    def fpause(self):
        print("pausing")

    def fstep(self):
        print("stepping")
        global input_string, str_len_edge, index, steps, err, curr_state, next_state, char_push, char_pop

        if dpda.is_final() and index == str_len_edge:
            self.step.config(state=DISABLED)

        char = input_string[index]
        print(char, index, str_len_edge)

        try:
            current_state, transition = dpda.read_symbol(char)
            curr_state_label = current_state.label

            # moved states
            if curr_state == current_state:
                char_pop = current_state.get_transition(char)[1]
                next_state = current_state.get_transition(char)[2]
                char_push = current_state.get_transition(char)[3]
            else:
                next_state = current_state.label
                char_pop = transition[1]
                char_push = transition[3]

            # remove_color(header_value_text)
            if index < 0:
                index = len(input_string) + index
            # change_character_color(header_value_text, index, "red")

            print(
                f"Read Character: {char}, Current State: {curr_state_label}, Next State: {next_state}, Push | Pop: {char_push} | {char_pop}")
            steps += 1

            if char_push == 'e' or char_pop == 'e':
                print("Current stack: ", end="")
                dpda.print_Stack()

            if char_push != 'e':
                dpda.push(str(char_push))
                print("Stack after pushing: ", end="")
                dpda.print_Stack()

            if char_pop != 'e':
                if dpda.stack_top[-1] == char_pop:
                    dpda.pop()
                    print("Stack after popping: ", end="")
                    dpda.print_Stack()
                # symbol to pop and stack top are not equal
                else:
                    print("halt-reject")
                    self.currstateval = "halt-reject"
                    err = True
                    self.step.config(state=DISABLED)

        except ValueError:
            # Current symbol is invalid
            print("halt-reject")
            self.currstateval = "halt-reject"
            err = True
            self.step.config(state=DISABLED)

        if dpda.is_done():
            current_state = dpda.read_symbol('e')
        else:
            index += 1

        if dpda.is_final() and index == str_len_edge:
            print("halt-accept")
            self.currstateval = "halt-accept"
            self.step.config(state=DISABLED)

        if index > str_len_edge:
            print("halt-reject")
            self.currstateval = "halt-reject"
            err = True
            self.step.config(state=DISABLED)

        print()

    def freset(self):
        print("resetting")


GUI()
