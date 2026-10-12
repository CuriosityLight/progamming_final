# KC, SP, VC, LV, text based adventure game
import random
from random import SystemRandom
import time


#kc, stats of player and enemy.
player = {  
    "hp": 20,
    "attack": 10,
    "sanity": 100,
    "inventory": []
}

clock_enemy = {
    "hp": 343.38,
    "attack": 4,
}


rand = SystemRandom()
bow_obtained = 0
current_room = 1
move = ""
duck_obtained = 0
fight_turn = ""
fight_enemy = ""
fight_choices = ["defend", "attack", "sanity"]
fight_seen = 0
# Kc, fighting
def clock_attack():
    while True:
        if fight_seen == 0:
            print("what is that...?")
            print("You stare at the weird clock figure, it is familiar yet completely new to you.")
            print("he attacks")
            print("???")
            fight_seen += 1
        print("HP:", player["hp"])
        print("SANITY: ", player["sanity"])
        fight_enemy = rand.choice(fight_choices)
        fight_turn = input("would you like to defend, attack or items") .lower() .strip()
        if fight_turn == "defend":
            print("you defended")
            if fight_enemy == "defend":
                print("you both somehow defend, giving you a headache... ")
                player["sanity"] -= 10
                print("SANITY dropped")
            elif fight_enemy == "attack":
                print("the entity attacked")
                print("reduced damage...")
                player["hp"] -= 2
            elif fight_enemy == "sanity":
                print("You tried to defend yet the clocks chimed")
                player["sanity"] -= 20
                print("SANITY fell a lot...")
            
    



# Kc, bug fixing and helping everyone
# Kc, inventory open function
inventory_look = ""
inventory_grab = ""
def inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained):
    inventory_look = input("Would you like to open your inventory?").lower().strip()
    if inventory_look == "yes":
        print(str(player["inventory"]).replace("[", "").replace("]", "").replace(",", ""))
        time.sleep(1)
        inventory_grab = input("What item would you like to use? ").lower().strip()
        if inventory_grab == "duck":
            if duck_obtained == 0:
                print("You do not have that item.")
            else:
                print("You squeezed the duck!")
                time.sleep(1)
                print("*SQUEEK!*")
                time.sleep(1)
                player["sanity"] += 20
                print("SANITY went up!")
                print("sanity levels: ", player["sanity"])
        elif inventory_grab == "bow":
            if bow_obtained == 0:
                print("You do not have that item.")
            else:
                print("You held the bow and remembered your childhood")
                time.sleep(1)
                print("~childhood....~")
                time.sleep(1)
                player["sanity"] += 20
                print("SANITY went up!")
                print("sanity levels: ", player["sanity"])
        elif inventory_grab == "key 1":
            print("it is a key, most likely unlocks a lock")
        elif inventory_grab == "key 2":
            print("It is a key, maybe it could unlock a certain place...")
        else:
            print("You do not have that item.")
            
    

#VC storyline/instructions
print("""
You wake up in a house with a headache. Thinking you're at home you get up to look around. You soon realize that this is not your home; you do not know where you are. 
Your job now is to find a way out through exploring the building.
""")

#SP first room
def room1(move):
    while True:
        time.sleep(1)
        print("You look in front of you and there is only one door. You open it and hiding behind it you find a long, spiral staircase.")
        while True:
            move = input("Do you want to go UP the stairs or DOWN the stairs?").lower().strip()
            if move == "up":
                return 2
            elif move == "down":
                return 3
            else:
                print("That's not a choice, choose up or down:")

    
#SP second choice
def room2(move):
    while True:
        print("You find two different doors, one is BLACK and from it hangs a single, empty picture frame. The second one is PINK with a bow and next to the black door.")
        move = input("Which door do you enter?: ").lower().strip()
        if move == "pink":
            return 4
        elif move == "black":
            return 6
        elif move == "back":
            return 1
        else:
            print("That is not a valid choice, pick PINK or BLACK: ")
        
    


#VC third choice
def room3(duck_obtained, player, move):
    while True:
        if duck_obtained == 0:
            print("You walk in and the stench of chlorine hits you like a truck. You feel your forehead getting damp and itchy with sweat, and see strange circular pools all over the cold, tiled floor. In the central pool you see a rubber duck.")
            move = input("Do you pick up the rubber duck YES or NO?: ").lower().strip()
            if move == "yes":
                player["inventory"].append("duck")
                duck_obtained += 1
                print("You got a duck, quack!")
            elif move == "no":
                print("You left the duck...sad")
            else:
                print("That is not an answer, pick YES or NO: ")
        else:
            print("You see a door at the end of the room.")
            move = input("Do you run to it YES or NO?: ")
            if move == "yes":
                return 6
            if move == "no":
                return 3
            else:
                print("That is not a valid choice, pick YES or NO:")


#SP 4th room
def room4(bow_obtained, move,):
    while True:
        if bow_obtained == 0:
            print("You walk into a room that is filled with hello kitty plushies. The lightbulbs glow and you feel warm inside. There is a large pink bow in the middle of the room.")
            move = input("Do you pick up the bow YES or NO?:").lower().strip()
            if move == "yes":
                player["inventory"].append("bow")
                bow_obtained += 1
                print("You got a bow!")
            elif move == "no":
                print("You left the bow, why..?")
            else:
                print("That is not a valid choice, pick YES or NO:")
        else:
            print("you see a door.")
            move = input("Do you want to go through the door? YES or NO?: ")
            if move == "yes":
                return 7
            if move == "no":
                return 4

def room5(move):
    while True:
     print("You walk into a room filled to the brim with clocks. Big clocks, small clocks. Clocks that tick backwards and three steps at a time...")
     move = input("As you keep walking through, you see a door at the end. It looks plain and old. Will you go through? YES or NO?: ")
     if move == "yes":
         return 8
     if move == "no":
         return 5

    



def room6(move):
    while True:
        print("You walk into a completely black room. The walls are covered in empty picture frames, but from the corner of your eye you see entities in the frames. They are gone by the time you turn your head, and you feel yourself slowly spiraling.")
        
        
        

    



 #SP 7th room   
def room7(move, key1_obtained, player,):
    while True:
        if key1_obtained == 0:
            print("You walk through a hallway and see a door with a damaged clock on the front. Something glistens under the clock. You crouch down to look, and see it's some sort of key.")
            move = input("Do you pick up the key YES or NO?:").lower().strip()
            if move == "yes":
                player["inventory"].append("key 1")
                key1_obtained += 1
                print("You got a key! To what it leads is a mystery...")
            elif move == "no":
                print("You left the key behind.")
            else:
                print("That is not a valid choice, pick YES or NO:")
        else:
            print("Moving on from the clock, you run into the door.")
            move = input(" do you want to go through the door? YES or NO?: ")
            if move == "yes":
                return 5
            if move == "no":
                if key1_obtained:
                    return 7
            
    
#VC 8th room
def room8(move, key2_obtained, player,):
    while True:
        if key2_obtained == 0:
            print("You walk through to see a big hallway leading down to a door. A plant sits beside the the left corner of the hallway. Something shiny under the plant catches your eye. You get closer and see a key.")
            move = input("Do you pick up the key, YES or NO?:")
            if move == "yes":
                player["inventory"].append("key 2")
                key2_obtained += 1
                print("You got a key! To what it leads is a mystery...")
            elif move == "no":
                print("You left the key behind.")
            else:
                print("That is not a valid choice, pick YES or NO:")
        else:
            print("Moving on from the clock, you run into the door.")
            move = input(" do you want to go through the door? YES or NO?: ")
            if move == "yes":
                return 9
            if move == "no":
                if key2_obtained:
                     return 8

    
#VC 9th room
def room9():
    print("You stumble into a room completely covered in marble. The light is blinding, but you can't find its source.")
    move = input("Do you proceed? YES or NO:")
    if move == "yes":
        print("You've successfully escaped...or have you?")
    elif move == "no":
        return 10


# kc, the thing that calls all the functions
while True:
    if player["sanity"] == 0:
        print("Insanity took your life. GAME OVER")
    print("sanity level:", player["sanity"])
    player["sanity"] -= 10
    time.sleep(1)
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
        current_room = room8()
    elif current_room == 9:
        current_room = room9()
    elif current_room == 10:
        current_room = print("you escaped, at last.")
        