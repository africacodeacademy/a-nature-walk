# -*- coding: utf-8 -*-
"""
A Nature Walk by HEXBREAK

This is the final project for the ACA-VCS Basics Course for Q1 2019. 

Authors:
    * Kiersten Baloto
    * Eamon Hoskins
    * Jacob Kagin

"""

import os
import time


# Logo
hexbreak_logo = "\n\n\
.##..##..######..##..##..#####...#####...######...####...##..##.\n\
.##..##..##.......####...##..##..##..##..##......##..##..##.##..\n\
.######..####......##....#####...#####...####....######..####...\n\
.##..##..##.......####...##..##..##..##..##......##..##..##.##..\n\
.##..##..######..##..##..#####...##..##..######..##..##..##..##.\n\
\n\n\n\
                       P R E S E N T S..."

title_0_logo = "\n\
                         |    \n\
                        |||   \n\
                       |  ||  \n\
                      .''''|. \n\
                     .|.  .||."

title_1_logo = "\n\
'|.   '|'           .                           \n\
 |'|   |   ....   .||.  ... ...  ... ..    .... \n\
 | '|. |  '' .||   ||    ||  ||   ||' '' .|...||\n\
 |   |||  .|' ||   ||    ||  ||   ||     ||     \n\
.|.   '|  '|..'|'  '|.'  '|..'|. .||.     '|...'"

title_2_logo = "\n\
        '|| '||'  '|'         '||  '||     \n\
         '|. '|.  .'   ....    ||   ||  .. \n\
          ||  ||  |   '' .||   ||   || .'  \n\
           ||| |||    .|' ||   ||   ||'|.  \n\
            |   |     '|..'|' .||. .||. ||."


# Nature Walk Strings

# Chapter 1 Strings: Intro
story_intro = "\
You are an intrepid private eye and it is late at night. You are suddenly \n\
awakened by a urgent phone call from Mrs. Martha Farthing, her daughter is \n\
missing! She was last seen heading to the woods for her regular nature walk \n\
but hadn't returned home. The police refuse to help because she has only been \n\
gone for a few hours, but Mrs. Farthing knows something terrible must have \n\
befallen her! \n\
You think to yourself it's late but maybe this might be a good opportunity \n\
to go on a nice nature walk as well! \n\n\
You arrive at the head of the edge of the woods. There's a path leading into \n\
the woods on your right, as well as think patch of trees in front of you. \n\
Out of the corner of your eye you something catches your attention, it looks \n\
like a note.\n"

# Chapter 2 Story Strings
story_2a = "\n\
You take the obvious path which heads straight into the forest. Looking \n\
down you notice what look like fresh footprints! \n\
Do you want to follow the footprints into the woods or head back?\n"

story_2b = "\n\
Ignoring the path, you trudge straight into the thickest part of the \n\
woods. You hear something! \n\
You decide to follow the sounds and find yourself face to face with a \n\
scary looking BEAR!!! It doesn't seem bothered by you yet, but you probably\n\
should get out of there! \n\
You might be able to dive behind some bushes to hide or try to make a run \n\
for it.\n"

story_2c = "\n\
You look around and you see that someone as pinned a mysterious note \n\
to the base of a tree. You take it and read it carefully... \n\
It says, 'Follow the trail of stones at the base of this tree to the meeting \n\
point!' Looking down, you see a trail of stones leading into the woods. \n\
Do you follow the trail or just go back to the path to the woods? \n"

# Chapter 3 Story Strings
story_3a = "\n\
You go in following the path into the trees and now find yourself deep in the \n\
woods and start worry that you might be lost! \n\
But then you see a light beyond the trees... You could also make out a clearing \n\
leading to the edge of the forest. \n\
\n"

story_3b = "\n\
You dash behind bushes trying to escape, and you manage to get away, but \n\ 
suddenly your feet give way beneath you and you fall into a deep hole! \n\
You tumble down and twist your ankle. Ouch! That hurts! \n\
You hear footsteps around the top of the hole, but they fade into the \n\
distance...  \n\
Do you wait for someone to save you or do you to try to climb out?\n"

story_3c = "The trail leads you to a large rock in the woods. Looking carefully, \n\
you see another note! It reads, 'I see you are good at following instructions! \n\
Keep following the trail and you'll find what you've been looking for!' \n\
Do you trust the note and keep following the trail or do you decide to head \n\
back deeper into the woods?\n"

# Chapter 4 Story Strings
story_4a = "\n\
You approach the cabin and manage to sneak up to a window where you see \n\
inside...\n\
It's Penny!!! She's tied up in a chair and she looks like she's alone. \n\
But wait, did you hear something in there?"

story_4b = "\n\
You wait for a few hours until daylight and finally hear someone near by. \n\
You yell for help as loud as you can and your yelling for help has attracted \n\
the attention of a friendly hiker. You tell her you hurt your ankle and she \n\
asks if you want to wait for the paramedics or do you think you can climb \n\
out with her help?\n"

story_4c = "Moving quickly, you suddenly find yourself at the edge of a cliff! \n\
As you look down to see the huge fall below, someone behind you yells, \n\
'Turn around NOW!' \n\
Do you do as you're told and turn around, or do you try to make a run for it, \n\
or play dumb and do nothing? \n"

# Ending Story Strings
story_end_1 = "You're not looking for trouble so you call the cops and they arrive \n\
and bust into the cabin. They rescue Penny and capture the evil Xavier Cross, \n\
Penny's greedy business partner. The police take all the credit for saving Penny, \n\
but at least she's safe!\n"

story_end_2 = "You look for a way in and you manage to open one of the \n\
windows and crawl in. Penny sees you and starts to make a ruckus getting \n\
the kidnapper's attenion. It's Xavier Cross, Penny's business parther! \n\
You bonk him on the head with a chair and he's out cold...\n\
You did it! You managed to save Penny from the clutches of the greedy Xavier \n\
Cross. You call the cops and Penny is safe and sound. And you managed to get a \n\
nice little paycheck from Penny's Mom! \n\
Good Job!!!\n"

story_end_3 = "\
Your ankle is sore but it feels better after waiting around the whole night. \n\
You decide to give up and just head home. Maybe it's time to rethink your \n\
career as a private detective anyway... \n\
The next day you read in the paper that Penny managed to escape from the \n\
clutches of her business parther Xavier Cross with the help of a friendly \n\
hiker. \n"

story_end_4 = "\
Oh no! It's the kidnapper, Xavier Cross, Penny's greedy business partner. \n\
Not only did you not solve the mystery, but he grabs you and ties you up with \n\
Penny! \n\
Lucky for you a random hiker discovered the cabin and she called the cops to \n\
save the both of you! Thank goodness! \n\
On the other hand, this is not a good look for your reputation as a private eye. \n\
Oh well, can't win them all!\n"

story_end_5 = "You've taken a pretty bad tumble and feel like you hurt your leg \n\
pretty bad, so you wait hoping for the paramadics to show up. \n\
Luckily, they came by pretty quickly and were able to get you to the hospital in \n\
one piece. Turns out it was just a minor sprain. You hear later that after the \n\
hiker left you she also helped save Penny too! Now that's a real hero!\n"

story_end_6 = "You ignore the command and suddenly you feel a kick to your back. \n\
As you tumble to your death, your last thought is, 'I wish I had stayed in bed \n\
instead of going on this darned nature walk!'\n"

# Prompt Strings
prompt_start = "Choose 'p' for the path, 'w' for the woods or 'n' to read the note:  "
prompt_2a = "Choose 'w' for woods , 'b' for back:  "
prompt_2b = "Choose 'h' to hide 'r' to run for it:  "
prompt_2c = "Choose 'f' to follow the note or 'w' to take a different path into the woods:  "
prompt_3a = "Choose 'l' to go to the light , 'c' to head to the clearing:  "
prompt_3b = "Choose 'w' to wait for help , 'c' to try climbing out:  "
prompt_3c = "Choose 'f' to keep following the note , 'd' to go deeper in the woods:  "
prompt_4a = "Choose 'c' to call the cops , 'sn' to sneak into the cabin or 'b' to barge through the door:  "
prompt_4b = "Choose 'w' to wait for the paramedics or 'c' try and climb out:  "
prompt_4c = "Choose 't' turn around , 'r' run away or 'd' don't do anything:  "


#
# Start of the story: 
# 
def start_story(do_intro):
    if do_intro == True:
        #Print Intro Titles
        clear_screen()
        print(hexbreak_logo)
        time.sleep(1)
        clear_screen()
        print(title_0_logo)
        time.sleep(1)
        print(title_1_logo)
        time.sleep(1)
        print(title_2_logo)
        time.sleep(1)

    # Start Story
    clear_screen()

    print(story_intro)
    choice = input (prompt_start)
    clear_screen()

    if choice == 'p':
        print ("You chose: p")
        chapter_2a()
    elif choice == 'w':
        print ("You chose: w")
        chapter_2b()
    elif choice == 'n':
        print ("You chose: n")
        chapter_2c()
    else:
        print("Sorry, didn't get that!")
        time.sleep(1)
        start_story(False)

    return

#
# Chapter 2 Functions
#

def chapter_2a(): 
    print(story_2a)
    choice = input(prompt_2a)
    
    clear_screen()

    if choice =='w':
        print ("You chose: w")
        chapter_3a()
    elif choice == 'b':
        print ("You chose: b")
        chapter_2b()
    else:
        print("Huh?")
        time.sleep(1)
        chapter_2a()
    return

def chapter_2b():
    print(story_2b)
    choice = input (prompt_2b)
    clear_screen()

    if choice == 'h':
        print ("You chose: h")
        chapter_3b()
    elif choice == 'r':
        print ("You chose: r")
        chapter_4c()
    else: 
        print("Say what?")
        time.sleep(1)
        chapter_2b()
    return
    
def chapter_2c():
    print(story_2c)
    choice = input (prompt_2c)
    clear_screen()
    
    if choice == 'f':
        print ("You chose: f")
        chapter_3c()
    elif choice == 'w':
        print ("You chose: w")
        chapter_3a()
    else: 
        print("please choose a valid option")
        time.sleep(1)
        chapter_2c()
    return
    
#
# Chapter 3 Functions
#


def chapter_3a():
    print(story_3a)
    choice = input (prompt_3a)
    clear_screen()
    
    if choice == 'l':
        print ('You chose: l')
        chapter_4a()
        
    
    elif choice == 'c':
        print ('You chose: c')
        chapter_4c()
        
    else:
        print ('WHAT???')
        time.sleep(1)
        chapter_3a()
    return    
    
def chapter_3b():
    print(story_3b)
    choice = input (prompt_3b)
    clear_screen()

    if choice == 'w':
        print ("You chose: w")
        chapter_4b()
    elif choice == 'c':
        print ("You chose: c")
        chapter_3a()
    else: 
        print("Say what?")
        time.sleep(1)
        chapter_3b()
    return
    
def chapter_3c(): 
    print(story_3c)
    choice = input (prompt_3c)
    clear_screen()

    if choice =='f':
        print ("You chose: f")
        chapter_4c()
    elif choice == 'w':
        print ("You chose: w")
        chapter_3a()
    else: 
        print("please choose valid option")
        time.sleep(1)
        chapter_3c()
    return


#
# Chapter 4 Functions
#

def chapter_4a():
    print(story_4a)
    choice = input (prompt_4a)
    clear_screen()

    if choice == 'c':
        print("You chose: c")
        ending_1()
    elif choice == 'sn':
        print("You chose: sn")
        ending_2()
        
    elif choice =='b':
        print('You chose: b')
        ending_4()
    else:
        print("Come again?")
        time.sleep(1)
        chapter_4a()
    return


def chapter_4b():
    print(story_4b)
    choice = input (prompt_4b)
    clear_screen()

    if choice == 'w':
        print("You chose: w")
        ending_5()

    elif choice == 'c':
        print("You chose: c")
        ending_3()

    else:
        print("please choose valid option")
        time.sleep(1)
        chapter_4b()
    return


def chapter_4c():
    print(story_4c)
    choice = input (prompt_4c)
    clear_screen()

    if choice == 't':
        print("You chose: t")
        ending_4()
    elif choice == 'r':
        print("You chose: r")
        chapter_3b()
    elif choice == 'd':
        print("You chose: d")
        ending_6()
    else:
        print("please choose valid option")
        time.sleep(1)
        chapter_4c()
    return

#
# Ending Functions
#

def ending_1():
    print(story_end_1)
    return

def ending_2():
    print(story_end_2)
    return

def ending_3():
    print(story_end_3)
    return

def ending_4():
    print(story_end_4)
    return

def ending_5():
    print(story_end_5)
    return

def ending_6():
    print(story_end_6)
    return


#
# Helper functions below:
#

def clear_screen():
    # Clears the screen for next page of output.
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    start_story(True)
    time.sleep(1)
 
    print ("*** THE END! ***")
    return

if __name__ == '__main__':
    main()
