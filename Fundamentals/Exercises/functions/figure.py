def square(a, b):
    result = a * b
    return result


def rectangle(a, b):
    result = (a * b) / 2
    return result


def circle(r):
    result = 3.14159265 * (r * r)
    return result


print('Hello, we are here to solve your problem.')
print('If you want calculate the area of any figure of the belows')
print('First input the figure and then the following parameter/s on single lines')
print(' ')
print('square : a, b')
print('rectangle : a, b')
print('circle : radius')
figure_i = input()
if figure_i == 'square':
    width = int(input())
    height = int(input())
    result = square(width, height)
elif figure_i == 'rectangle':
    width = int(input())
    height = int(input())
    result = rectangle(width, height)
elif figure_i == 'circle':
    radius = int(input())
    result = circle(radius)

print(result)
