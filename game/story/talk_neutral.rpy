# ---------- NEUTRAL WORKER CONVERSATIONS ----------

label talk_neutral:
    
    if w2.conversations == 2:
        "2: [w2.name] has [w2.conversations] remaining"

    elif w2.conversations == 1:
        "1: [w2.name] has [w2.conversations] remaining"

    else:
        "0: [w2.name] has [w2.conversations] remaining"