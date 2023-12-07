label end:
    $ police    = Character("Police")

    stop music fadeout 1.0
    pause(1.0)
    scene black
    with fade

    "You look out the restaurant window to see a makeshift bridge being positioned over the death-moat."
    "Police begin crawling across."
    "A few of them fall into the spooky depths of the death-moat, joining the many drive-thru cars and their passengers that had met their fate hours before."

    play sound "knock.mp3"

    police "It's the police, open up!!!"

    p.c "Coming!!"

    "You rush over to the door to let the police into the WacBonald's."

    play music "5.mp3" volume 0.5
    scene restaurant
    with fade

    show neutral normal at right
    with moveinleft
    
    show mean normal at left
    with moveinleft

    show shy worried at center
    with moveinleft

    police "We haven't got time to do a proper investigation, folks. We also only have one pair of handcuffs."
    police "Tell us who murdered the beloved WacBonald's manager!"

    # ENDINGS:
    # Bad ending: less than 2 innocence
    # Incomplete ending: 3+ innocence and incorrectly guessed the murderer
    # Good ending: 3-8 innocence  and correctly guessed the murderer
    # Ultimate ending: 9+ innocence and correctly guessed the murderer

    
    $ p.guess_murder = True

    # both the ultimate and complete endings start the same.
    if p.innocence >= 3 and p.guess_murder == True:
        jump complete_ending

    elif p.innocence >= 3 and p.guess_murder == False:
        jump incomplete_ending

    else:
        jump bad_ending
    


# ---------- BAD ENDING ----------
# less than 3 innocence

label bad_ending:
    "[w1.name], [w2.name], and [w3.name] look towards you."

    w3.c "[p.name] did it. No doubt about it."

    w2.c "It's the most likely scenario."

    w1.c "T-they did get written up twice today before the manager's death..."

    hide shy
    with dissolve

    hide neutral
    with dissolve

    hide mean
    with dissolve

    "You look towards [w4.name], bewildered."

    show friend worried 2 at center
    with dissolve

    w4.c "As much as I know you didn't do it... WacBonald's operates under a strict democracy policy."

    show friend worried 1 at center
    w4.c "I know, I'm just as surprised as you are."

    show friend worried 2 at center
    w4.c "I wish there was more I could do..."

    scene black
    with fade

    show text "{color=#fff}You were brought to a musty little jail cell, where you withered away until death.\nYou also didn't get the chance to consume any Chicken WacNuggets during your one and only shift at WacBonald's, by the way. How cruel!{/color}\n\n{color=#f00}THE (bad) END{/color}"
    with Dissolve (2.0)

    call screen end_game with dissolve
    return


# ---------- INCOMPLETE ENDING ----------
# 3-8 innocence
# player does not correctly guess the murderer

label incomplete_ending:
    p.c "It was [accused]."

    if accused != w1.name:
        w1.c "Y-yeah... I believe it was [accused], too."

    if accused != w2.name:
        w2.c "Agreed."

    if accused != w3.name:
        w3.c "Jail 'em!"

    scene black
    with fade
    
    show text "{color=#fff}The police escort [accused] out of the WacBonald's restaurant.\n\n[accused_info]{/color}\n\n{color=#f00}THE (incomplete) END{/color}"
    with Dissolve (2.0)

    call screen end_game with dissolve
    return



# ---------- COMPLETE ENDING ----------
# 3-8 innocence
# player correctly guesses the murderer

label complete_ending:
    hide shy
    with dissolve

    hide neutral
    with dissolve

    hide mean
    with dissolve

    "You hesitate to say it. The one person who offerered a mediocre workplace friendship (and sometimes expressed concerning behaviour)... you care a little bit, but you have to do what you think is right!"

    p.c "It was [accused]."

    stop music fadeout 1.0
    pause(1.0)
    play music "1.mp3" volume 0.5

    b "Well, well, well..."

    show bonald neutral at center
    with dissolve

    b "You found me out, [p.name]."

    w1.c "Is... is that Bonald WacBonald???"

    w2.c "No way..."

    w3.c "{i}THE{/i} BONALD WACBONALD?"

    "You are confused. Who the hell is Bonald and why do they look like [w4.name] with gaudy clown makeup... and a suit?"

    show bonald bored 1

    b "You have no idea who I am, do you, [p.name]?"

    show bonald bored 2

    b "Well then..."

    show bonald angry 1

    b "I'll have you know, I didn't plan for it to go like this. I've been going broke and decided to commit tax fraud."

    p.c "You didn't plan to kill the manager??? You were going to frame me!"

    show bonald happy

    b "The manager? She knew too much - when I went to the washroom, she noticed my hair looked much like {i}the{/i} Bonald WacBonald's. AKA me."

    b "I had no other choice but to do what was necessary!"

    show bonald neutral

    b "Anyway, my original plan was to simply sink the building into the sinkhole I made. I planned on making sure everyone was rescued first, of course."

    show bonald angry 2
    
    b "Until {i}you{/i} figured me out and got me caught up in all this hullabaloo."

    p.c "You {i}made{/i} the sinkhole??? The same one with all the creepy voices that swallowed up all the drive thru customers???"

    show bonald bored 2

    b "As soon as I accepted to become the WacBonald's mascot, I was given God-like powers. Duh. I can do pretty much anything I want."
    
    show bonald bored 1 
    b "Obviously I don't want to use those powers all willy-nilly, else I'd be in a predicament like this!"

    show bonald happy

    b "Anyhow, adios amigos! I may not have been able to claim fraud this time, but I can surely escape!"

    hide bonald
    with moveoutleft

    scene black
    with fade

    if p.innocence >= 9:
        jump ultimate_ending
    
    else:
        show text "{color=#fff}[accused_info]{/color}\n{color=#fff}\n{/color}\n{color=#f00}THE END{/color}\n... or is it?"
        with Dissolve (2.0)

        call screen end_game with dissolve
        return



# ---------- ULTIMATE ENDING ----------
# 9-10 innocence
# player correctly guesses the murderer
label ultimate_ending:

    show text "{color=#fff}[accused_info]{/color}\n{color=#fff}\n{/color}\n{color=#f00}THE END{/color}"
    with Dissolve (2.0)
    
    call screen end_game with dissolve
    return