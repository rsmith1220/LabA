from graphviz import Digraph

class NFAState:
    def __init__(self, transitions, accepting=False):
        self.transitions = transitions
        self.accepting = accepting

def postfix_to_nfa(postfix):
    stack = []
    for c in postfix:
        if c.isalpha():
            #transiciones
            state1 = NFAState(transitions={c: [1]})
            state2 = NFAState(transitions={}, accepting=True)
            state1.transitions[''] = [state2]
            #se hace un stack para luego hacer un pop
            stack.append(state1)
            stack.append(state2)

            #epsilon
        elif c == 'ε':
            state2 = stack.pop()
            state1 = stack.pop()
            for t, states in state1.transitions.items():
                for s in states:
                    if t not in state2.transitions:
                        state2.transitions[t] = []
                    state2.transitions[t].append(s)
            stack.append(state1)
            stack.append(state2)

            #kleene
        elif c == '*':
            state = stack.pop()
            new_state = NFAState(transitions={})
            new_state.transitions[''] = [state]
            state.transitions[''] = [state, new_state]
            stack.append(new_state)

            #mas
        elif c == '+':
            state = stack.pop()
            new_state = NFAState(transitions={})
            new_state.transitions[''] = [state]
            state.transitions[''] = [new_state]
            stack.append(new_state)
        else:
            if c == '|':
                state2 = stack.pop()
                state1 = stack.pop()
                new_state = NFAState(transitions={}, accepting=True)
                new_state.transitions[''] = [state1, state2]
                for t, states in state1.transitions.items():
                    for s in states:
                        if t not in new_state.transitions:
                            new_state.transitions[t] = []
                        new_state.transitions[t].append(s)
                for t, states in state2.transitions.items():
                    for s in states:
                        if t not in new_state.transitions:
                            new_state.transitions[t] = []
                        new_state.transitions[t].append(s)
                stack.append(new_state)
    start_state = stack.pop()
    
    # Se crea un pdf con la imagen usando graphviz
    graph = Digraph()
    graph.attr('graph', rankdir='LR')  # Set the rankdir attribute to the graph instead of to the node
    graph.attr('node', shape='circle')
    state_ids = {}
    def add_states_to_graph(state):
        if id(state) not in state_ids:
            state_id = len(state_ids) + 1
            state_ids[id(state)] = state_id
            graph.node(str(state_id), style='doublecircle' if state.accepting else '')
            for t, states in state.transitions.items():
                for s in states:
                    add_states_to_graph(s)
                    graph.edge(str(state_id), str(state_ids[id(s)]), label=t)
    add_states_to_graph(start_state)
    
    return graph
