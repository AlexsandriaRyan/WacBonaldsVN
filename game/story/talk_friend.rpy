# ---------- FRIEND WORKER CONVERSATIONS ----------

label talk_friend:
    # Check remaining conversations and jump to appropriate label
    if w4.conversations == 3:
        jump friend_3

    elif w4.conversations == 2:
        jump friend_2
                
    elif w4.conversations == 1:
        jump friend_1
        
    else:
        jump friend_0



# ---------- 3 Conversations Remaining ----------

label friend_3:
    show friend normal at center

    menu:
        w4.c "So? How goes proving your innocence?"

        "Good!":
            show friend happy at center
            w4.c "Glad to hear it!! You're going to need all the help you can get!"

        "Not so good.":
            show friend worried 1 at center
            w4.c "I kinda figured..."

        "As long as you think I'm innocent!":
            show friend worried 1 at center
            w4.c "... yeah! Totally!"

    p.c "What's that supposed to mean?"

    show friend surprised at center
    show friend worried 1 at center
    with dissolve

    w4.c "Hahaha! Nothing at all!"

    menu:
        w4.c "It's just..."

        "Just what?":
            jump friend_3_fail

        "It's cool.":
            jump friend_3_pass


label friend_3_fail:
    show friend surprised at center
    
    w4.c "Passive aggressive, are we?"

    show friend angry 1 at center

    w4.c "I don't think you get it."
    w4.c "If you didn't do it, someone in this room must have done it."

    show friend angry 3 at center

    w4.c "Even though I know you didn't do it..."
    w4.c "... saying otherwise might make me look guilty."

    hide friend
    with dissolve

    p.c "Wait, [w4.name] would throw me under the bus, even thought I didn't do it???"
    p.c "So much for friends having each others' backs. I'd better make sure I'm innocent..."

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w4.conversations == 3:
        $ w4.conversations -= 1
        $ p.conversations_had += 1

    jump conversations


label friend_3_pass:
    p.c "I know it's hard to fully picture me as 'innocent' when I quite literally found the manager dead."

    show friend worried 1 at center

    w4.c "Yeah, that's kinda hard to come back from that, huh?"
    
    show friend normal at center

    w4.c "If it makes you feel any better, I know you didn't do it."
    w4.c "Remember, friends have each others' backs!"

    hide friend
    with dissolve

    p.c "[w4.c] really likes that saying, huh? She must see me as a very good friend already!"

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w4.conversations == 3:
        $ w4.conversations -= 1
        $ p.conversations_had += 1
        $ p.innocence += 1

    jump conversations



# ---------- 2 Conversations Remaining ----------

label friend_2:
    show friend happy at center
    with dissolve

    w4.c "Hey, bestie!!!"

    show friend normal at center
    
    menu:
        w4.c "How's your innocence coming?"

        "Not so good...":
            show friend worried 1 at center
            "Awww, poor [p.name]."
            show friend happy at center
            w4.c "I'm sure it'll at work out!"

        "Could be better.":
            show friend happy at center
            w4.c "Good!"
            p.c "What?"
            show friend worried 2 at center
            w4.c "Didn't you hear me? I said, 'not good'."
            w4.c "That sucks to hear, [p.name]."
            
        "I don't think anyone believes it was me!":
            show friend angry 3 at center
            w4.c "Is that right... they must be suspecting someone else, then."
            show friend happy at center
            w4.c "I'm so glad for you!"

        "How should I know???":
            p.c "Alex didn't put a darn innocence counter on this darned game."
            w4.c "Well, duh! If she did, you wouldn't have much mystery, huh?"

    p.c "Either way, I'm sure we'll find out who really did it."

    show friend normal at center

    menu:
        w4.c "And what do you plan to do, once you find them out?"

        "Turn them in, of course.":
            jump friend_2_fail

        "Let them go, of course.":
            jump friend_2_pass

        "Kill them, of course.":
            jump friend_2_fail_kill

label friend_2_fail:
    show friend angry 3 at center

    w4.c "Why would you do that?! For all we know, the manager's death was a mistake."
    w4.c "Turning someone in could be a mistake, too."

    show friend normal at center
    w4.c "Do you understand, [p.name]?"

    "You nod, hesitantly."

    show friend happy at center
    w4.c "You just get me! I'm so glad we're friends!"

    hide friend
    with dissolve

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w4.conversations == 2:
        $ w4.conversations -= 1
        $ p.conversations_had += 1

    jump conversations


label friend_2_fail_kill:
    show friend angry 3 at center

    w4.c "ARE YOU CRAZY?"
    w4.c "After proving your innocence, you'd want to commit murder after all?!"
    w4.c "Jeez, you may as well have killed the manager yourself."
    w4.c "DON'T lay a hand on the person who did it!!!"
    w4.c "For all WE know, the manager's death was a mistake!!!"

    hide friend
    with dissolve

    "You had to walk away. Ain't no consoling [w4.name] when she's like this."

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w4.conversations == 2:
        $ w4.conversations -= 1
        $ p.conversations_had += 1
        p.crazy = True

    jump conversations

label friend_2_pass:

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w4.conversations == 2:
        $ w4.conversations -= 1
        $ p.conversations_had += 1
        $ p.innocence += 1



# ---------- 1 Conversation Remaining ----------

label friend_1:

label friend_1_fail:

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w4.conversations == 1:
        $ w4.conversations -= 1
        $ p.conversations_had += 1

label friend_1_pass:

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w4.conversations == 1:
        $ w4.conversations -= 1
        $ p.conversations_had += 1
        $ p.innocence += 1



# ---------- 0 Conversations Remaining ----------

label friend_0:
    jump conversations_refresh