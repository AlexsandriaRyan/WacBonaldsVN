label talk_mean:
    if w3.conversations == 3:
        "3: [w3.name] has [w3.conversations] remaining"

    elif w3.conversations == 2:
        "2: [w3.name] has [w3.conversations] remaining"


    elif w3.conversations == 1:
        "1: [w3.name] has [w3.conversations] remaining"

    else:
        "0: [w3.name] has [w3.conversations] remaining"