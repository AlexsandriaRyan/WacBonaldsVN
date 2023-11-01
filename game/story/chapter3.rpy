# * * * * * * * * * * CHAPTER 3  * * * * * * * * * *
# ---------- MANAGER SCENE ----------

label chapter3:
    
    scene black
    with fade

    play music "3.mp3" volume 0.5 fadein 1.0

    "Everyone but [w3.name] helps clean up. He's busy sitting alone at a restaurant table, sulking.
    You feel a bit bad for him - he seemed pretty upset."

    "It doesn't take long for the kitchen to get cleaned up with everyone else's help."

    "Help doesn't seem to be on the way anytime soon, as a pack of racoons have surrounded the sinkhole moat around WacBonald's. They are feral and have been attacking anyone that approaches."

    "You sit with [w4.name] at a table once you're done.
    A couple hours pass, and you get to know [w4.name] a little more."

    scene restaurant
    with fade

    show layer master at night

    show friend happy at center
    with dissolve

    p.c "Wait, aren't those customers in the background?"

    show friend angry 1

    w4.c "Remember what I told you about this being a visual novel? Stop asking questions and pretend they aren't there. This is the closest royalty-free stock image Alex could find that ressembles the inside of a... WacBonalds *wink wink*."

    show friend happy at center

    w4.c "You're too funny! I'm so glad I was able to make a friend out of such an icky day."

    show friend angry 1

    $ friend_check = False;

    while friend_check == False:

        menu:
            w4.c "We ARE friends, right?"

            "I literally just met you today...":
                $ friend_check = False;

            "Absolutely!":
                $ friend_check = True;
            
            "Uhhh... no?":
                $ friend_check = False;
    
    show friend happy

    w4.c "Yay! I'm so glad we're on the same page. You got my back, I've got yours!"

    "You hear grumbling throughout the restaurant; [w1.name], [w2.name], [w3.name] seem especially restless."

    p.c "Hey, [w4.c], I'm going to check on the manager... Curious to know what the ETA is on our rescue."

    show friend angry 1

    menu:
        w4.c "I wouldn't do that if I were you."

        "Get the manager anyway":
            show friend angry 3
            w4.c "Fine..."

        "Get the manager, but feel like you have a choice in the progression of the story":
            show friend angry 3
            w4.c "You really like breaking the fourth wall, huh? So be it..."

    stop music fadeout 1.0

    scene black
    with fade

    show layer master at night

    play sound "knock.mp3"

    "You knock on the door."

    pause 3

    "No response..."

    play sound "knock.mp3"

    "You knock on the door again."

    p.c "Hello? Boss? You in there...?"

    pause 3

    play sound "creak.mp3"

    "You open the door."

    pause 1

    show manager dead at center
    with dissolve

    p.c "Oh... oh my god."
    p.c "HELP!!"

    play music "2.mp3" volume 0.5 fadein 1.0

    show mean surprised at left
    with moveinleft

    w3.c "What in the -"

    show mean angry
    w3.c "WHAT DID YOU DO???"

    show neutral normal at right
    with moveinright

    w2.c "What's going on no-"

    show neutral worried

    w2.c "Oh my god."
    w2.c "[p.name]... what have you done..."

    p.c "Guys, no, you have the wrong idea... this wasn't me. I just opened the door and saw her like this!"

    show shy worried at right
    with moveinright

    w1.c "Huh, what did [p.name] find?"

    show shy cry

    w1.c "Oh my god. OH MY GOD."

    hide shy cry
    with moveoutright

    "[w1.name] runs back to the restaurant, holding her face, sobbing."

    w3.c "You get written up TWICE and this is what you do to the manager?? That's not how you keep a job, you psycho!"

    with vpunch

    "[w3.name] tries to grab you by the arm."

    show friend angry 2 at left
    with moveinleft

    menu:
        w4.c "Hold it!! [p.name] probably didn't do this!"

        "Probably?":
            w4.c "You know what I mean. The others seem to think you did this."

        "Uhh, I DEFINITELY didn't do this.":
            w4.c "Well... I'm sure of that, but the others don't seem to think so..."

    show friend angry 1 at left

    w4.c "I mean, the scene does look pretty..."
    w4.c "incriminating."
    
    show neutral angry 2 at right

    w2.c "I'm not about to put my hands on someone. I recommend everyone does the same."

    show neutral angry 1 at right

    w2.c "As messed up as the situation is, the police will be here soon enough. We're trapped until then."
    w2.c "We'll hand [p.name] over when they arrive."

    hide neutral angry 1
    with moveoutright

    show mean angry at right
    with move

    w3.c "I've got my eyes on you, [p.name]."

    hide mean angry
    with moveoutright

    show friend worried

    w4.c "Try not to worry, [p.name]... I'll try to talk to the police when they get here and vouch that you were with me the whole time..."
    w4.c "I can't promise anything, though... It seems the others are pretty convinced you did this."
    w4.c "I know you'd do that same for me. Friends got each others' back, right?"

    hide friend worried
    with moveoutleft

    scene black
    with fade

    "You close the door, hands shaking. You slowly make your way back to the restaurant where everyone is sitting in separate areas."
    "The room feels cold, tense. A scent of cold, stale WacNuggets fills the air."
    "You sit next to [w4.name]. She seems uneasy, but has shown you the most kindness... hopefully she sees your innocence."

    window hide

    pause (1.0)

    show text "HOW TO PLAY:\nTake part in 10 conversations with your fellow coworkers.\nCollect evidence to prove your innocence by selecting the right dialogue options."
    with Dissolve (2.0)

    call screen start_conversations with dissolve