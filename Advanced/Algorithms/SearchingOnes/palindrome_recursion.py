# Define a function
def palindrome(word, idx):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"

    if word[idx] != word[-idx-1]:
        return f"{word} is not a palindrome"

    return palindrome(word, idx + 1)


# Test Code
print(palindrome("abcba", 0))
print(palindrome("peter", 0))