version = input()
version_int = version.replace(".", "")
new_version = int(version_int) + 1
print(".".join(str(new_version)))
