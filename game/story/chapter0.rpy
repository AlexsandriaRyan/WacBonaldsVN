# * * * * * * * * * * CHAPTER 0  * * * * * * * * * *
# ---------- GAME START ----------

# TODO
# 1. Make the characters reappear towards the front whenever they have a line
# 2. Make characters' sprites dim whenever they aren't speaking
# 3. Find new bg music asset for power outage? Something creepy maybe?


label start:

    play music "3.mp3" volume 0.5

    $ pname = renpy.input("Welcome to the WacBonald's crew! What is your name?")
    $ pname = pname.strip()

    if pname == "":
        $ pname = "Silly Little Goose"

    elif pname.lower() == "alex":
        $ pname = "Wannabe"

    $ p    = Player(Character("[pname]", color="B02020"), pname)
    $ w1   = Worker(Character("Shy Worker"), "Shy Worker", 2)
    $ w2   = Worker(Character("Neutral Worker"), "Neutral Worker", 2)
    $ w3   = Worker(Character("Mean Worker"), "Mean Worker", 3)
    $ w4   = Worker(Character("Work Friend"), "Work Friend", 3)
    $ m    = Character("Manager")



# ---------- OPENING SCENE ----------

    # set scene and music
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

    jump chapter1