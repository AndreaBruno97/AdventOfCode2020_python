def createToken(x):
    if x == "+" or x == "*" or x == "(" or x == ")":
        return x
    return int(x)


''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

'''
Compiler for the given language:
 - Lexical analysis: from string to tokens
 - Syntax analysis: from tokens to rules
 - Semantic analysis: from rules to output computation
'''

total = 0
for line in content:
    '''
    Lexical analysis: create token ( symbols remain equal, numbers are turned into integers)
        integer -> INT
        "+"     -> PLUS
        "*"     -> TIMES
        "("     -> RO
        ")"     -> RC
    '''
    # Each parenthesis is surrounded by spaces
    line = line.replace("\n", "").replace("(", "( ").replace(")", " )")
    token_list = list(map(createToken, line.split(" ")))

    '''
    Syntax analysis: each token is put in the stack one at the time, 
    and then in the stack is compared to the possible rules
    (In this simplified version, I avoid generalization for operands and rules to aggregate lists)
    
    To enforce the precedence of addition to multiplication, one lookahead symbol is needed:
        the multiplication can be done if the next symbol is not a plus 
    
        RO INT RC       -> INT
        INT PLUS INT    -> INT
        INT TIMES INT (Next is not PLUS) -> INT

    At the end of the process, in  the stack there will be an INT, result of the operations.   

    Semantic analysis: to each rule, the corresponding mathematical operation is associated to the INT value put in the stack:
             "( 3 )" -> 3
             "1 + 2" -> 3
             "2 * 3" -> 6
    '''
    stack = []
    for index, token in enumerate(token_list):
        stack.append(token)

        while True:
            # Rule 1: RO INT RC -> INT
            if len(stack) >= 3 and stack[-3] == "(" and isinstance(stack[-2], int) and stack[-1] == ")":
                # Extract 3 from "( 3 )"
                new_val = stack[-2]

                # Update the stack
                stack.pop()
                stack.pop()
                stack.pop()

                stack.append(new_val)
                continue

            # Rule 2: INT PLUS INT -> INT
            elif len(stack) >= 3 and isinstance(stack[-3], int) and stack[-2] == "+" and isinstance(stack[-1], int):
                # Extract 3 from "1 + 2"
                new_val = stack[-3] + stack[-1]

                # Update the stack
                stack.pop()
                stack.pop()
                stack.pop()

                stack.append(new_val)
                continue

            # Precedence rule: lookahead symbol must not be PLUS
            if index < len(token_list) - 1 and token_list[index+1] == "+":
                break

            # Rule 3: INT TIMES INT -> INT
            elif len(stack) >= 3 and isinstance(stack[-3], int) and stack[-2] == "*" and isinstance(stack[-1], int):
                # Extract 6 from "3 * 2"
                new_val = stack[-3] * stack[-1]

                # Update the stack
                stack.pop()
                stack.pop()
                stack.pop()

                stack.append(new_val)
                continue

            break

    # At the end of the process, in  the stack there will be an INT, result of the operations.
    total += stack[0]

print("The sum of all expressions is " + str(total))