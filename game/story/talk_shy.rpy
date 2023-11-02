# ---------- SHY WORKER CONVERSATIONS ----------
label talk_shy:

    # Check remaining conversations and jump to appropriate label
    if w1.conversations == 2:
        jump shy_2
                
    elif w1.conversations == 1:
        jump shy_1
        
    else:
        jump shy_0



# ---------- 2 Conversations Remaining ----------

label shy_2:    
    show shy worried at center
    with dissolve

    menu:
        w1.c "Y... yes?"

        "How are you doing?":
            w1.c "I don't think I'm doing very well, at the moment..."

        "You don't believe it was me... right?":
            w1.c "I don't know what else to think... You were the one to find her."

    show shy cry at center        

    menu:
        w1.c "It's so hard to forget... her face was so..."

        "Console [w1.name]":
            w1.c "Thank you, [p.name]..."

        "It wasn't that bad. Not like she was left around to rot, it was still fresh.":
            jump shy_2_fail
    

    menu:
        w1.c "It's horrific. I don't know how you, or anyone, could have done that."

        "I don't know about 'horrific' - that's a pretty strong word.":
            jump shy_2_fail

        "Really? I could see why someone would, she was so rude!":
            jump shy_2_fail

        "That's exactly why I didn't do it. I could never.":
            jump shy_2_pass

label shy_2_fail:
    w1.c "I..."

    hide shy
    with dissolve

    "[w1.name] needs some space right now."

    $ w1.conversations -= 1
    $ p.conversations_had += 1

    jump conversations

label shy_2_pass:
    show shy worried at center

    w1.c "I want to believe you. It's just..."

    p.c "The odds are stacked against me? I know. Not exactly a good look."

    w1.c "Yeah... you understand. It's really hard to wrap my head around. I'm still so..."

    show shy cry at center

    "[w1.name] sobs uncontrollably. You give her a quick hug and move away as to give her some space. She needs some time right now."

    hide shy
    with dissolve

    $ w1.conversations -= 1
    $ p.evidence_collected += 1
    $ p.conversations_had += 1

    jump conversations



# ---------- 1 Conversation Remaining ----------

label shy_1:
    show shy worried at center
    with dissolve

    menu:
        w1.c "Hello again."

        "It's been a long day, huh?":
            w1.c "Extremely..."

        "Do you think I'm innocent now?":
            jump shy_1_fail

    show shy cry at center        

    menu:
        w1.c "Do you think we will get help soon?"

        "I think so. Those raccoons must be getting tired out there, by now.":
            show shy happy 1
            "She smiles lightly."

        "I really hope not... I'm afraid of what will happen next.":
            jump afraid

    menu:
        w1.c "If today hadn't gone how it had, I feel like you would have done really well here."

        "Thank you":
            p.c "Hearing that means a lot. It was a pleasure working with you, even for a day."
            jump shy_1_pass

        "Thank you, but...":
            p.c "I really don't think I enjoyed working here with you guys, so it probably wouldn't have worked out anyway."
            jump shy_1_fail

    menu afraid:
        w1.c "Why would you be afraid, [p.name]?"

        "Because, even if I prove my innocence to you all...":
            p.c "I know you'll all see me differently. I know I didn't do it... but even being in this situation right now has altered my life forever. If I could rewind time, I would."
            jump shy_1_pass

        "Because I know what you all think of me...":
            p.c "a monster."
            p.c "Even if you believe deep down that I didn't do it, there's still a stain on my reputation."
            jump shy_1_fail

        "Because...":
            p.c "You know... I don't think I can give you a valid reason, really."
            jump shy_1_fail
    
label shy_1_fail:
    show shy angry 1
    w1.c "Please leave me alone."

    hide shy
    with dissolve

    $ w1.conversations -= 1
    $ p.conversations_had += 1

    jump conversations

label shy_1_pass:
    show shy happy 2
    w1.c "I wish you the best of luck, [p.name]"

    hide shy
    with dissolve

    $ w1.conversations -= 1
    $ p.evidence_collected += 1
    $ p.conversations_had += 1

    jump conversations



# ---------- 0 Conversations Remaining ----------

label shy_0:
    jump conversations_refresh