from tkinter import Button, Entry

from Advanced.Projects.gui_shop.helpers import clean_screen
from canvas import root, frame


def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg="green",  # background color
        fg="white",  # font color
        bd=0,
        width=7,
        height=2,
        command=register,
    )

    login_button = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        bd=0,
        width=6,
        height=2,
        command=login,
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 305, window=login_button)


def register():
    clean_screen()

    frame.create_text(100, 50, text="First name:")
    frame.create_text(100, 100, text="Last name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    print("Register")


def login():
    clean_screen()

    frame.create_text(100, 50, text="First name:")
    frame.create_text(100, 100, text="Last name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)  

    print("Login")


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0)
