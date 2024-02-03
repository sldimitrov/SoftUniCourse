from collections import deque

parentheses = deque(input())
opening_parentheses = deque()

while parentheses:
    current_parentheses = parentheses.popleft()

    if current_parentheses in "({[":
        opening_parentheses.append(current_parentheses)
    elif not opening_parentheses:
        print("NO")
        break
    else:
        if f"{opening_parentheses.pop() + current_parentheses}" not in "(){}[]":
            print("NO")
            break

else:
    print("YES")