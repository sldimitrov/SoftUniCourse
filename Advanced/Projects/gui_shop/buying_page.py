from PIL import ImageTk, Image

from helpers import clean_screen
from json import load

from Advanced.Projects.gui_shop.canvas import frame


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    with open("db/products.json", "r") as stock:
        info = load(stock)

    x, y = 150, 50

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))
        images.append(item_img)  # keeping the reference to the image so tkinter
        # does not delete it after the function ends

        frame.create_text(x, y, text=item_name)
        frame.create_image(x, y + 100, image=item_img)

        x += 200

        if x >= 550:
            y += 270
            x = 150


images = []

