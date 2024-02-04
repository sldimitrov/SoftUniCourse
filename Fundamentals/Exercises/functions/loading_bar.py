# Define a function
def loading_bar(some_number: int) -> str:
    if some_number != 100:
        percentages = some_number // 10
        return f"{some_number}% [{'%' * percentages}{'.' * (10 - percentages)}]\n" \
               f"Still loading..."
    return f"100% Complete!\n" \
           f"[{'%' * 10}]"


# Read User inputs
single_number = int(input())

# Print the function's result
print(loading_bar(single_number))
