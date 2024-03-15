
def start_playing(inst):
    return inst.play()


class Children:

    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))
