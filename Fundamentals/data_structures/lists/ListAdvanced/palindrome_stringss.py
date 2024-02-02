def palindrome_word_check(word):
    if word == word[::-1]:
        return word

# Read User input
some_list = input().split()
palindrome_word = input()

palindrome_list = [word for word in some_list if palindrome_word_check(word)]
palindrome_counter = palindrome_list.count(palindrome_word)

print(palindrome_list)
print(f"Found palindrome {palindrome_counter} times")
