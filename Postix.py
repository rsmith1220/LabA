def Postfix():
    # Define the operator precedence
    precedence = {'|': 1, '.': 2, '?': 3, '*': 3, '+': 3}

    # Define the special characters
    specials = ['|', '.', '?', '*', '+', '(', ')','ε']

    def regex_to_postfix(regex):
        """Convert a regular expression to postfix."""
        output = []
        stack = []
        for char in regex:
            if char not in specials:
                output.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                    output.append(stack.pop())
                stack.append(char)
        while stack:
            output.append(stack.pop())
        return ''.join(output)

    # Example usage
    regex = input("Enter a regular expression: ")
    postfix = regex_to_postfix(regex)
    print(f"Postfix: {postfix}")
