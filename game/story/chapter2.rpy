# * * * * * * * * * * CHAPTER 2  * * * * * * * * * *
# ---------- EXPLOSION SCENE ----------

label chapter2:
    
    stop music

    show friend surprised

    show shy surprised 1

    play sound "explosion.mp3"
    with Shake((0,0,0,0), 5.0, dist=30)

    w1.c "What... was.......... that?"

    play music "6.mp3" fadein 1.0 volume 0.5

    show shy surprised 1 at center
    with move

    show neutral normal at right
    with moveinright

    menu:
        w2.c "Did you guys hear that?"

        "No":
            show neutral angry 1
            w2.c "Very funny."

        "Yes!!":
            w2.c "Glad I'm not going crazy."
  
        "What are you talking about?":
            show neutral angry 1
            w2.c "Did you not just hea-... y'know what, nevermind."


    show neutral normal

    w2.c "It looks like the whole drivethru became a sinkhole... I'll go get the manager."

    hide neutral normal
    with moveoutright

    show shy worried at right
    with move

    stop music fadeout 2.0

    play music "voices.mp3" fadein 1.0

    "You look out the drivethru window to see that a giant sinkhole has taken place of the drivethru, consuming all customers and their vehicles within it."
    "An ominous, spooky, frightful, smelly, bewildering, sound of voices echoes from the depths of the sinkhole."
    "You're pretty sure you see at least forty-two cars within the sinkhole, crushed, dangling; their passengers absolutely, positively dead."
    "How did forty-two cars fit in this drivethru anyway?"

    p.c "Hey... guys...? Do you hear that?"

    show friend angry 3

    w4.c "What did I say about asking too many questions?"

    stop music fadeout 2.0

    show friend happy

    play music "6.mp3" fadein 1.0 volume 0.5

    w4.c "I don't hear anything, [p.name].
    Maybe the manager will let us close up the store! A sinkhole is definitely too much of a hazard to stay open!"

    hide shy worried
    with moveoutright

    hide friend normal
    with moveoutright

    scene restaurant
    with dissolve

    show neutral angry 1 at left
    with dissolve

    show manager happy at right
    with dissolve

    w2.c "I really think we should be closing up, boss."

    m "Absolutely not. The drivethru is the only area with the sink hole - we can still have indoor service."

    show manager angry

    m "Now go put a pylon in front of the drivethru and get back to work."

    show neutral angry 2
    w2.c "Fine."

    hide neutral angry 2
    with moveoutleft

    show mean normal at center
    with moveinleft

    show friend normal at left
    with moveinleft

    show manager normal

    w3.c "Yo, boss, did I just hear that the drivethru is closed? Can we go home?"

    w4.c "Yeah, that sinkhole poses a working hazard. We really should put our workers' safety first."

    menu:
        m "Do I look like the type to care about workers' rights or 'safety first'? Get back to your stations, now."

        "I don't think so! Stop being a meanie weanie and close up this dang WacBonald's!":
            show manager angry
            m "Don't you dare tell me what to do, [p.name]. Your first day and you've already got a writeup."

        "Dang, girl, you put the 'wac' in 'WacBonald's'":
            show manager angry
            m "How else do you think I got this job? Because I think you meant this as an insult, you're getting a writeup for that, [p.name]."

        "I love working for WacBonald's!!! I promise my whole life to this company 'til the day I die!":
            show manager happy
            m "I appreciate your enthusiasm, [p.name]!"

            show manager normal
            m "Unfortunately, we have a strict no-cringe policy. That's going to have to be a writeup."

    show mean bored

    w3.c "Are you stupid??? Getting written up on your first day? WacBonald's will hire anyone, these days..."

    hide mean bored
    with moveoutleft

    menu:
        "I'm so sorry, boss - can you please forgive me and forgo the writeup? :(":
            show manager angry
            m "What did I say about asking questions, [p.name]? That's two writeups now."

        "Can I go home now?":
            show manager angry
            m "What did I say about asking questions, [p.name]? That's two writeups now."

        "Is it too late to quit?":
            show manager angry
            m "What did I say about asking questions, [p.name]? That's two writeups now."

    hide manager angry
    with moveoutright

    show friend surprised at center
    with move

    w4.c "[p.name], what are you thinking?! It's your first day and you've already gotten on the manager's bad side... please be more careful."

    stop music

    play sound "explosion.mp3"
    with Shake((0,0,0,0), 5.0, dist=30)

    # simulated power outage
    show layer master at night
    with Dissolve(0.1)
    show layer master
    with Dissolve(0.5)
    show layer master at night
    with Dissolve(0.1)
    show layer master
    with Dissolve(1)
    show layer master at night
    with Dissolve(0.1)
    show layer master
    with Dissolve(0.5)
    show layer master at night
    with Dissolve(1)

    w1.c "Wahhh.. not again!"
    w2.c "Did the power just go out...?"
    w3.c "You've got to be KIDDING me."

    show friend worried 2
    w4.c "I can't believe it... there's a sinkhole outside the front door now, too."

    "You check the front windows. The sinkhole has expanded, creating a death-moat around the perimeter of the WacBonald's."

    show friend worried 2 at left
    with move

    show manager happy at right
    with moveinright

    m "Silver linings, guys, there's no customers in the store, and it looks like we're stuck here. Let's close up for now until we're rescued."

    show mean angry 1 at center
    with moveinleft

    w3.c "We can't even leave if we wanted to, now?! We should have just left when we should! For God's sake, I hate it here. You're all insufferable."

    hide mean angry 1
    with moveoutleft

    "[w3.name] goes to sit down at a table by himself."

    m "Typical [w3.name], he'll never change, huh?"

    show manager normal

    m "Not much we can do about it now, so let's try our best to clean up and keep ourselves busy. I'll be in my office."

    hide manager normal
    with moveoutright

    show friend worried 1 at center
    with move

    w4.c "Well.. not much we can do about the situation now, I guess... let me go to the restroom right quick, then come help me tidy up in the kitchen, OK?"

    jump chapter3