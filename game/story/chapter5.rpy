# * * * * * * * * * * CHAPTER 5  * * * * * * * * * *
# ---------- PREPARE FOR END GAME ----------

label chapter5:
    # at end, player will select who they think is the murderer

    scene black
    with fade

    # phone ring

    w2.c "... I'll get it."

    # phone ring stop

    w2.c "... Hello?"
    w2.c "... Really?"
    w2.c "... Yes that would be great."
    w2.c "... Ambulance? I think we're mostly okay, but there is a body that needs to be dealt with."
    w2.c "... I see."
    w2.c "... Yes, I think so."
    w2.c "... Of course. Thanks."

    scene restaurant
    with fade

    show neutral normal at right
    with moveinright
    w2.c "Guys, this is important. Listen up."
    
    show mean normal at left
    with moveinleft

    show shy normal at center
    with moveinleft

    w2.c "The police are on the way. It's been a long few hours, so we'll get out soon."
    w2.c "That said..."

    show neutral worried at left
    w2.c "There's an ambulance on the way for the manager's body."
    w2.c "We will also be questioned on who we think did it."

    show shy worried at center
    w1.c "I'm so nervous to talk to the police..."

    w3.c "I wouldn't worry too much about it. I think we all know who did it."

    w2.c "Just to be on the same page, DO we all know who did it?"

    hide shy
    with dissolve

    hide neutral
    with dissolve

    hide mean
    with dissolve

    menu:
        "I think it was..."

        "[w1.name]":
            jump accuse_w1

        "[w2.name]":
            jump accuse_w2

        "[w3.name]":
            jump accuse_w3

        "[w4.name]":
            jump accuse_w4

label accuse_w1:
    show shy surprised 1 at center
    with dissolve
    w1.c "... Huh?"

    show shy cry at center
    w1.c "I... how could you think that..."

    jump end

label accuse_w2:
    show neutral worried at center
    with dissolve
    w2.c "Wow... really...?"

    jump end

label accuse_w3:
    if p.mom:
        show mean cry 2 at center
        with dissolve
        w3.c "BUT YOU KNEW! HOW COULD YOU THINK THAT?"
        
        show mean cry 1 at center
        w3.c "Mom..."

    else:
        show mean angry 1 at center
        with dissolve
        w3.c "WHAT????"
        w3.c "You SERIOUSLY can't be for real right now, right?"

    jump end

label accuse_w4:
    $ p.guess_murder = True

    jump end