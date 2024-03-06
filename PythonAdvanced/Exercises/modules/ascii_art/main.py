import pyfiglet


text = input()
while text != 'Stop':
    result = pyfiglet.figlet_format(text, font = "doh")
    print(result)
    text = input()
