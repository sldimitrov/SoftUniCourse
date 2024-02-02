a = ["tim", "bob", "anna", "steve", "john","aaaaa","zzza"]
a = sorted(a, key = lambda x:(x[-1], len(x),x))
print(a)