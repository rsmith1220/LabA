import AFNgraph
def Postfix():
    #Definir un diccionario para saber el orden 
    precedence = {'|': 1, '.': 2, '?': 3, '*': 3, '+': 3}

    # Define caracteres especiales
    specials = ['|', '.', '?', '*', '+', '(', ')','ε']

    def regex_to_postfix(regex):
        #convertir la expresion a postfix
        output = []
        stack = []
        for char in regex:
            #append a una lista si no es un caracter especial
            if char not in specials:
                output.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                #si el parentesis no es el que se abre, lo agrega
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
                #Si el caracter es un operador, la funcion hace pop
            else:
                while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                    output.append(stack.pop())
                stack.append(char)
        #append si todavia hay caracteres
        while stack:
            output.append(stack.pop())
        #regresa el output como un string
        return ''.join(output)

    
    regex = input("Ingrese su expresion regular: ")
    postfix = regex_to_postfix(regex)
    print(f"Postfix: {postfix}")
    #se llama la clase AFNgraph para hacer el grafo
    AFNgraph.create_nfa(postfix)
    

    
    