import graphviz

def create_nfa(postfix_expression):
    dot = graphviz.Digraph(comment='NFA')
    # Step 1: Recibir y parsear la expresion postfix
    stack = []
    for token in postfix_expression:
        if token == '*': 
            state = {'id': len(stack), 'transitions': [(len(stack), len(stack) + 1)], 'accepting': False}
            stack.append(state)

        elif token == '|':
            #usando stack y pop se actualiza el stack
            #procesa un token y actualiza el stack
            right_state = stack.pop()
            left_state = stack.pop()
            new_state = {'id': len(stack), 'transitions': [], 'accepting': False}
            new_state['transitions'] += left_state['transitions']
            new_state['transitions'] += right_state['transitions']
            stack.append(new_state)

        elif token == '+':  
            right_state = stack.pop()
            left_state = {'id': len(stack), 'transitions': [], 'accepting': False}
            left_state['transitions'] += right_state['transitions']
            left_state['transitions'].append((left_state['id'], right_state['id']))
            stack.append(left_state)

        elif token == 'ε':
            state = {'id': len(stack), 'transitions': [(len(stack), len(stack) + 1, 'ε')], 'accepting': False}
            stack.append(state)

        else:
            state = {'id': len(stack), 'transitions': [(len(stack), len(stack) + 1, token)], 'accepting': True}
            stack.append(state)

    # Crea una lista de los estados
    states = stack

    # crea el estado inicial
    start_state = {'id': 0, 'transitions': [], 'accepting': False}
    states.insert(0, start_state)

    # Conecta los estados
    for state in states:
        for transition in state['transitions']:
            if len(transition) == 2:
                transition += ('',)
            label = transition[2]
            dot.edge(str(state['id']), str(transition[1]), label=label)

    # Step 5: Mark final states as accepting states
    #Marca los estados finales como estados aceptadores
    for state in states:
        if state['id'] == len(states) - 1:
            state['accepting'] = True

    # Retornar 
    #este dot crea el documento para ver el resultado de la maquina
    dot.view()
    return start_state




