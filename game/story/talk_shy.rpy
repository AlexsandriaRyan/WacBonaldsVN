label talk_shy:
    if w1.conversations == 2:
        jump shy_2
                
    elif w1.conversations == 1:
        jump shy_1
        
    else:
        jump shy_0

label shy_2:
    "[w1.name] has [w1.conversations] remaining"
    
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
    $ w1.conversations -= 1

    return

label shy_2_pass:
    show shy worried at center

    w1.c "I want to believe you. It's just..."

    p.c "The odds are stacked against me? I know. Not exactly a good look."

    w1.c "Yeah... you understand. It's really hard to wrap my head around. I'm still so..."

    show shy cry at center

    "[w1.name] sobs uncontrollably. You give her a quick hug and move away as to give her some space. She needs some time right now."

    $ w1.conversations -= 1
    $ p.evidence_collected += 1

    return

label shy_1:
    "1: [w1.name] has [w1.conversations] remaining"

    return

label shy_1_fail:
    $ w1.conversations -= 1

    return

label shy_1_pass:
    $ w1.conversations -= 1
    $ p.evidence_collected += 1

    return

label shy_0:
    "0: [w1.name] has [w1.conversations] remaining"

    return