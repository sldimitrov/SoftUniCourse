from hashlib import sha256

from canvas import frame


def clean_screen():
    frame.delete("all")


def get_password_hash(password):
    hash_object = sha256(password.encode("UTF-8"))
    print(hash_object.hexdigest())


get_password_hash("hello")

