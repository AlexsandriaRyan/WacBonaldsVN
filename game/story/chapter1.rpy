# * * * * * * * * * * CHAPTER 1  * * * * * * * * * *

label chapter1:

    stop music fadeout 1.0

    pause(1.0)

    scene black
    with fade

    play music "6.mp3" volume 0.5

    pause(3.0)

    scene restaurant
    with fade

    call screen pick_character with dissolve

    return