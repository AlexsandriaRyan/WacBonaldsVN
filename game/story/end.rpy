label end:
    $ police    = Character("Police")

    scene black
    with fade

    "You look out the restaurant window to see a makeshift bridge being positioned over the death-moat."
    "Police begin crawling across."
    "A few of them fall into the spooky depths of the death-moat, joining the many drive-thru cars and their passengers that had met their fate hours before."

    # knock sound

    police "It's the police, open up!!!"

    if p.innocence <= 2:
        jump bad_ending

    elif p.innocence >= 3 and p.innocence <= 8 and p.guess_murder == False:
        jump incomplete_ending_1

    elif p.innocence >= 3 and p.guess_murder <= 8 and p.guess_murder == True:
        jump complete_ending

    elif p.innocence >= 9 and p.guess_murder == False:
        jump incomplete_ending_2
    
    elif p.innocence >= 9 and p.guess_murder == True:
        jump good_ending


# ---------- BAD ENDING ----------
# less than 3 innocence
label bad_ending:
    w2.c "Coming, one sec."

    "[w2.name] opens the door for the police to enter the WacBonald's."

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

    show text "{color=#fff}You were brought to a musty little jail cell, where you withered away until death.\nYou also didn't get the chance to consume any Chicken WacNuggets during your one and only shift at WacBonald's, by the way.How cruel!{/color}\n\n{color=#f00}THE (bad) END{/color}"
    with Dissolve (2.0)

    call screen end with dissolve


# ---------- INCOMPLETE ENDING 1----------
# 3-8 innocence
label incomplete_ending_1:
    p.c "Coming!!"

    "You rush over to the door to let the police into the WacBonald's."

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

    p.c "It was [accused]"

    if accused != w1.name:
        w1.c "Y-yeah... I believe it was [accused], too."

    if accused != w2.name:
        w2.c "Agreed."

    if accused != w3.name:
        w3.c "Jail 'em!"

    scene black
    with fade
    
    show text "{color=#fff}The police escort [accused] out of the WacBonald's restaurant.\n\n[accused_info]{/color}\n\n{color=#f00}(one of) THE (incomplete) END(s){/color}"
    with Dissolve (2.0)

    call screen end with dissolve


# ---------- COMPLETE ENDING ----------
# 3-8 innocence
# player chooses work friend to die
label complete_ending:


    scene black
    with fade

    show text "{color=#fff}\n{/color}\n\n{color=#f00}THE (sort-of complete) END{/color}"
    with Dissolve (2.0)

    call screen end with dissolve


# ---------- INCOMPLETE ENDING 2 ----------
# 9-10 innocence
# player does not choose work friend to die
label incomplete_ending_2:



    scene black
    with fade

    show text "{color=#fff}The police escort [accused] out of the WacBonald's restaurant.\n{/color}\n{color=#f00}[accused_info]\n\n(one of) THE (incomplete) END(s){/color}"
    with Dissolve (2.0)

    call screen end with dissolve


# ---------- GOOD ENDING ----------
# 9-10 innocence
# player chooses work friend to die
label good_ending:

    scene black
    with fade

    show text "{color=#fff}\n{/color}\n{color=#f00}THE (good) END{/color}"
    with Dissolve (2.0)
    
    call screen end with dissolve