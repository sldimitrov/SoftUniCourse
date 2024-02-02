names = ['ivan', 'pesho', 'dragan']

capitalized_names = map(str.capitalize, names)
upper_names = map(str.upper, names)

# We should add list in the front unless we want to receive:
#         <map object at 0x000001A957D3EBF0>

# In fact we can skip this part and print them in a for loop
for name in capitalized_names:
    print(name,end=' ')

# for readability
print()

print(list(upper_names))



