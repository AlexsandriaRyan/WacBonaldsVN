label talk_friend:
    if w4.conversations == 3:
        "3: [w4.name] has [w4.conversations] remaining"

    elif w4.conversations == 2:
        "2: [w4.name] has [w4.conversations] remaining"


    elif w4.conversations == 1:
        "1: [w4.name] has [w4.conversations] remaining"

    else:
        "0: [w4.name] has [w4.conversations] remaining"