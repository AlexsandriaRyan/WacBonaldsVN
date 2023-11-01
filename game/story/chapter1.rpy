# * * * * * * * * * * CHAPTER 1  * * * * * * * * * *
# ---------- DRIVE THRU SCENE ----------

label chapter1:

    scene kitchen 3
    with dissolve

    "You watch [w4.name] working the drive thru for a few transactions..."

    show friend normal at center
    with dissolve

    menu:
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

    menu:
        customer "Hello...? Anyone there???? HeeeelllooooooOOOOOOO..."

        "Uhhhh...":
            customer "What do you mean 'Uhhh'?"
        
        "Welcome to WacBonald's! How can I help you?":
            customer "Finally!! Some service!"

    menu:
        customer "Give me 40 WacNuggets and Sweet 'n' Extra Sweet sauce!!"

        "Sure thing! Would you like fries with that?":
            customer "DUH. I want fifteen LARGE fries. You got that???"

        "Hungry, are we?":
            customer "Why else would I be here???"

        "No.":
            customer "I'LL ROB YA BLIND, GIVE ME MY WACNUGGETS."

    stop music
    show friend worried 1

    "You remove the headset and hand it back to [w4.name]"

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
    $ current_date_month = current_date.strftime("%B")
    $ current_date_formatted = current_date.strftime("%m %d")

    if (current_date_formatted == "10 31"):
        p.c "Today is Halloween, actually."
        
        show shy cry
        w1.c "W... what??? Is my memory slipping...? I have to get out of this place before it's too late..."

    else:
        "It is not halloween.
        Today is [current_date_month] [current_date.day]."

    jump chapter2