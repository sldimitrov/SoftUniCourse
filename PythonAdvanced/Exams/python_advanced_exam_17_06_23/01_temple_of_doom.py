from collections import deque

# Read 3 following collections
tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

is_won = False

# Logic
while tools and substances:
    curr_tool = tools.popleft()
    curr_substance = substances.pop()

    result = curr_tool * curr_substance
    # make experiment with super methods
    if result in challenges:
        challenges.remove(result)
        if not challenges:
            is_won = True
    else:
        curr_tool += 1
        tools.append(curr_tool)
        curr_substance -= 1
        if curr_substance != 0:
            substances.append(curr_substance)

# Print User output
if is_won:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
elif not tools or not substances:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")
if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")
