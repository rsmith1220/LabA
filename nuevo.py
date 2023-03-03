import graphviz

g = graphviz.Digraph('finite_state_machine', filename='process.gv')
g.attr(rankdir='LR', size='8,5')

postfix = 'ab|a*'

# g.edge('LR_0', 'LR_1', label='SS(S)')

labels=[]

create=[]

graph=[]



def Dibujar(lista):
    suma=0
    ultimo = 'nada'
    ver=0
    
    while suma != 1:
        op=lista.pop()
        other=lista.pop()
        if op == '|' or other == '|':
            lugar = 'a0'
        elif op == '*'or other == '*':
            lugar = 'b0'
        elif op == '?'or other == '?':
            lugar = 'c0'
        elif op == '+'or other == '+':
            lugar = 'd0'
        elif op == 'ε'or other == 'ε':
            lugar = 'e0'
        else:
            suma -= 1
        suma += 1
        lista.append(other)
        lista.append(op)

 
    pasae=0

    viene = 0

    siguiente = ''

    verificar = 'jota'

    nombrecito = 0

    contar=0
    # g.edge('0',lugar,label='ε')
    while contar < len(lista):
        token=lista.pop()
        #estado inicial
        

        if token == '|':
            g.edge('a0','a1',label='ε')
            try:
                g.edge('a1','a2',label=create[0])
            except:
                verificar = lista.pop()
                if verificar == '|' or verificar == '*' or verificar== '?' or verificar == '+' or verificar == 'ε':
                    flecha = lista.pop()
                    lista.append(verificar)
                    g.edge('a1','a2', label=flecha)
                else:
                    # g.edge('a1','a2',label=verificar)
                    flecha = lista.pop()
                    g.edge('a1','a2', label=flecha)
                    create.append(verificar)
            g.edge('a0','a3',label='ε')
            try:
                if nombrecito == 0:
                    g.edge('a3','a4',label=create[1])
                else:
                    pass
            except:
                if verificar == '|' or verificar == '*' or verificar== '?' or verificar == '+' or verificar == 'ε':
                    flecha = lista.pop()
                    lista.append(verificar)
                    if nombrecito == 0:
                        g.edge('a3','a4', label=flecha)
                    else:
                        g.edge('a3','a4')
                else:
                    if nombrecito == 0:
                        g.edge('a3','a4',label=verificar)
                    else:
                        g.edge('a3','a4')
            g.edge('a2','a5',label='ε')
            g.edge('a4','a5',label='ε')
            if pasae ==1:
                if ver == 0:
                    ultimo = 'a5'
                    ver +=1
                else:
                    g.edge(ultimo,'a0')
            else:
                if viene == 0:
                    ultimo = 'a0'
                    viene+=1
                else:
                    g.edge('a3',ultimo)
                    g.edge(siguiente, 'a4')
                    # g.edge('a3','a4')


        elif token == '*':
            g.edge('b0','b1',label='ε')
            try:
                g.edge('b1','b2',label=create[0])
            except:
                verificar = lista.pop()
                if verificar == '|' or verificar == '*' or verificar== '?' or verificar == '+' or verificar == 'ε':
                    flecha = lista.pop()
                    
                    if verificar == '|':
                        lista.append(flecha)
                    else:
                        pass
                    lista.append(verificar)
                    g.edge('b1','b2',label=flecha)
                else:
                    g.edge('b1','b2',label=verificar)
                
            g.edge('b2','b1',label='ε')
            g.edge('b2','b3',label='ε')
            g.edge('b0','b3',label='ε')
            if pasae == 1:
                pasae =+1
                if ver == 0:
                    ultimo = 'b3'
                    ver +=1
                else:
                    g.edge(ultimo,'b0')
            else:
                if viene == 0:
                    ultimo = 'b0'
                    siguiente = 'b3'
                    viene=+1
                    nombrecito+=1
                else:
                    
                    g.edge('b3',ultimo)
                    g.edge(siguiente, 'b3')
            


        elif token == '?':
            pasae+=1
            g.edge('c0','c1',label='ε')
            try:
                g.edge('c1','c2',label=create[0])
            except:
                g.edge('c1','c2',label=lista[0])
            g.edge('c0','c3',label='ε')
            g.edge('c3','c4',label='ε')
            g.edge('c2','c5',label='ε')
            g.edge('c4','c5',label='ε')
            if ver == 0:
                ultimo = 'c5'
                ver+=1
            else:
                g.edge(ultimo,'c0')


        elif token == '+':
            g.edge('d0','d1',label=create[0])
            g.edge('d1','d2',label='ε')
            g.edge('d3','d4',label='ε')
            g.edge('d2','d3',label=create[0])
            g.edge('d3','d2',label='ε')
            g.edge('d1','d4',label='ε')
            try:
                g.edge('d4','d5',label=create[1])
            except:
                g.edge('d4','d5',label=lista.pop())
            if ver == 0:
                ultimo = 'd5'
                ver +=1
            else:
                g.edge(ultimo,'d0')


        elif token == 'ε':
            g.edge('e0','e1',label='ε')
            if ver == 0:
                ultimo = 'e1'
                ver +=1
            else:
                g.edge(ultimo,'e0')


        else:
            create.append(token)
        
        contar+=1
    if len(lista) >0 or len(create)>0:
            try:
                boo=lista.pop()
                g.edge(ultimo, '6', label=boo)
            except:
                boo = create.pop()
                g.edge(ultimo, 'last', label=boo)
    else:
        pass
            

        

for token in postfix:
    labels.append(token)
    # print(labels)

Dibujar(labels)
g.view()