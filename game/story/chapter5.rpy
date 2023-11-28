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

    p.c "Wait, won't the police do an investigation? Telling them who we {i}think{/i} did it won't mean anything, right?"

    show mean bored at left
    w3.c "You're kidding right? This is a visual novel. The 'police' out there - not even real."
    w3.c "Your fate lies in the decisions you've made throughout this game and this very moment."

    hide shy
    with dissolve

    hide neutral
    with dissolve

    hide mean
    with dissolve

    $ accused = ''

    menu:
        "I think the murderer was..."

        "[w1.name]":
            $ accused = "w1"
            $ accused_info = "Needless to say, she didn't make it.\nOh, she didn't die. But she did stay in jail until the ripe age of 114. Although she was innocent in the manager's death, she found a home in the jail she lived in and 'adopted' many of the young inmates as her own children. Many of them returned to society as well-nurtured people. How wholesome!"
            
            jump accuse_w1

        "[w2.name]":
            $ accused = "w2"
            if (p.cat):
                $ accused_info = "[w2.name]'s kitties were split amongst the remaining WacBonald's workers. [w2.name] missed them very much - so much so that he escaped jail to recollect them. He stole them from you and your coworkers' humble abodes in the middle of the night, and went on to live a nomad life in the forest with all of his twelve and a half kitties."

            else:
                $ accused_info = "[w2.name] eventually escaped from jail, returning to his apartment. Turned out he had twelve (and a half) kitties at home, with no one to care for them. Unfortunately, the kitties didn't make it. In [w2.name]'s sadness, he promptly taxidermied his beloved kitties and donated them to a local museum before returning to jail."

            jump accuse_w2

        "[w3.name]":
            $ accused = "w3"
            if (p.mom):
                $ accused_info = "[w3.name] was pissed that he went to jail. You knew that the manager was his mom, so it was very unlikely of him to have killed her! But he was a bit of a thorn in your side.\n[w3.name] eventually got out of jail after 2 years and proceeded to sue WacBonald's, the police force, and you. You don't end up in jail, but your paycheques are garnished for the rest of your life!"

            else:
                $ accused_info = "[w3.name] eventually proves his innocence and leaves jail after 2 years. It was later revealed that the manager was his mother! How did the police not know that before sending him away? Weird.\nNonetheless, he decides to sue WacBonald's, the police force, and you! In the process, [w3.name] accused you of the manager's / his mother's murder. Even though you were innocent, you decide to run away, change your identity, and live a new life in Peru."

            jump accuse_w3

        "[w4.name]":
            $ accused = "w4"
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

    show friend angry 3 at center
    with dissolve

    w4.c "So much for friends having each others' backs, huh?"
    w4.c "I should have known better than to trust you."

    jump end