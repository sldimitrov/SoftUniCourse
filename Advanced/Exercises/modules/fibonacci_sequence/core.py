
def create_seq(n):
    # Create the sequence
    sequence = [0, 1]
    # Logic
    for i in range(n - 2):
        # Get the next element
        element = sequence[-1] + sequence[-2]
        # Append the element to the sequence
        sequence.append(element)

    return sequence


def locate(el: int, sequence: list):
    if el in sequence:
        return f"The number {el} is at index {sequence.index(el)}"
    else:
        return f"The number {el} is not in the sequence"
