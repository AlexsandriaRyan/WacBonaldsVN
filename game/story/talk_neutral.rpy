# ---------- NEUTRAL WORKER CONVERSATIONS ----------

label talk_neutral:
    # Check remaining conversations and jump to appropriate label
    if w2.conversations == 2:
        jump neutral_2

    elif w2.conversations == 1:
        jump neutral_1

    else:
        jump neutral_0

# ---------- 2 Conversations Remaining ----------

label neutral_2:
    show neutral normal at center

    "[w2.name] is busy playing on his phone. He doesn't seem to notice you."

    menu:
        "Tap his shoulder.":
            show neutral angry 2
            w2.c "What?"

        "Whisper in his ear, imitating a the ghost of a dead cat.":
            show neutral angry 2
            w2.c "What's wrong with you???"
            jump neutral_2_fail

        "Sit across from him and wait patiently.":
            w2.c "Hi, [p.name]. What do you want?"

    p.c "I was wondering how you're holding out?"

    show neutral angry 2

    menu:
        w2.c "I really don't care to share my emotions with you, right now."

        "That's ok, I understand.":
            jump neutral_2_pass

        "But you don't think I did it, right?":
            p.c "I just really, REALLY gotta know."
            jump neutral_2_fail


label neutral_2_fail:
    #$ renpy.fix_rollback()

    show neutral angry 2
    w2.c "Leave me be, please."

    hide neutral
    with dissolve

    "[w2.name] turns away from you, shifting his attention to his phone."

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w2.conversations == 2:
        $ w2.conversations -= 1
        $ p.conversations_had += 1
    
    jump conversations

label neutral_2_pass:
    #$ renpy.fix_rollback()

    show neutral normal at center
    w2.c "Thank you for respecting my privacy."

    hide neutral
    with dissolve

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w2.conversations == 2:
        $ w2.conversations -= 1
        $ p.conversations_had += 1
        $ p.innocence += 1

    jump conversations
    



# ---------- 1 Conversations Remaining ----------    

label neutral_1:
    show neutral normal at center
    with dissolve
    
    menu:
        w2.c "Can I help you?"

        "I wanted to thank you.":
            w2.c "What for?"
            
            p.c "For holding back [w3.name]. He was going to hurt me if you hadn't intervened."

            w2.c "Oh, that. I really don't care what he does to you, honestly. I just didn't want to make the situation worse."

        "Please tell me you don't think it was me!":
            w2.c "I really don't care if you did. They'll find a new manager eventually. It's none of my business."

    p.c "You don't seem to care about a lot, huh?"

    w2.c "Why should I? I show up for my job and go home. That's it."
    
    show neutral angry 2 at center

    menu:
        w2.c "I just want to go home."

        "Don't we all?":
            jump neutral_1_fail

        "What's at home?":
            show neutral normal at center
            w2.c "My cats."
            $ p.cat = True

    p.c "You didn't strike me as a cat person! How many?"

    menu:
        w2.c "Twelve and a half."

        "I can only imagine the smell.":
            jump neutral_1_fail

        "And a half...?":
            show neutral happy at center
            w2.c "Oh, yeah, Carl. He was hit by a car last month, so I had his better-looking half taxidermied."

        "Must have a big home for all those cats.":
            w2.c "Why are you so interested in my cats?"
            jump neutral_1_fail

    show neutral worried at center

    menu:
        w2.c "Although he is taxidermied, I miss him very much."

        "It's never the same after losing a fluffy friend.":
            jump neutral_1_pass

        "His half-body is probably haunted.":
            jump neutral_1_fail


label neutral_1_fail:
    #$ renpy.fix_rollback()

    show neutral angry 1 at center

    "[w2.c] looks you up and down, judgingly. He turns away from you and starts scrolling on his phone in boredom."

    hide neutral
    with dissolve

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w2.conversations == 1:
        $ w2.conversations -= 1
        $ p.conversations_had += 1

    jump conversations

label neutral_1_pass:
    #$ renpy.fix_rollback()

    show neutral happy at center

    w2.c "Carl would have liked to meet you, I think."

    hide neutral
    with dissolve

    p.c "[w2.name] is a lot weirder than I initially thought."

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w2.conversations == 1:
        $ w2.conversations -= 1
        $ p.conversations_had += 1
        $ p.innocence += 1

    jump conversations



# ---------- 0 Conversations Remaining ----------

label neutral_0:
    jump conversations_refresh