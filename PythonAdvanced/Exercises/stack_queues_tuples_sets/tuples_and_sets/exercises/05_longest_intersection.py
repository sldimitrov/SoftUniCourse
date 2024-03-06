# Read User input
n_lines = int(input())

collection = [input().split('-') for x in range(n_lines)]

biggest_intersection = []

# Logic
for each_list in collection:
    first_set = set()
    second_set = set()

    lower_f, upper_f = each_list[0].split(',')
    lower_s, upper_s = each_list[1].split(',')

    lower_f, upper_f = int(lower_f), int(upper_f)
    lower_s, upper_s = int(lower_s), int(upper_s)

    for c in range(lower_f, upper_f + 1):
        first_set.add(c)

    for c in range(lower_s, upper_s + 1):
        second_set.add(c)

    if len(first_set & second_set) > len(biggest_intersection):
        biggest_intersection = first_set & second_set

# Print User output
print(f"Longest intersection is"
      f" [{', '.join([str(x) for x in biggest_intersection])}]"
      f" with length {len(biggest_intersection)}")