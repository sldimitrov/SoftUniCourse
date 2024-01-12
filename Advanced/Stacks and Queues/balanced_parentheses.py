from collections import deque

parentheses = deque(input())
open_parentheses = deque

while parentheses:
    current_parentheses = parentheses.popleft()

    if current_parentheses in "([{":
        open_parentheses.append(current_parentheses)
    elif not open_parentheses:
        print("NO")
        break
    else:
        if f"{open_parentheses.pop + current_parentheses}" not in "{}[]()":
            print("NO")
            break

else:
    print("YES")