# Read User input
events = input().split('|')
for event in events:
    event_items = event.split('-')
    event_name = event_items[0]
    event_value = int(event_items[1])
    print(event_name, event_value)
# Logic

# Print User output