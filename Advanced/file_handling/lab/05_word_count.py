import os

# Save the data in each file
words_file = "words.txt"
text_file = "text.txt"

path = os.path.join("resources", words_file)

words_dictionary = {}

with open(path, "w") as f:

    searched_words = input("Searched words: ")

    for word in searched_words.split():
        if word not in words_dictionary.keys():
            words_dictionary[word] = 0

    f.write(searched_words)

path = os.path.join("resources", text_file)
with open(path, "a") as f:
    f.write(input("Text: "))

with open(path, "r") as f:
    text = f.readline().split('-')

    for line in text:
        line = line.strip()
        for word in line.split():
            if word.lower() in words_dictionary.keys():
                words_dictionary[word] += 1

[print(f"{key} - {value}") for key, value in words_dictionary.items()]