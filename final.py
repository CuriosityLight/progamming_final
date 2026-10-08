# KC, SP, VC, text based adventure game
import random
import time
print("Start")


#kc, stats of player and enemy.
player = {  
    "hp": 20,
    "attack": 6,
    "sanity": 100,
    "inventory": []
}

enemy = {
    "hp": 34.3,
    "attack": 4,
}

current_room = 1
move = ""


    

#VC storyline/instructions
print("""
You wake up in a house with a headache. Thinking you're at home you get up to look around. You soon realize that this is not your home; you do not know where you are. 
Your job now is to find a way out through exploring the building.
""")

#SP first room
def room1(move):
    print("you look infront of you and there is only one door so you decide to go through it and you find a long stairway.")
    while True:
        move = input("Do you want to go UP the staircase or DOWN the staircase?") .lower().strip()
        if move == "up":
            return 2
        elif move == "down":
            return 3
        else:
            print("That's not a choice, choose up or down:")

    
#SP second choice
def room2(move):
    print("you find two different doors, one is all BLACK and has a bunch of picutre frames without anything in it, the other one is PINK with a bow and the door behind which where you just came from.")
    move = input("which door do you want to go in?: ")
    print("sanity level:", player["sanity"])
    if move == "pink":
        return 4
    elif move == "black":
        return 6
    else:
        print("that's not a chocie, pick PINK or BLACK: ")
    
    


#VC third choice continue tomorrow
def room3():
    print("You can in and the smell of clorine hits you like a truck. There's circle pools all around the floor. ")



#SP 4th room
def room4():
    print("You walk into an room that has a lot of hello kitty plushies, you see a big pink bow in the middle of the room")
    move = input("do you want to pick up the bow YES or NO?:")
    if move == "yes":
      inventory += 1
    if move == "no":
        inventory == 0 




def room5():
    print("unfinished")
def room6():
    print(" you walk into an all black room with a bunch of picture frames but this time it has your memories in them. you feel your head pounding and these memories do somethin to you.")
    
def room7():
    print("unfinsished")


# kc, the thing that calls all the functions
while True:
    player["sanity"] -= 10
    if current_room == 1:
        current_room = room1(move)
    elif current_room == 2:
        current_room = room2(move)
    elif current_room == 3:
        current_room = room3()
    elif current_room == 4:
        current_room = room4()
    elif current_room == 5:
        current_room = room5()
    elif current_room == 6:
        current_room = room6()
    elif current_room == 7:
        current_room = room7()
    elif current_room == 8:
        current_room = print("you escaped, at last")