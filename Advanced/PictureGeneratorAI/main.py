import tkinter as tk
# import json
# import urllib.request
# import requests
#
# from io import BytesIO
# from PIL import ImageTK, Image


def display_image(image_url: str) -> None:
    pass


def get_image_url() -> str:
    pass


def render_image():
    pass


# Initialize the window
window = tk.Tk()

# The title
window.title("AI Image Generator")

# The size of the screen
window.geometry("500x350")  # width x height

error_label = tk.Label(window, text="Prompt cannot be empty!", fg="red")

input_field = tk.Entry(window, width=16)
input_field.place(x=165, y=320)

image_label = tk.Label(window)
image_label.place(x=123, y=70)

generate_button = tk.Button(window, text="Create", height=1, command=render_image)
generate_button.place(x=270, y=317)

# Keeps the window alive
window.mainloop()
