def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{value}, {key}")


greet_me(Peter="Hello", George="Bye")
