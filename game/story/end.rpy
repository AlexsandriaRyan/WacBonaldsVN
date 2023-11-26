label end:
    if (p.innocence <= 2):
        jump bad_ending

    elif (p.innocence >= 3 && p.innocence <= 8 && p.guess_murder == False):
        jump incomplete_ending_1

    elif (p.innocence >= 3 && p.guess_murder <= 8 && p.guess_murder == True):
        jump complete_ending

    elif (p.innocence >= 9 && p.guess_murder == False):
        jump incomplete_ending_2
    
    elif (p.innocence >= 9 && p.guess_murder == True):
        jump good_ending


# ---------- BAD ENDING ----------
# less than 3 innocence
label bad_ending:

# ---------- INCOMPLETE ENDING 1----------
# 3-8 innocence
label incomplete_ending_1:

# ---------- COMPLETE ENDING ----------
# 3-8 innocence
# player chooses work friend to die
label complete_ending:

# ---------- INCOMPLETE ENDING 2 ----------
# 9-10 innocence
# player does not choose work friend to die
label incomplete_ending_2:

# ---------- GOOD ENDING ----------
# 9-10 innocence
# player chooses work friend to die
label good_ending: