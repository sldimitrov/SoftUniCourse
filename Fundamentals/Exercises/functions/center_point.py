# Define a function
def center_point(x1:float, y1:float, x2:float, y2:float)-> int:
    first_pair = abs(x1) + abs(y1)
    second_pair = abs(x2) + abs(y2)
    if first_pair < second_pair:
        print(f'{round(x1), round(y1)}')
    else:
        print(f'{round(x2), round(y2)}')
    return True

# Read User input
first_parameter = float(input())
second_parameter = float(input())
third_parameter = float(input())
forth_parameter = float(input())
result = center_point(first_parameter, second_parameter, third_parameter, forth_parameter)

# Print function's return
