# Define a function
def grades(grade: float):
    """
        This function takes a grade argument,
        evaluates you on the base of the grade
        and gives you a mark.
        -
        Parameters: float(student's grade)
        -
        It Returns: str(your mark)
    """
    if 2 <= grade <= 2.99:
        return 'Fail'
    elif 3 <= grade <= 3.49:
        return 'Poor'
    elif 3.5 <= grade <= 4.49:
        return 'Good'
    elif 4.5 <= grade <= 5.49:
        return 'Very Good'
    elif 5.5 <= grade <= 6:
        return 'Excellent'


# Read User input
grade = float(input())

# Call the function and print its result
print(grades(grade))




