# Deterministic Pushdown Automata

## STALGCM - S11
- GON GON, Zhoe Aeris
- SULIT, Anne Gabrielle
- TORIO, Ysobella

## Introduction
This README provides instructions on how to use the provided text file template to define a Deterministic Pushdown Automaton (DPDA) for accepting a specific language. The DPDA is used to determine if an input string belongs to a specified language.

## Instructions

### 1. Template Structure
The template file consists of a series of lines, each representing a state definition for the DPDA. A state definition includes the state label, transitions, and whether the state is a final state (accepting or rejecting).

### 2. Defining States and Transitions
Each state definition is enclosed within parentheses '()'. The structure of a state definition is as follows:

- `<state_label>`: The label for the state. The first state defined is always the initial state.
- `<input_symbol>`: The input symbol triggering the transition.
- `<symbol_to_pop>`: The symbol to be popped from the stack.
- `<next_state>`: The label of the next state.
- `<symbol_to_push>`: The symbol to be pushed onto the stack.
- `<final_state>`: 'True' if the state is a final (accepting or rejecting) state, 'False' otherwise.

### 3. Adding Language and Transitions
To define your own language and transitions, follow these steps:
- Locate the template lines within the file and replace them with your own state definitions.
- Update the `<state_label>`, `<input_symbol>`, `<symbol_to_pop>`, `<next_state>`, `<symbol_to_push>`, and `<final_state>` values accordingly.

### 4. Final State Determination
The DPDA must have at least one final state. To determine whether a state should be final, set the `<final_state>` value to 'True' if the state should be an accepting state, and 'False' otherwise.

### 5. Running the DPDA
Once you've defined your DPDA using the template, you can use DPDA simulation tools or in the program to process input strings and determine whether they are accepted by the defined language.
