import re
import AFNgraph
# niveles importantes
PRECEDENCE = {
    '?': 4, 
    '*': 3,
    '|': 3,
    '+': 2,
    '-': 2,
    '(': 1,
}
def PostfixFromRegex():

    def infixToPostfix(expr):
        tokens = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\?\+\*\-\|])", expr)
        stack = []
        postfix = []

        for token in tokens:
            #si el token es un operando empujarlo al output
            if token.isalnum():
                postfix.append(token)

            #si el token es un parentesis izquierdo meterlo al stack
            elif token == '(':
                stack.append(token)

            
            elif token == ')':
                top = stack.pop()
                while top != '(':
                    postfix.append(top)
                    top = stack.pop()

            
            else:
                while stack and (PRECEDENCE[stack[-1]] >= PRECEDENCE[token]):
                    postfix.append(stack.pop())
                stack.append(token)

        
        while stack:
            postfix.append(stack.pop())
        
        return postfix


    def listToString(s):
 
        
        str1 = ""
    
        
        for ele in s:
            str1 += ele
    
        
        print(str1)
        return str1

    regex = input("Ingrese su expresion regular: ")

    

    expressions = [regex]


    for expr in expressions:
        lista=(infixToPostfix(expr))

    final=listToString(lista)

   
