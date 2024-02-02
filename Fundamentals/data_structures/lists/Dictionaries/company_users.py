# Initialise a dict to store company data in.
company_info = {}

# Initialise a While loop.
while True:
    command = input()
    # break condition
    if command == "End":
        break

    company, employee_id = command.split(" -> ")
    # add the company to the dict if it's not there
    if company not in company_info:
        company_info[company] = []
    # if the user id does not appear in the dict, append it
    if employee_id not in company_info[company]:
        company_info[company].append(employee_id)

# print name of the company
        # -- student ID
for name, students in company_info.items():
    print(f"{name}")
    for student in students:
        print(f"-- {student}")