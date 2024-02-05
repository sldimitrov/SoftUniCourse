import random
import time
import pyttsx3

# TODO: 1
# fix the info
# fix the input mistake within the menu * input = 'anything else', for example throws and error


class TextToSpeech:
    """
    The functionality that this class applies to the project is that it open the dictionary
    file and read every sentence from it. The idea behind this is to train listening and
    to hear the new words more often.
    """
    engine: pyttsx3.Engine

    def __init__(self, voice, rate: int, volume: float):
        """
        The function initializes a text-to-speech engine with specified voice, rate, and volume properties.

        :param voice: The "voice" parameter is used to specify the voice that the text-to-speech engine should use.
        It can be a string representing the name of the voice, or it can be set to None to use the default voice.
        :param rate: The "rate" parameter determines the speed at which the text is spoken. It is measured in words per
        minute (wpm). A higher rate value will result in faster speech, while a lower rate value will result in slower
        speech.
        :type rate: int
        :param volume: The "volume" parameter is used to control the volume of the voice output.
        It is a float value between 0.0 and 1.0, where 0.0 represents the lowest volume (mute)
        and 1.0 represents the highest volume
        :type volume: float
        """
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def list_available_voices(self):
        """
        The function "list_available_voices" prints the name, age, and ID of each available voice.
        It is written in case you want to change the speaker. If you want to you should call the function once
        and then copy the ID of the person you'd like to speak.
        """
        voices: list = [self.engine.getProperty('voices')]

        for i, voice in enumerate(voices[0]):
            print(f'{i + 1} Name : {voice.name},  Age : {voice.age}, ID : [{voice.id}]')

    def text_to_speech(self, text: str, save: bool = False, file_name='output.mp3'):
        self.engine.say(text)

        if save:
            self.engine.save_to_file(text, file_name)

        self.engine.runAndWait()
        return True


def text_to_speech():
    """
    The function `text_to_speech` reads sentences from a file, and if there are any sentences, it converts them to
    speech using the specified voice and settings. If there are no sentences in the file, it prints a message
    indicating that there are no sentences.
    """
    tts = TextToSpeech('HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0',
                       200, 1.0)
    # tts.list_available_voices()
    f = open('sentences_list.txt', 'r')
    data = f.read()
    if data:
        counter = 1
        data = data.split('\n')
        data = [x for x in data if x != '']
        print('Listen...')
        for sentence in data:
            if sentence:
                tts.text_to_speech(sentence)
                print(f'({counter}/{len(data)})')
                time.sleep(3)
                counter += 1
        print('These were all of your sentences!')
    else:
        print('There are not any sentences written yet.')


def write_sentences() -> bool:
    """
    The function `write_sentences` reads words and their definitions from a text file,
    prompts the user to enter sentences related to each word, saves the sentences into
    a separate text file, and saves the words and their definitions into a dictionary.
    :return: a boolean value `True`.
    """
    lines = []

    # Read the data from the text file and append it into a list
    data = open('list_of_words.txt', 'r')
    for d in data:
        if '\n' in d:
            d = d.replace('\n', '')
        lines.append(d)

    words_dictionary = {}
    sentences = []
    if lines:
        for line in lines:
            if line:  # if it's not a blank line
                # Split the line by ("-") in order to get the word and its definition
                word, definition = line.split('-')
                print(f'\nWord or a phrase found: {word}')
                print(f'Definition: {definition}')

                # Collect sentences into a list
                sentence = input('Show imagination: ')
                sentences.append(sentence)
                print('Sentence saved successfully')

                # Save the word with its definition into a dictionary
                words_dictionary[word] = definition

                # Remove the written words from the (words text file)
                f = open('./list_of_words.txt', 'r')
                text = f.read()
                text = text.replace(line, '')
                f.close()
                f = open('./list_of_words.txt', 'w')
                f.write(text)
                f.close()
                print()
    else:
        print('There are not any new words.')

    # Save the sentences into a text file
    file = open('./sentences_list.txt', 'a')
    file.write('\n')
    file.write('\n'.join(sentences))
    file.close()

    # Save the words and their definitions into the dictionary
    file = open('./dictionary.txt', 'a')
    for key, value in words_dictionary.items():
        file.write(f'{key} - {value}\n')
    file.close()
    return True


def access_dictionary() -> bool:
    """
    The function `access_dictionary` reads a file called "dictionary.txt" and checks if it contains any words, returning
    True if it does and printing the line if they are alphabetical.
    :return: a boolean value.
    """
    f = open('./dictionary.txt', 'r')
    data = f.read()
    if data:
        print("\nAll the words that are in the dictionary:")
        for line in data:
            if line.isalpha():
                print(data)
                f.close()
                return True
    else:
        print('\nThere are not any words in the dictionary.')
        return True


def show_new_words() -> bool:
    """
    The function `show_new_words` reads a file called "list_of_words.txt" and prints all the alphabetic characters in
    the file, indicating that they are new words. If there are no new words, it prints a message indicating that the
    list is empty.
    :return: a boolean value.
    """
    f = open('./list_of_words.txt', 'r')
    data = f.read()
    for _ in data:
        if _.isalpha():
            print('\nList of all new words:')
            print(data)
            f.close()
            return True
    else:
        print('There are not any new words.')   # ADD A OPERATION - ADDING NEW WORDS WHEN THE LIST IS EMPTY
        return True


def test_knowledge():
    """
    The function `test_knowledge()` allows the user to play a game where they are given a word and they have to provide
    its definition.
    :return: The function `test_knowledge` returns a boolean value `True`.
    """
    data = open('dictionary.txt', 'r')   # Open the text file
    lines = []
    # Remove all the new lines from the data in order to save each line in a list
    # Save the data into a list
    for d in data:
        if '\n' in d:
            d = d.replace('\n', '')
        if d:
            lines.append(d)
    if lines:
        # Let the User to choose a game type
        print('Here you will be able to check your knowledge.\n'
              'Please choose a game-type\n'
              '(s) for a short one\n'
              'and (l) for a longer one'
              '...')
        answer = input()
        if answer == 's':
            n = 10
        elif answer == 'l':
            n = 20
        else:
            print('Error: Invalid Input')
            return True

        # Choose a random word from the list and ask the user for its definition
        points = 0
        bad_words = []
        for _ in range(n):
            number = random.randint(0, len(lines) - 1)
            line = lines[number]
            word, definition = line.split('-')
            print(f'\nThe given words is: {word}')
            _back = input('What is the definition?: ')

            print(f'\nThe definition is: {definition}')
            signal = input('Did you answer correctly? (y/n): ')
            if signal.lower() == 'y':
                points += 1
                print('+1 point')
            elif signal.lower() == 'n':
                bad_words.append(line)

        if answer == 's':
            if points <= 3:
                print('\nYou still have much to learn, buddy!\n'
                      f'Points: {points}:10')
            elif 3 < points <= 5:
                print('\nYou are in the middle gold, motivate yourself to do better!\n'
                      f'Points: {points}/10')
            elif 5 < points <= 8:
                print('\nGood job! Keep learning!\n'
                      f'Points: {points}/10')
            elif 8 < points <= 10:
                print('\nExcellent!\n'
                      f'Points: {points}/10')

        elif answer == 'l':
            if points <= 6:
                print('\nYou still have much to learn, buddy!\n'    
                      f'Points: {points}/20')
            elif 6 < points <= 10:
                print('\nYou are in the middle gold, motivate yourself to do better!\n' 
                      f'Points: {points}/20')
            elif 10 < points <= 16:
                print('\nGood job! Keep learning!\n'
                      f'Points: {points}/20')
            elif 16 < points <= 20:
                print('\n'
                      'Excellent! -------\n'              
                      f'Points: {points}/20\n'
                      f'------------------')
        else:
            print('Wrong game-type inputted')
            return True
        return True

    else:   # No words in the dictionary:
        print('There are not any words in your dictionary.')
        menu()


def show_info():
    """
    The function "show_info" returns a message that provides an overview of the program and its purpose.
    :return: string (info)
    """
    message = '\tEverything you need to know\n' \
              'This program was born in my head and it was implemented into code by my own hands.\n\n' \
              '  The mission:\n' \
              'To help others. Learning never stops and it makes us better humans. This is the main purpose,\n' \
              'for which I managed to create something, that will help us to be and earn more!\n\n' \
              '  How to use it?\n' \
              'Everything in this program is separated into sections.\n' \
              ' Let\'s say that you\'d just inputted the words, that you want to write\n' \
              'into the (list of words txt) - This is when you want to choose (1)\n' \
              ' On the other hand, when you had already used this program at least once.\n' \
              'You\'re not sure which words you have in your text file, choose (2) and find out.\n'\
              ' Moreover, if you want to see which words you have already learned input (3)\n' \
              ' Within the forth operation (4) you are not only going to learn. You\'re going to be challenged!\n' \
              'Choose it and go and face your demons or stay the same forever!\n' \
              ' (5) is what you had already chosen, so I believe it does not need any explanation\n' \
              ' If information is all you needed at this point choose (6) to exit the temple.\n' \
              'I will be waiting for your return, because I hope that your learning will be an endless process!'
    return message


def menu() -> str:
    """
    The `menu` function returns a string containing a user menu with several options.
    :return: a string that contains the user menu options.
    """
    menu_message = ('Please, choose an operation (1/2/3/4/5/6):\n'
                    '1. See the new words\n'
                    '2. Write down some sentences\n'
                    '3. Open the dictionary\n'
                    '4. Test your knowledge\n'
                    '5. Listen to the written sentences\n'
                    '6. Info\n'
                    '7. Exit the program')
    return menu_message


# This and the other 2 functions below are responsible for the input
def get_input() -> str:
    """
    When called: This function prints out a message, which asks the user to input a single number.
    Then: Checks if user's input is valid by calling the (input validator) function and if its not -
    calls out the (handle invalid input) which prints out an error message.
    :return: str
    """
    while True:
        choice = input('\nChoose operation (1/2/3/4/5/6/7) or (m) if you want to see the menu: ')
        if choice is input_validator(choice):
            print(handle_invalid_input(choice))
        else:
            return choice


# Define a function
def input_validator(message: str):
    """
    This functions checks if the choice of the user occurs in the valid list of answers
    If not: the (handle invalid input) func. is being called.
    :param message: str
    :return: str / bool
    """
    valid_answers = [1, 2, 3, 4, 5, 6, 7]
    if message not in valid_answers:
        message = handle_invalid_input(message)
        return message
    return True


# Define a function
def handle_invalid_input(some_input: str):
    """
    Returns an error message every time it is called
    :param some_input: str
    :return: str
    """
    return f'Error: {some_input} is an invalid input\n'


def main():
    """
    The main function contains the functionalities of the entire program and
    calls other functions based on the user's choice.
    """
    print(menu())
    choice = get_input()
    while True:
        if choice == 'm':
            main()
        choice = int(choice)
        if choice == 1:
            show_new_words()
        elif choice == 2:
            write_sentences()
        elif choice == 3:
            access_dictionary()
        elif choice == 4:
            test_knowledge()
        elif choice == 5:
            text_to_speech()
        elif choice == 6:
            print(show_info())
        choice = get_input()


# Welcoming message
print(' Hello, Learner!\n'
      'Are you ready to dive into a world fulfilled with new words and meanings?\n')

if __name__ == '__main__':
    main()

# Greetings for an end
print('\nThank yourself for the time you spent learning!\n'
      'I am so happy that you just used my program!\n'
      'If you had seen any bugs or if you have any ideas\n'
      'how I should improve my app, please mail me here:\n'
      ' -slavidimitrov54@gmail.com\n'
      ' ' * 29, 'Best wishes,\n'
      ' ' * 29, 'SD')
