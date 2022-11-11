expression = input()

stack = []

for idx in range(len(expression)):

    character = expression[idx]

    if character == '(':
        stack.append(idx)

    elif character == ')':

        last_opening_bracket_idx = stack.pop()
        sub_expression = expression[last_opening_bracket_idx : idx + 1]
        print(sub_expression)