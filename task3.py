def check_brackets(sequence):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    opening = brackets.keys()
    closing = brackets.values()

    only_brackets = [char for char in sequence if char in opening or char in closing]

    for char in only_brackets:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return "Несиметрично"
            last_open = stack.pop()
            if brackets[last_open] != char:
                return "Несиметрично"

    return "Симетрично" if not stack else "Несиметрично"


examples = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for expr in examples:
    result = check_brackets(expr)
    print(f"{expr}: {result}")
