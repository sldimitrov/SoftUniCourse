# Define a function
from collections import deque


def math_operations(*args, **kwargs):
    keys = list(kwargs.keys())

    numbers = deque(args)

    for i in range(len(args)):
        idx = keys[i % 4]
        num = numbers.popleft()

        if idx == 'a':
            kwargs[idx] += num
        elif idx == 's':
            kwargs[idx] -= num
        elif idx == 'd':
            if num != 0:
                kwargs[idx] /= num
        elif idx == 'm':
            kwargs[idx] *= num

        if not numbers:
            break

    sorted_dict = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    return '\n'.join(f"{k}: {v:.1f}" for k, v in sorted_dict)

# Test code
print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
