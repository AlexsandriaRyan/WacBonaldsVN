label talk_shy:
    if w1.conversations == 2:
        "2: [w1.name] has [w1.conversations] remaining"

    elif w1.conversations == 1:
        "1: [w1.name] has [w1.conversations] remaining"

    else:
        "0: [w1.name] has [w1.conversations] remaining"