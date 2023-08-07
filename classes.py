"""
    This class represents the Deterministic PDA Machine.

    members:
        list (states): list of State objects
        State (current): current state. the first state is always the first object in list states.
"""


class Machine:
    def __init__(self, states):
        if not states:
            raise ValueError("The states list must be given.")
        self.states = states
        self.current = self.states[0]
        self.stack_top = ["Z"]

    """This read the symbol. """
    def read_symbol(self, symbol):
        transition = self.current.get_transition(symbol)
        if transition[0] == "error":
            raise ValueError("Invalid transition passed in State: " + self.current.label)

        print(f"Transition: {transition}")
        input_symbol, symbol_to_pop, next_state_label, symbol_to_push = transition
        next_state = next((state for state in self.states if state.label == next_state_label), None)
        if next_state is None:
            raise ValueError("State " + next_state_label + " is unreachable")
        else:
            self.current = next_state

        # self.current.print_state()
        #  Returns: a tuple of new current state
        return self.current, transition

    def push(self, symbol):
        print("pushing ", symbol)
        self.stack_top.append(symbol)

    def pop(self):
        if self.stack_top:
            print("popping ", self.stack_top.pop())

    def print_Stack(self):
        print(self.stack_top)

    def is_final(self):
        return self.current.is_final

    def is_done(self):
        return all(symbol == "Z" for symbol in self.stack_top)

    def reset_machine(self):
        self.current = self.states[0]


"""
    This class represents a state in a PDPA Machine.

    members:
        string (label): label of state
        list (transitions): a list of tuples that represent the transitions of state
        boolean  (is_final): determines if state is a final state
        notes:
            the list members are of the following types:
                (string_literal, Number,string_literal)
                they stand for (next state label, the character to read)
"""


class State:
    def __init__(self, state):
        self.label, self.transitions, self.is_final = state
        # self.print_state()

    """identify a valid transition given a symbol."""

    def get_transition(self, symbol):
        try:
            # print("Get Transition: ", next(val for val in self.transitions if val[0] == symbol))
            return next(val for val in self.transitions if val[0] == symbol)
        except StopIteration:
            # return a default transition to handle situation where there is no valid transition for the symbol
            return "No valid transition", symbol

    def print_state(self):
        print("Label:", self.label)
        print("Transitions:", self.transitions)
        print("Is Final:", self.is_final)