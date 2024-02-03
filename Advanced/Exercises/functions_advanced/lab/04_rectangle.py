# Define a function
def rectangle(length, width):
    # Check if both params are int, else : error
    if not (isinstance(length, int) and isinstance(width, int)):
        return "Enter valid values!"

    # Define an inner function
    def area():
        return length*width

    # Define a nested function
    def perimeter():
        return 2*(length+width)

    # Calling the 2 inner functions within the f.form., returns a message
    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


# Call the main function and print out the returned message
print(rectangle(2, 10))
