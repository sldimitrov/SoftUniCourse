import os
import re

words_path = os.path.join("resources", "words.txt")
text_path = os.path.join("resources", "input.txt")
output_file_path = os.path.join("resources", "output.txt")

with open(words_path) as f:
    words_as_string = f.read()
    searched_words = [word.lower() for word in words_as_string.split()]

with open(text_path) as f:
    content = f.read().lower()

words_count = {}

for searched_word in searched_words:
    pattern = re.compile(rf"\b{searched_word}\b")
    result = re.findall(pattern, content)
    words_count[searched_word] = len(result)

sorted_dictionary = sorted(words_count.items(), key=lambda kvp: -kvp[1])

with open(output_file_path, "a") as f:
    for word, count in sorted_dictionary:
        f.write(f"{word} - {count}\n")

