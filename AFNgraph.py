import graphviz

def create_nfa(postfix_expression):
    dot = graphviz.Digraph(comment='NFA')
    #Recibir y parsear la expresion postfix
    stack = []
    for token in postfix_expression:
        if token == '*': 
            #push a la lista STACK
                        #key                            #value
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
            #hace un pop y una transicion a si mismo
            right_state = stack.pop()
            left_state = {'id': len(stack), 'transitions': [], 'accepting': False}
            left_state['transitions'] += right_state['transitions']
            left_state['transitions'].append((left_state['id'], right_state['id']))
            stack.append(left_state)

        elif token == '?':
            #hace pop a dos estados
            #crea un nuevo estado de la izquierda a la derecha
            right_state = stack.pop()
            left_state = stack.pop()
            new_state = {'id': len(stack), 'transitions': [], 'accepting': False}
            new_state['transitions'] += left_state['transitions']
            new_state['transitions'] += right_state['transitions']
            new_state['transitions'].append((left_state['id'], right_state['id'], ''))
            stack.append(new_state)

        elif token == 'ε':
            #push al siguiente estado
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
                transition += ('ε',)
            label = transition[2]
            #con este dot se crea el grafo
            dot.edge(str(state['id']), str(transition[1]), label=label)

   
    # Retornar 
    #este dot crea el documento para ver el resultado de la maquina
    dot.view()
    return start_state




