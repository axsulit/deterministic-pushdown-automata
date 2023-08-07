import tkinter
from ast import literal_eval
from tkinter import *
from classes import State, Machine

states_list = set()
states_obj_list = set()
dpda = Machine([()])

done = False
err = False
curr_state = set()
input_string = ""
str_len_edge = 0
index = 0
steps = 0


class GUI:
    def __init__(self):
        # Window
        self.root = Tk()
        self.root.title("Deterministic PDA")
        self.root.resizable(False, False)
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
        self.rightFrame.pack(side="left")
        self.entryFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.entryFrame.pack(side="top", pady=10, padx=50, fill=tkinter.X)
        self.ctrlsFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.ctrlsFrame.pack(side="top", pady=10, padx=50, fill=tkinter.X)
        self.inputStrFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.inputStrFrame.pack(side="top", pady=10, padx=50, fill=tkinter.X)
        self.currStFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.currStFrame.pack(side="top", pady=10, padx=50, fill=tkinter.X)
        self.stepsFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.stepsFrame.pack(side="top", pady=10, padx=50, fill=tkinter.X)
        self.stackFrame = Frame(self.rightFrame, bg="#98c1d9")
        self.stackFrame.pack(side="top", pady=10, padx=50, fill=tkinter.X)

        # Machine Program
        self.label = Label(self.programFrame, bg="#98c1d9", text="Machine Program", font=('Arial', 13),
                           padx=20, pady=6)
        self.label.pack()
        self.scrollbar = Scrollbar(self.programDefFrame, orient='vertical')
        self.scrollbar.pack(side=RIGHT, fill='y', pady=0)
        self.machineprog = Text(self.programDefFrame, font=('Fixedsys', 10), height=27, width=75,
                                yscrollcommand=self.scrollbar.set)
        self.machineprog.pack()
        self.display_file("sample.txt")

        # Input a String
        self.label = Label(self.entryFrame, bg="#98c1d9", text="Input a String", font=('Arial', 12), pady=2)
        self.label.pack()
        self.input_str = Entry(self.entryFrame, bd=1, width=32, font=('Arial', 9))
        self.input_str.pack(fill=tkinter.BOTH)

        # Controls
        self.label = Label(self.ctrlsFrame, bg="#98c1d9", text="Controls", font=('Arial', 12), pady=2)
        self.label.pack(side="top")
        self.btnFrame = Frame(self.ctrlsFrame, bg="#98c1d9")
        self.btnFrame.pack(side="top")
        self.run = Button(self.btnFrame, text="Run", font=('Arial', 9), command=self.frun, width=7)
        self.run.pack(side="left", padx=5, pady=5)
        self.step = Button(self.btnFrame, text="Step", font=('Arial', 9), command=self.fstep, width=7)
        self.step.pack(side="left", padx=5, pady=5)
        self.reset = Button(self.btnFrame, text="Reset", font=('Arial', 9), command=self.freset, width=7)
        self.reset.pack(side="left", padx=5, pady=5)

        # Given String
        self.label = Label(self.inputStrFrame, bg="#98c1d9", text="Given String", font=('Arial', 12), pady=2)
        self.label.pack()
        self.given_label = Text(self.inputStrFrame, bg="#e0fbfc", font=('Arial', 13), padx=0,
                                pady=1, wrap=WORD, width=50, height=1)
        self.given_label.insert(END, "N/A")
        self.given_label.tag_config("center", justify='center')
        self.given_label.tag_add("center", "1.0", "end")
        self.given_label.config(state=DISABLED)
        self.given_label.pack(fill=tkinter.BOTH, expand=True, pady=10, padx=5)

        # Current State
        self.currstatelbl = Label(self.currStFrame, bg="#98c1d9", text="Current State", font=('Arial', 12), pady=2)
        self.currstatelbl.pack()
        self.currstateval = Label(self.currStFrame, bg="#e0fbfc", text="0", font=('Arial', 13), padx=20, pady=1)
        self.currstateval.pack(fill=tkinter.BOTH)

        # Steps
        self.stepslbl = Label(self.stepsFrame, bg="#98c1d9", text="Steps", font=('Arial', 12), pady=2)
        self.stepslbl.pack()
        self.stepsval = Label(self.stepsFrame, bg="#e0fbfc", text="0", font=('Arial', 13), padx=20, pady=1)
        self.stepsval.pack(fill=tkinter.BOTH)

        # Stack
        self.stacklbl = Label(self.stackFrame, bg="#98c1d9", text="Stack", font=('Arial', 12), pady=2)
        self.stacklbl.pack()
        self.stackval = Label(self.stackFrame, bg="#e0fbfc", text="Z", font=('Arial', 13), padx=20)
        self.stackval.pack(fill=tkinter.BOTH)

        self.root.mainloop()

    def get_machine_text(self):
        text_content = self.machineprog.get("1.0", END).strip()
        lines = text_content.splitlines()
        text_content = "\n".join(line for line in lines if (not line.startswith(';') and not line == ""))
        lines = text_content.splitlines()
        return [literal_eval(strings) for strings in lines]

    def display_file(self, path):
        with open(path, 'r') as fptr:
            stream = fptr.read()
            self.machineprog.insert(END, stream)

    def change_text(self, new_text):
        """Change the text in the given Text widget."""
        self.given_label.config(state=NORMAL)
        self.given_label.delete("1.0", END)
        self.given_label.insert(END, new_text)
        self.given_label.tag_configure("center", justify='center')
        self.given_label.tag_add("center", "1.0", "end")
        self.given_label.config(state=DISABLED)

    def change_character_color(self, char_index, color):
        """Change the color of a specific character and set all other characters to a different color in the given
        Text widget. """
        self.given_label.config(state=NORMAL)
        self.given_label.tag_configure("colored", foreground=color)
        self.given_label.tag_add("colored", f"1.{char_index}")
        self.given_label.config(state=DISABLED)

    def remove_color(self):
        self.given_label.config(state=NORMAL)
        self.given_label.tag_remove("colored", "1.0", "end")
        self.given_label.config(state=DISABLED)

    def frun(self):
        print("running")
        if self.input_str.get() == "":
            self.reset.config(state=DISABLED)
        else:
            global input_string, str_len_edge, index, steps, err, curr_state, states_list, states_obj_list, dpda

            # Get list of states as defined by the given machine
            states_list = self.get_machine_text()

            # Convert state list to state objects
            states_obj_list = [State(s) for s in states_list]

            # Create DPDA Machine
            dpda = Machine(states_obj_list)

            input_string = self.input_str.get()
            str_len_edge = len(input_string) - 1

            curr_state = dpda.current

            self.change_text(input_string)

            self.step.config(state=DISABLED)
            self.reset.config(state=DISABLED)

            while not (dpda.is_final() and index == str_len_edge) and not err:
                self.fstep()
                self.root.update_idletasks()
                self.root.after(700)

            self.reset.config(state=ACTIVE)
            self.input_str.config(state=DISABLED)

    def fstep(self):
        print("stepping")

        if self.input_str.get() == "":
            self.reset.config(state=DISABLED)
        else:
            global done, input_string, str_len_edge, index, steps, err, curr_state, next_state, char_push, char_pop, states_list, states_obj_list, dpda

            # Get list of states as defined by the given machine
            states_list = self.get_machine_text()

            # Convert state list to state objects
            states_obj_list = [State(s) for s in states_list]

            # Create DPDA Machine
            dpda = Machine(states_obj_list)

            input_string = self.input_str.get()
            str_len_edge = len(input_string) - 1

            curr_state = dpda.current

            self.change_text(input_string)

            if dpda.is_final() and index == str_len_edge:
                self.step.config(state=DISABLED)

            char = input_string[index]
            print(char, index, str_len_edge)

            if done:
                print("almost done")
                self.currstateval.config(text=curr_state.label)
                current_state, transition = dpda.read_symbol('e')
                dpda.pop()
            else:
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

                    self.remove_color()

                    if index < 0:
                        index = len(input_string) + index
                    self.change_character_color(index, "red")

                    print(
                        f"Read Character: {char}, Current State: {curr_state_label}, Next State: {next_state}, Push | Pop: {char_push} | {char_pop}")
                    steps += 1
                    self.currstateval.config(text=curr_state_label)
                    self.stepsval.config(text=steps)

                    if char_push == 'e' or char_pop == 'e':
                        print("Current stack: ", end="")
                        dpda.print_stack()
                        self.stackval.config(text=' '.join(dpda.stack_top))

                    if char_push != 'e':
                        dpda.push(str(char_push))
                        print("Stack after pushing: ", end="")
                        dpda.print_stack()
                        self.stackval.config(text=' '.join(dpda.stack_top))

                    if char_pop != 'e':
                        if dpda.stack_top[-1] == char_pop:
                            dpda.pop()
                            print("Stack after popping: ", end="")
                            dpda.print_stack()
                            self.stackval.config(text=' '.join(dpda.stack_top))
                        # symbol to pop and stack top are not equal
                        else:
                            print("halt-reject (symbol to pop and stack top are not equal)")
                            self.currstateval.config(text="halt-reject")
                            err = True
                            self.step.config(state=DISABLED)

                    if not dpda.is_done():
                        index += 1
                    else:
                        done = True

                except ValueError:
                    # Current symbol is invalid
                    print("halt-reject (Current symbol is invalid)")
                    self.currstateval.config(text="halt-reject")
                    err = True
                    self.step.config(state=DISABLED)

            if dpda.is_final() and index == str_len_edge:
                print("halt-accept")

                self.currstateval.config(text="halt-accept")
                self.step.config(state=DISABLED)
                self.stackval.config(text=' '.join(dpda.stack_top))

            elif index > str_len_edge or len(dpda.stack_top) == 0:
                # Incomplete tape or stack is emptied before string is done being read
                print("halt-reject")
                self.currstateval.config(text="halt-reject")
                err = True
                self.step.config(state=DISABLED)

            print()

    def freset(self):
        print("resetting")

        global input_string, str_len_edge, index, steps, err, done, dpda

        err = False
        done = False
        input_string = self.input_str.get()
        self.change_text(input_string)
        str_len_edge = len(input_string) - 1
        index = 0
        steps = 0
        self.currstateval.config(text=0)
        self.stepsval.config(text=0)
        self.stackval.config(text="Z")
        self.run.config(state=ACTIVE)
        self.step.config(state=ACTIVE)
        self.input_str.config(state=NORMAL)
        dpda.reset_machine()


if __name__ == '__main__':
    GUI()
