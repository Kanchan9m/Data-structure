def infixToPostfix(exp: str) -> str:
    # Write your code here.
    OPERATORS = ['+', '-', '*', '/', '(', ')', '^']
    PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = [] 
    output = ''
    for ch in exp:
        if ch not in OPERATORS:
            output+= ch
        elif ch=='(':
            stack.append('(')
        elif ch==')':
            while len(stack) != 0 and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()

        else:
            while len(stack) != 0 and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    while len(stack) != 0:
        output+=stack.pop()
    return output

exp = '3^(1+)'
print(infixToPostfix(exp))