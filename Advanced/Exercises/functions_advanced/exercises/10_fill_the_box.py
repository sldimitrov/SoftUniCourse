from collections import deque


# Define a function
def fill_the_box(height, length, width, *args):
    space = height * length * width  # calculate the area

    boxes = deque(args)  # put arguments into a queue

    while True:
        box = boxes.popleft()  # popleft an argument

        if box == "Finish":  # break condition
            break  # if the arg is finish

        space -= box  # put the box in the free space | decrease the space

        if space < 0:  # if we run out of space
            boxes_left = sum(x for x in boxes if x != "Finish")  # calculate how much boxes are left

            # to the sum of boxes left
            boxes_left += abs(space)  # add the boxes that we tried to put in but there was not enough space

            return f"No more free space! You have {boxes_left} more cubes."

    return f"There is free space in the box. You could put {space} more cubes."


# Test Code
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
