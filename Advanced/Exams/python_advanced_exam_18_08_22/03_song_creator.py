# Define the function
def add_songs(*songs_info):
    # Initialise a dictionary
    playlist = {}

    # Sort the given data into the dictionary
    for song in songs_info:
        song_name, lyrics = song[0], song[1]
        if song_name not in playlist:
            playlist[song_name] = []
        if lyrics:
            playlist[song_name].append(lyrics)

    # Initialise a list for the return
    result = []

    # Append songs and their lyrics
    for current_song in playlist.items():
        name, lyrics = current_song[0], current_song[1]
        result.append(f"- {name}")
        if lyrics:
            for line in lyrics:
                result.append('\n'.join(line))

    return '\n'.join(result)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))

