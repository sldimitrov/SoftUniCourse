def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{value}, {key}")


greet_me(Peter="Hello", George="Bye")
greet_me(b=1, a=2, d=3, c=4)