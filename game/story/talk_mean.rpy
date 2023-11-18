# ---------- MEAN WORKER CONVERSATIONS ----------

label talk_mean:
    if w3.conversations == 3:
        jump mean_3

    elif w3.conversations == 2:
        jump mean_2

    elif w3.conversations == 1:
        jump mean_1

    else:
        jump mean_0

# ---------- 2 Conversations Remaining ----------

label mean_3:
    show mean normal at center

    "[w3.name] watches you closely as you approach."

    pause(3.0)

    "He says nothing to you."

    menu:
        "Heeeeeeeyyyyy":
            w3.c "..."

        "I'm really sorry.":
            w3.c "..."

        "Did I do something???":
            w3.c "..."

    "He stares at you."

    show mean angry 2

    "His eyebrows are... pointier?"

    menu:
        "I gather you're not exactly happy with me...":
            w3.c "THAT is the textbook definition of UNDERSTATEMENT."

        "I'm... gonna leave.":
            jump mean_3_fail

        "Is there anything I can do to make this situation better?":
            w3.c "Try anything and you're done for, got it, murderer?"
        
    "You scooch your boot a little farther back from [w3.name] to put some distance between you."

    menu:
        "Look...":
            jump mean_3_pass

        "I'll flatten you.":
            jump mean_3_fail

        "...":
            show mean normal at center
            w3.c "Nothing left to say for yourself, huh?"

    menu:
        "Well...":
            jump mean_3_pass

        "...":
            jump mean_3_fail

       
label mean_3_fail:
    #$ renpy.fix_rollback()

    show mean normal at center

    "[w3.name] relaxes, but his eyes are dead cold."

    w3.c "Try anything, and there'll be another body to collect when we get out of here."

    "Hopefully you got the hint."
    "(If you didn't this means you should go, now)"
    "((Who am I kidding, I'm forcing you to leave this conversation whether you like it or not))"

    hide mean
    with dissolve

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w3.conversations == 2:
        $ w3.conversations -= 1
        $ p.conversations_had += 1
    
    jump conversations

label mean_3_pass:
    #$ renpy.fix_rollback()

    p.c "I know there's not much I can do to prove anything to you. I can accept that you don't like me, but it's hard to accept that you're targeting the wrong person here."

    show mean normal at center

    "[w3.name] relaxes a bit."

    p.c "The manager's death might be a mistake, for all we know. But if it wasn't, there's a murderer among us."

    p.c "You're wasting your time thinking it's me."

    "You walk away from [w3.name]. Who cares what he has to say, anyway? You tell him how it is, sis!!"

    hide mean
    with dissolve

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w3.conversations == 2:
        $ w3.conversations -= 1
        $ p.conversations_had += 1
        $ p.innocence += 1

    jump conversations



# ---------- 2 Conversations Remaining ----------

label mean_2:
    show mean normal at center

    p.c "Hey."

    "[w3.name] pretends you're not there."

    menu:
        "He seems really into his phone."

        "Peer over his shoulder to see what he's looking at.":
            "He's looking at photos of the manager."

        "Snatch his phone.":
            "You catch a glimpse of the manager."
            "He snatches it back immediately."
            jump mean_2_fail

    "The photos look as if she wasn't aware of them being taken. Nothing promiscuous or creepy, just badly-taken shots from work; her working at her desk, supervising behind the counter, eating a hamburger on a break..."

    "I guess that's pretty creepy in-and-of itself though, isn't it?"

    p.c "Is that... the manager? Why do you have so many photos of her?"

    show mean angry 1 at center

    w3.c "WHAT ARE YOU DOING?! Get away from me!!!"

    with vpunch

    "[w3.name] swats at you."

    pause(1.0)

    show mean sad at center
    
    menu:
        "You notice him starting to soften."

        "Leave him alone.":
            jump mean_2_fail
        
        "Sit next to him.":
            "You pull up a chair and sit next to him."

    menu:
        "Say nothing.":
            jump mean_2_pass

        "Ask what's wrong.":
            jump mean_2_fail

       
label mean_2_fail:
    #$ renpy.fix_rollback()

    show mean cry 2 at center

    w3.c "You RUINED my LIFE.. you... you FREAK!"

    pause(1.0)

    show mean cry 1 at center
    with dissolve

    p.c "He seems really upset. Best to leave him be."

    hide mean
    with dissolve

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w3.conversations == 2:
        $ w3.conversations -= 1
        $ p.conversations_had += 1
    
    jump conversations

label mean_2_pass:
    #$ renpy.fix_rollback()

    w3.c "She..."
    pause(2.0)

    show mean cry 1 at center
    with dissolve

    "He struggles to hold back the tears."

    w3.c "Mom..."

    $ p.mom = True

    "He turns his head into you and cries into your shoulder."
    "Who'd have thought that the manager was his mother???"
    "After a few minutes, he sits himself back upright."

    show mean normal at center

    w3.c "Sorry for that. I'm still trying to understand..."

    p.c "So you cry onto the murderer's shoulder?"

    w3.c "Honestly, I don't know if it was you. Maybe it was. I just..."

    show mean sad at center

    w3.c "I don't know what to do..."

    "You sit with him for a few more minutes while he calms down."

    show mean normal at center

    w3.c "Thanks, [p.name]... I'm sorry you had to see that."
    w3.c "Can you keep this a secret between us, though? That the manager's my mom? No one else knows. Not even she did."

    p.c "Wait, you mean the manager didn't know she was your mom?"

    w3.c "Yeah, I was adopted. I found out she was my birth mother a while ago. So... I started working here to get to know her."
    w3.c "I haven't had the chance to speak with her about it yet..."

    show mean sad at center

    w3.c "I guess I won't get the chance to, now."

    p.c "I'm so sorry, [w3.name]."

    w3.c "Thanks... I'm going to need a minute..."

    hide mean
    with dissolve

    p.c "No wonder [w3.name] got so upset seeing the manager's body... who would have thought she was his mother?"

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w3.conversations == 2:
        $ w3.conversations -= 1
        $ p.conversations_had += 1
        $ p.innocence += 1

    jump conversations



# ---------- 1 Conversations Remaining ----------    

label mean_1:
    show neutral normal at center
    with dissolve

    menu:
        "What do you want???"

        "Wow, rude.":
            w3.c "I'm not rude, I'm real."

        "A burger.":
            w3.c "Good thing we work at a literal WacBonald's."

    if (p.cat):
        menu:
            "Mean as always...":
                jump mean_1_fail

            "Why can't we be friends, already?":
                w3.c "Friendship, with a murderer???"

            "Want to hear a secret about [w2.c]?":
                jump mean_1_pass_cat
    else:
        menu:
            "Mean as always...":
                jump mean_1_fail

            "Why can't we be friends, already?":
                w3.c "Friendship, with a murderer???"

    p.c "Hey! I'm not a murderer!"

    show mean bored at center

    menu:
        w3.c "Well, who do you think it is then?"

        "[w1.name]":
            show mean happy
            w3.c "What? [w1.name]? She couldn't even hurt a french fry."
            jump mean_1_pass

        "[w2.name]":
            show mean happy
            w3.c "What? [w1.name]? Don't get me wrong, he's definitely odd, but I wouldn't think he'd be capable of that."
            jump mean_1_pass

        "[w3.name]":
            if (p.mom):
                show mean sad at center
                w3.c "How could you say that... you're messed up, you know that?"
                jump mean_1_fail
            
            else:
                show mean angry 1
                w3.c "The fact that you could accuse me of that is beyond insane!"
                jump mean_1_fail

        "[w4.name]":
            show mean surprised
            w3.c "Hmm. I guess I never considered [w4.name]. I don't really know much about her, now that I think about it..."
            jump mean_1_pass

        "...":
            w3.c "Just what I thought. Freak."
            jump mean_1_fail

label mean_1_fail:
    #$ renpy.fix_rollback()

    hide mean
    with dissolve

    "[w3.name] definitely doesn't want to speak with you, right now."

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w3.conversations == 1:
        $ w3.conversations -= 1
        $ p.conversations_had += 1

    jump conversations

label mean_1_pass:
    #$ renpy.fix_rollback()

    show mean normal at center

    w3.c "Either way, whether it's you or anyone else... we should be careful with who we speak to."
    w3.c "Including you..."
    pause(2.0)
    w3.c "...and myself."

    "He gives a little sigh and gets back to scrolling on his phone."

    hide mean
    with dissolve

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w3.conversations == 1:
        $ w2.conversations -= 1
        $ p.conversations_had += 1
        $ p.innocence += 1

    jump conversations

label mean_1_pass_cat:
    #$ renpy.fix_rollback()

    show mean surprised at center

    w3.c "You know something about [w2.name]???"
    w3.c "He's been here for years, but doesn't really talk much about himself."

    show mean happy at center

    w3.c "Please tell me before I go convince everyone you're the murderer."

    p.c "Okay, okay!! He has TWELVE cats. Kinda."

    show mean surprised

    w3.c "...Kinda?"

    p.c "Yeah... he taxidermied one of them. Half of one."

    w3.c "Oh-"

    show mean surprised at left
    with move
    
    show neutral normal at right
    with moveinright

    w2.c "Did I just hear my name?"

    pause(3.0)

    show mean happy at left

    w3.c "No."

    w2.c "Oh. OK."

    hide neutral
    with moveoutright

    show mean happy at center
    with move

    "You both laugh for a few seconds."

    w3.c "Thanks for the laugh, [p.name]. I really needed it after today."

    hide mean
    with dissolve

    # Double-check that the conversation variables align.
    # This prevents the variables from updating again if the 
    # player selects the "back" option
    if w3.conversations == 1:
        $ w2.conversations -= 1
        $ p.conversations_had += 1
        $ p.innocence += 1

    jump conversations



# ---------- 0 Conversations Remaining ----------

label mean_0:
    jump conversations_refresh