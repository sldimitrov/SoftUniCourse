# Define function
def calculate_rectangle_area(width: int, height: int):
    """
    This function calculates the area of
               an rectangle

    Parameters: width: int, height: int

    It returns the area(int)
    """
    result = width * height
    return result
# Read User input
width = int(input())
height = int(input())

print(calculate_rectangle_area(width, height))
# Call the function and print its result