# * * * * * * * * * * GAME START * * * * * * * * * *
# * * * * * * * * * * CHAPTER 0  * * * * * * * * * *

# TODO
# 1. Make the characters reappear towards the front whenever they have a line
# 2. Dim the background when the power goes off
# 3. Make characters' sprites dim whenever they aren't speaking
# 4. Make the voices sound replace the bg music. Restart bg music after Work Friend says she can't hear anything
# 5. Consider separating each scene into chapters for easier reading?

label start:

    play music "3.mp3" volume 0.5

    $ pname = renpy.input("Welcome to the WacBonald's crew! What is your name?")
    $ pname = pname.strip()
    if pname == "":
        $ pname = "Silly Little Goose"

    $ p    = Player(Character("[pname]", color="B02020"), pname)
    $ w1   = Worker(Character("Shy Worker"), "Shy Worker", 2)
    $ w2   = Worker(Character("Neutral Worker"), "Neutral Worker", 2)
    $ w3   = Worker(Character("Mean Worker"), "Mean Worker", 3)
    $ w4   = Worker(Character("Work Friend"), "Work Friend", 3)
    $ m    = Character("Manager")



# ---------- OPENING SCENE ----------

    scene kitchen 1
    with fade

    p.c "Oh wow! I'm so excited to start my first-ever shift at WacBonald's!
    I wonder if I can have unlimited Chicken WacNuggets during my shift...?"

    show manager normal at center
    with dissolve

    m "Good morning, [p.name]. Right on time for your first shift!
    You'll be training with [w4.name] at the drive thru today."

    show manager normal at right
    with move

    show friend normal at left
    with moveinleft

    w4.c "Hello!! Welcome to the WacBonald's team!"

    show manager happy at right

    m "Well, I'll leave you two to it then! Please refrain from asking me any questions :)"

    show manager angry at right

    m "Ever."

    hide manager happy
    with moveoutright

    show friend happy at center
    with move

    w4.c "She's quite the handful, huh? Well, let's get to it then!"
    hide friend normal
    with moveoutleft



# ---------- DRIVE THRU SCENE ----------

    scene kitchen 3
    with dissolve

    "You watch [w4.name] working the drive thru for a few transactions..."

    show friend normal at center
    with dissolve

    menu drive_thru:

        w4.c "You ready to give it a try?"

        "Yes!!":
            show friend happy
            w4.c "Awesome!! You got this!!"

        "I think I should watch you a few more times...":
            show friend angry 1
            w4.c "Too bad, you'll never make it in this dog-eat-dog world with that attitude, [p.name]."

    stop music fadeout 0.5
    pause 1.0
    play sound 'plop.mp3'
    with vpunch
    pause 0.5
    play music "7.mp3"

    show friend normal

    "[w4.name] puts the headset on your head."

    play sound 'bell.mp3'

    $ customer = Character("Customer")

    menu customer_1:
        customer "Hello...? Anyone there???? HeeeelllooooooOOOOOOO..."

        "Uhhhh...":
            customer "What do you mean 'Uhhh'?"
        
        "Welcome to WacBonald's! How can I help you?":
            customer "Finally!! Some service!"

    menu customer_2:
        customer "Give me 40 WacNuggets and Sweet 'n' Extra Sweet sauce!!"

        "Sure thing! Would you like fries with that?":
            customer "DUH. I want fifteen LARGE fries. You got that???"

        "Hungry, are we?":
            customer "Why else would I be here???"

        "No.":
            customer "I'LL ROB YA BLIND, GIVE ME MY WACNUGGETS."

    stop music
    show friend worried 1

    "You remove the headset and hand them back to [w4.name]"

    w4.c "Uh... how'd it go?"

    customer "HEY! YOU WITH THE PIGTAILS!"

    pause 2.0
    
    play music "4.mp3"
    
    show customer at left
    with MoveTransition(0.1) 
    with vpunch

    show friend surprised at right
    with MoveTransition(0.1)

    customer "GIVE ME MY WACNUGGETS, PIGTAILS."

    w4.c "Didn't you... just... order?"

    p.c "How is she in the kitchen right now?"

    show friend angry 1

    w4.c "Don't you know how visual novels work? This is just the customer's character sprite.
    Pretend shes talking through the drive thru window."

    w4.c "You want your nuggets?"

    show customer angry
    customer "OBVIOUSLY."

    show friend happy
    w4.c "Order up!"

    show nuggets
    with hpunch
    with moveinright

    hide nuggets
    with moveoutleft

    hide customer angry
    with moveoutleft

    stop music fadeout 1.0
    play music "6.mp3"

    p.c "Do customers always treat us so horribly?"

    show friend angry 2 at center
    with move

    w4.c "Don't ask too many questions."

    "*sniff... sniff...*"

    show friend worried 1 at left
    with move

    show shy worried at right
    with moveinright

    w4.c "Are you alright [w1.name]?"

    w1.c "Absolutely not!! That customer was horrifying! She was rude and had VAMPIRE TEETH. It's not even Halloween..."

    $ current_date = datetime.datetime.today()

    if (current_date.month == 10 & current_date.day == 31):
        p.c "Today is Halloween, actually."
        
        show shy cry
        w1.c "W... what??? Is my memory slipping...? I have to get out of this place before it's too late..."

# REMOVE THIS LATER, TEST ON HALLOWEEN
    else:
        "It is not halloween.
        Today is [current_date.month] [current_date.day]."



# ---------- EXPLOSION SCENE ----------

    stop music

    show friend surprised

    show shy surprised 1

    play sound "explosion.mp3"
    with Shake((0,0,0,0), 5.0, dist=30)

    w1.c "What... was.......... that?"

    play music "6.mp3" fadein 1 volume 0.5

    show shy surprised 1 at center
    with move

    show neutral normal at right
    with moveinright

    menu hear:
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

    play sound "voices.mp3"

    "You look out the drivethru window to see that a giant sinkhole has taken place of the drivethru, consuming all customers and their vehicles within it."
    "An ominous, spooky, frightful, smelly, bewildering, sound of voices echoes from the depths of the sinkhole."
    "You're pretty sure you see at least forty-two cars within the sinkhole, crushed, dangling; their passengers absolutely, positively dead."
    "How did forty-two cars fit in this drivethru anyway?"

    p.c "Hey... guys...? Do you hear that?"

    show friend angry 3

    w4.c "What did I say about asking too many questions?"

    stop sound

    show friend happy

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

    menu safety:
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

    menu ask_boss:
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

    show mean angry at center
    with moveinleft

    w3.c "We can't even leave if we wanted to, now?! We should have just left when we should! For God's sake, I hate it here. You're all insufferable."

    hide mean angry
    with moveoutleft

    "[w3.name] goes to sit down at a table by himself."

    show manager normal

    m "Not much we can do about that now, so let's try our best to clean up and keep ourselves busy. I'll be in my office."

    hide manager normal
    with moveoutright

    show friend worried 1 at center
    with move

    w4.c "Well.. not much we can do about the situation now, I guess... let me go to the restroom right quick, then come help me tidy up in the kitchen, OK?"



# ---------- MANAGER SCENE ----------

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

        menu friends:
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

    menu get_manager:
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

    menu guilty:
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
    w2.c "We'll hand over [p.name] when they arrive."

    hide neutral angry 1
    with moveoutright

    w3.c "I've got my eyes on you, [p.name]."

    hide mean angry
    with moveoutleft

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

    call screen start_chapter1 with dissolve

return