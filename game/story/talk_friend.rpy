# ---------- FRIEND WORKER CONVERSATIONS ----------

label talk_friend:
    # Check remaining conversations and jump to appropriate label
    if w4.conversations == 3:
        jump friend_3

    elif w4.conversations == 2:
        jump friend_2
                
    elif w4.conversations == 1:
        jump friend_1
        
    else:
        jump friend_0


# ---------- 3 Conversations Remaining ----------

label friend_3:

label friend_3_fail:

label friend_3_pass:

# ---------- 2 Conversations Remaining ----------

label friend_2:

label friend_2_fail:

label friend_2_pass:

# ---------- 1 Conversation Remaining ----------

label friend_1:

label friend_1_fail:

label friend_1_pass:

# ---------- 0 Conversations Remaining ----------

label friend_0:
    jump conversations_refresh