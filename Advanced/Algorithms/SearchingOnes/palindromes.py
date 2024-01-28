def is_palindrome(word):

    idx = len(word) // 2

    index = 0
    while index < idx:
        if word[index] != word[-index-1]:
            return False
        index += 1
    return True


print(is_palindrome('abbcbba'))
print(is_palindrome('abKOba'))




