﻿# resources:
# character assets : created with Sutemo
# amongus.mp3 : https://tuna.voicemod.net/sound/c4ba023d-fa12-4473-8f56-c167d47df425
# bell.mp3 : https://freesound.org/people/deleted_user_13744718/sounds/623667/
# knock.mp3 : https://freesound.org/people/LPHypeR/sounds/500994/
# creak.mp3 : https://freesound.org/people/HerbertBoland/sounds/29692/
# explosion.mp3 : https://freesound.org/people/AENHS/sounds/607049/
# plop.mp3 : https://freesound.org/people/acclivity/sounds/19988/
# voices.mp3 : https://freesound.org/people/Serithi/sounds/151616/
# ring.mp3 : https://pixabay.com/sound-effects/telephonering-6384/
# nuggets.png : iStock-171590269
# customer.png : iStock-1220339777
# customer angry.png : iStock-1220339777 with modifications
# restaurant.png : https://pixabay.com/photos/beijing-airport-airport-the-room-2379526/
# rupaul.png : https://www.shutterstock.com/image-photo/los-angeles-mar-16-rupaul-andre-1047755632



init python:

    class Player:
        def __init__(self, character, name, innocence = 0, conversations_had = 0, cat = False, mom = False, crazy = False, guess_murder = False):
            self.c = character
            self.name = name
            self.innocence = innocence
            self.conversations_had = conversations_had
            self.cat = cat
            self.mom = mom
            self.crazy = crazy
            self.guess_murder = guess_murder

    class Worker:
        def __init__(self, character, name, conversations):
            self.c = character
            self.name = name
            self.conversations = conversations

# ********** THE FOLLOWING SHAKER CODE IS FROM RENPY.ORG
# https://www.renpy.org/wiki/renpy/doc/cookbook/Shake_effect
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,time,child,add_sizes=True,**properties)

        Shake = renpy.curry(_Shake)