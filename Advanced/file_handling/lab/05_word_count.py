import os

text_path = os.path.join("resources", "input.txt")
words_path = os.path.join("resources", "words.txt")

with open(text_path, "r") as file:
    text = file.read().lower()

with open(words_path, "r") as file:
    searched_words = file.read().split()
    searched_words = [word.lower() for word in searched_words]

count_of_s_words = {}

for searched_word in searched_words:
    number_of_appearance = text.count(searched_word)
    if searched_word not in count_of_s_words.keys():
        count_of_s_words[searched_word] = 0
        count_of_s_words[searched_word] += number_of_appearance


[print(f"{key} - {value}") for key, value in sorted(count_of_s_words.items())]