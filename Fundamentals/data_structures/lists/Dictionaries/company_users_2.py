# Initialise a dict to store the data
stored_data = {}

# Read User input
while True:
    command = input()
    if command == 'End': # break condition
        break
    company, employee = command.split(" -> ")

    if company not in stored_data:
        # Initialise a company space
        stored_data[company] = []

    if employee not in stored_data[company]:
        # adding employees into the company list
        stored_data[company].append(employee)

# Print User output
for company, employees in stored_data.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")