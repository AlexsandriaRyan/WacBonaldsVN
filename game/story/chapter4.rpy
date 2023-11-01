# * * * * * * * * * * CHAPTER 4  * * * * * * * * * *
# ---------- CONVERSATIONS LOOP ----------

label chapter4:
    
    stop music fadeout 1.0
    pause(1.0)
    scene black
    with fade
    play music "6.mp3" volume 0.5
    pause(3.0)
    scene restaurant
    with fade

    # simulated power return
    show layer master at night
    with Dissolve(0.5)
    show layer master 
    with Dissolve(0.1)
    show layer master at night
    with Dissolve(1)
    show layer master 
    with Dissolve(0.1)
    show layer master at night
    with Dissolve(0.5)
    show layer master
    with Dissolve(1)

    show friend surprised at center
    with dissolve

    w4.c "Wow, the power must have come back on!"

    show friend worried 1

    menu:
        w4.c "[p.name], I'm so sorry you've got caught up in this. It must be stressful having to worry about life in jail with no parole on the first day."

        "Uhhhh... yeah":
            w4.c "*sigh*"

        "Why are you sorry?":
            show friend angry 3
            w4.c "Can't I just feel bad for you for a second, please?"

        "Life in jail???":
            show friend worried 1
            w4.c "I mean, you could escape, but we're surrounded by a sinkhole death moat right now."

    show friend worried 1

    w4.c "You are taking this seriously, right? I think it'd be worthwhile to chat with the others and convince them that you're innocent."

    hide friend
    with dissolve

label conversations:

    if p.conversations_had < 10:
        call screen pick_character with dissolve

    else:
        jump endgame

label endgame:
    # put different endings here