# Creating class Party
class Party:
    def __init__(self):
        self.people = []


# Create an instance of the class
party = Party()

name = input()
# Initializing a while loop
while name != "End":
    party.people.append(name)
    name = input()

# Print the output
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")