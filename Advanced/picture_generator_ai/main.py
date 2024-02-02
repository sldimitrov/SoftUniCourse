import tkinter as tk
import json
import urllib.request
import requests

from io import BytesIO
from PIL import ImageTk, Image


def display_image(image_url: str) -> None:
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()

    image_stream = BytesIO(image_data)
    image = ImageTk.PhotoImage(Image.open(image_stream))

    image_label.config(image=image)
    image_label.image = image


def get_image_url() -> str:
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjYxY2QzZDgtYjUxZC00Zjk5LWE5M2QtODdjYTczMWE4NDFhIiwidHlwZSI6ImFwaV90b2tlbiJ9.v8xe6QW2UlfDRL3k77Ls9dMJx-7BcP5icEyMuXo1Dk8"
    }

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),
        "resolution": "256x256",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)

    return result['openai']['items'][0]["image_resource_url"]


def render_image():
    print('clicked')

    try:
        error_label.place_forget()
        image_url = get_image_url()
    except KeyError:
        error_label.place(x=175, y=50)
    else:
        display_image(image_url)


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
image_label.place(x=123, y=50)

generate_button = tk.Button(window, text="Create", height=1, command=render_image)
generate_button.place(x=270, y=317)

# Keeps the window alive
window.mainloop()
