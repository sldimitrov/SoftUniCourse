from string import punctuation

with open('resources/text.txt', 'r') as read_text:
    text = read_text.readlines()

output_file = open("resources/output.txt", "w")

for row in range(len(text)):
    letters, punctuation_marks = 0, 0

    for s in text[row]:
        if s.isalpha():
            letters += 1
        if s in punctuation:
            punctuation_marks += 1

    output_file.write(f"Line {row + 1}: {''.join(text[row][:-1])} ({letters})({punctuation_marks})\n")