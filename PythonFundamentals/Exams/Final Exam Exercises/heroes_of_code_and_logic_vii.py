# Initialise a dictionary to store the data
data = {}

# Read User input
n = int(input())
for _ in range(n):
    name, HP, MP = input().split()
    data[name] = {'HP': int(HP), 'MP': int(MP)}

# Initialise a while loop
while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    action = command[0]

    # max MP(mana) - 200 ; max HP - 100;
    if action == 'CastSpell':
        hero, MP_needed, spell_name = command[1], command[2], command[3]
        if data[hero]['MP'] >= int(MP_needed):
            data[hero]['MP'] -= int(MP_needed)
            print(f"{hero} has successfully cast {spell_name} and now has {data[hero]['MP']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif action == 'TakeDamage':
        hero, damage, attacker = command[1], command[2], command[3]
        data[hero]['HP'] -= int(damage)
        if data[hero]['HP'] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {data[hero]['HP']} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            data.pop(hero)

    elif action == 'Recharge':
        hero, amount = command[1], command[2]
        added = int(amount)
        substring = data[hero]['MP']
        data[hero]['MP'] += int(amount)
        if data[hero]['MP'] > 200:
            data[hero]['MP'] = 200
            added = 200 - int(substring)
        print(f"{hero} recharged for {added} MP!")

    elif action == 'Heal':
        hero, amount = command[1], command[2]
        added = int(amount)
        substring = data[hero]['HP']
        data[hero]['HP'] += int(amount)
        if data[hero]['HP'] > 100:
            data[hero]['HP'] = 100
            added = 100 - int(substring)
        print(f"{hero} healed for {added} HP!")

for hero, info in data.items():
    print(hero)
    print(f"  HP: {info['HP']}")
    print(f"  MP: {info['MP']}")