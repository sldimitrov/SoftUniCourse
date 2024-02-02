# Define a function
def palindrome_strings(words: list, special: str):
    palindrome_list = []
    counter = 0
    for word in words:
        reverse_word = ''
        for letter in word[::-1]:
            reverse_word += letter
        if reverse_word == word:
            palindrome_list.append(word)
            if word == palindrome:
                counter += 1

    return palindrome_list, counter

# Read User input
word_list = input().split()
palindrome = input()
out_list, count = palindrome_strings(word_list, palindrome)
print(out_list)
print(f"Found palindrome {count} times")