from collections import deque

def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()  
    chars = deque(s)

    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True

strings = ["Казак", "Я несу гусеня", "Радар", "Паліндром"]

for s in strings:
    result = "паліндром" if is_palindrome(s) else "не паліндром"
    print(f"'{s}' — це {result}")
