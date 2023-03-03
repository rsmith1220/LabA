import graphviz

g = graphviz.Digraph('finite_state_machine', filename='process.gv')
g.attr(rankdir='LR', size='8,5')

postfix = 'ε'

# g.edge('LR_0', 'LR_1', label='SS(S)')

labels=[]

create=[]

graph=[]



def Dibujar(lista):
    contar=0
    while contar < len(lista):
        token=lista[contar]
        if token == '|':
            g.edge('0','1',label='ε')
            g.edge('1','2',label=create[0])
            g.edge('0','3',label='ε')
            g.edge('3','4',label=create[1])
            g.edge('2','5',label='ε')
            g.edge('4','5',label='ε')

        elif token == '*':
            g.edge('0','1',label='ε')
            g.edge('1','2',label=create[0])
            g.edge('2','1',label='ε')
            g.edge('2','3',label='ε')
            g.edge('0','3',label='ε')

        elif token == '?':
            g.edge('0','1',label='ε')
            g.edge('1','2',label=create[0])
            g.edge('0','3',label='ε')
            g.edge('3','4',label='ε')
            g.edge('2','5',label='ε')
            g.edge('4','5',label='ε')

        elif token == '+':
            g.edge('0','1',label='ε')
            g.edge('1','2',label='ε')
            g.edge('3','4',label='ε')
            g.edge('2','3',label=create[0])
            g.edge('3','2',label='ε')
            g.edge('1','4',label='ε')
            g.edge('4','5',label=create[1])

        elif token == 'ε':
            g.edge('0','1',label='ε')

        else:
            create.append(token)
        
        contar+=1

        

for token in postfix:
    labels.append(token)
    # print(labels)

Dibujar(labels)
g.view()