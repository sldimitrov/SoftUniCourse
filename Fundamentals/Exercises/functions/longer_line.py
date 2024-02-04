import math
x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())


# Define a function
def hypotenuse(x, y):
    result = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return result


hypotenuse_1 = hypotenuse(x_1, y_1) + hypotenuse(x_2, y_2)
hypotenuse_2 = hypotenuse(x_3, y_3) + hypotenuse(x_4, y_4)

if hypotenuse_1 > hypotenuse_2:
    distance_to_center_1 = hypotenuse(x_1, y_1)
    distance_to_center_2 = hypotenuse(x_2, y_2)
    if distance_to_center_1 <= distance_to_center_2:
        print(f"({int(x_1)}, {int(y_1)})({int(x_2)}, {int(y_2)})")
    else:
        print(f"({int(x_2)}, {int(y_2)})({int(x_1)}, {int(y_1)})")
else:
    distance_to_center_1 = hypotenuse(x_3, y_3)
    distance_to_center_2 = hypotenuse(x_4, y_4)
    if distance_to_center_1 <= distance_to_center_2:
        print(f"({int(x_3)}, {int(y_3)})({int(x_4)}, {int(y_4)})")
    else:
        print(f"({int(x_4)}, {int(y_4)})({int(x_3)}, {int(y_3)})")