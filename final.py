# KC, SP, VC, LV, text based adventure game
import random
from random import SystemRandom
import time


#kc, stats of player and enemy.
#LV, wrote descriptions and set the story.

player = {  
    "hp": 50,
    "attack": 10,
    "sanity": 100,
    "inventory": []
}

clock_enemy = {
    "hp": 137,
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

key1_obtained = 0
key2_obtained = 0
# Kc, inventory open function
inventory_look = ""
inventory_grab = ""
def inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained):
    inventory_look = input("Would you like to open your inventory?").lower().strip()
    while True:
        if inventory_look == "yes":
            print(str(player["inventory"]).replace("[", "").replace("]", "").replace("'", ""))
            if str(player["inventory"]).replace("[", "").replace("]", "").replace(",", "") == "":
                print("You do not have anything in your inventory.")
                time.sleep(1)
                return
            time.sleep(1)
            inventory_grab = input("What item would you like to use, or would you like to CLOSE inventory? ").lower().strip()
            if inventory_grab == "duck":
                if "duck" not in player["inventory"]:
                    print("You do not have that item.")
                else:
                    print("You squeezed the duck!")
                    time.sleep(1)
                    print("*SQUEEK!*")
                    time.sleep(1)
                    player["sanity"] += 20
                    print("SANITY went up!")
                    print("Sanity levels: ", player["sanity"])
                    player["inventory"].remove("duck")
            elif inventory_grab == "bow":
                if "bow" not in player["inventory"]:
                    print("You do not have that item.")
                else:
                    print("You held the bow and remembered your childhood.")
                    time.sleep(1)
                    print("childhood...")
                    time.sleep(1)
                    player["sanity"] += 20
                    print("SANITY went up!")
                    print("sanity levels: ", player["sanity"])
                    player["inventory"].remove("bow")
            elif inventory_grab == "get out of my head":
                while True:
                    print("get out of my head")
            elif inventory_grab == "key 1":
                if "key 1" in player["inventory"]:
                    print("It is a key, it most likely unlocks a lock")
                else:
                    print("You don't have that item")
            elif inventory_grab == "key 2":
                if "key 2" in player["inventory"]:
                    print("It is a key, maybe it could unlock a certain place...")
                else:
                    print("You don't have that item.")
            elif inventory_grab == "close":
                print("Inventory closed.")
                return
            else:
                print("You do not have that item.")
        elif inventory_look == "no":
            print("Inventory closed.")
            time.sleep(1)
            return



three_four = 0
attack_won = 0
lost_attack = 0

# Kc, fighting
def clock_attack(player, clock_enemy, fight_enemy, fight_turn, lost_attack, attack_won):
    print("What is that...?")
    print("You glare at the clock figure as its shadow closes in and the ticking grows louder. It is a familiar sensation, yet you know you have never experienced something like this before.")
    print("It Attacks.")
    while True:
        if player["sanity"] <= 0:
            print("Insanity took your life.")
            lost_attack = 1
            return
        if player["hp"] <= 0:
            print("You have died.")
            lost_attack = 1
            return
        if clock_enemy["hp"] <= 0:
            print("The clockwork finally faltered.")
            return
        print("??? HP:", clock_enemy["hp"])
        print("HP:", player["hp"])
        print("SANITY: ", player["sanity"])
        fight_enemy = rand.choice(fight_choices)
        fight_turn = input("Would you like to DEFEND, ATTACK or use ITEM?") .lower().strip()
        if fight_turn == "defend":
            print("You try defending yourself...")
            if fight_enemy == "defend":
                print("You both choose to act defensive, giving you a headache as you anticipate a strike...")
                player["sanity"] -= 10
                print("SANITY dropped")
            elif fight_enemy == "attack":
                print("The entity attacked and got past your defense.")
                print("Reduced damage...")
                player["hp"] -= 2
            elif fight_enemy == "sanity":
                print("You tried to help yourself, yet the chiming would not cease...")
                player["sanity"] -= 20
                print("SANITY fell... by a lot.")
        elif fight_turn == "attack":
            if fight_enemy == "defend":
                print("You tried to hit, but it was too agile for your attack.")
                print("The entity lost no HP.")
            elif fight_enemy == "attack":
                print("Both parties attacked.")
                player["hp"] -= 5
                clock_enemy["hp"] -= 10
            elif fight_enemy == "sanity":
                print("You caught the entity off guard, and managed to land a hit.")
                clock_enemy["hp"] -= 20
        elif fight_turn == "item":
            inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
            if fight_enemy == "defend":
                print("It retreats, but you are not in the clear just yet...")
                player["sanity"] -= 5
            elif fight_enemy == "attack":
                print("You look back, only to be met with its ambush.")
                player["hp"] -= 5
            elif fight_enemy == "sanity":
                print("You want to go back. You need to go back. Yet it feels like you can't.")
                player["sanity"] -= 20
        elif fight_turn == "kill thy enemy":
            clock_enemy["hp"] -= 4328743287032
            print("CHEATER")
            
            

# Kc, bug fixing and helping everyone and doing fixing many many issues. also doing tiny changes to everything.


#VC storyline/instructions
print("""
You wake up in a house with a headache. Thinking you're at home you get up to look around. You soon realize that this is not your home; you do not know where you are. 
Your job now is to find a way out through exploring the structure.
""")

#SP first room
def room1(move):
    print("You look in front of you and there is only one door. You open it and hiding behind it you find a long, spiral staircase.")
    while True:
        time.sleep(1)
        move = input("Do you want to go UP the stairs, DOWN the stairs, or open your (INV)entory?: ").lower().strip()
        if move == "up":
            return 2
        elif move == "down":
            return 10    
        elif move == "inv":
            inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
        else:
            print("That is not a choice, choose UP, DOWN, or INV: ")

three_four = 0
#SP second choice
def room2(move):
    if three_four >= 2:
        print("You remembered you saw two different doors last time, one black, the other pink.")
    else:
        print("You find two different doors, one is BLACK and from it hangs a single, empty picture frame. The second one is PINK, its paint slowly yellowing and peeling off.")
    while True:
        print(three_four)
        time.sleep(1)
        if three_four == 3:
            print("It seems like the pink door vanished from the last time you went...")
            move = input("Do you open the PINK door, go BACK to the first room, or open (INV)entory?: ").lower().strip()
            if move == "pink":
                return 4
            elif move == "back":
                return 1
            elif move == "inv":
                    inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
        
        elif three_four == 4:
            print("It seems like the black door vanished from the last time you went...")
            move = input("Do you open the BLACK door, go BACK to the first room, or open (INV)entory?: ").lower().strip()
            if move == "black":
                return 6
            elif move == "back":
                return 1
            elif move == "inventory":
                    inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
        else:
            move = input("Do you enter the PINK door, the BLACK door, or go BACK? Or, do you look at your (INV)entory?: ").lower().strip()
            if move == "pink":
                return 4
            elif move == "black":
                return 6
            elif move == "back":
                return 1
            elif move == "inv":
                    inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
            else:
                print("That is not a valid choice, pick the PINK or BLACK door, go BACK or open INV: ")

bow_not_obtained = 0
duck_not_obtained = 0
#VC third choice
def room3(duck_obtained, player, move, three_four, duck_not_obtained):
    print("You walk in and the stench of chlorine hits you like a truck. You feel your forehead getting damp and itchy with sweat, and see strange circular pools all over the cold, tiled floor. In the central pool you spot a rubber duck.")
    while True:
        if three_four != 3:
            three_four = 3
        if duck_obtained == 0:
            if duck_not_obtained == 0:
                time.sleep(1)
                move = input("Do you pick up the rubber duck YES or NO?: ").lower().strip()
                if move == "yes":
                    player["inventory"].append("duck")
                    duck_obtained += 1
                    print("You got a duck, quack!")
                elif move == "no":
                    print("You left the duck...sad")
                    duck_not_obtained += 1
                else:
                    print("That is not an answer, pick YES or NO: ")
            else:
                print("You watch as the duck floats away.")
                print("You see a door at the end of the room.")
                time.sleep(1)
                move = input("Do you run to it (YES), go BACK, or open (INV)entory?: ")
                if move == "yes":
                    return 7
                if move == "back":
                    return 2
                elif move == "inv":
                    inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
                else:
                    print("That is not a valid choice, pick YES or NO: ")

        else:
            print("You see a door at the end of the room.")
            time.sleep(1)
            move = input("Do you run to it (YES), go BACK, or open (INV)entory?: ")
            if move == "yes":
                return 7
            if move == "back":
                return 2
            elif move == "inv":
                inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
            else:
                print("That is not a valid choice, pick YES, BACK, or INV: ")


#SP 4th room
def room4(bow_obtained, move, player, three_four, bow_not_obtained):
    print("You walk into a room that is filled with plushies and love..? The incandescent lightbulbs glow and you feel warm inside. There is a large pink bow in the middle of the room.")
    while True:
        if three_four != 4:
            three_four = 4
        if bow_obtained == 0:
            if bow_not_obtained == 0:
                time.sleep(1)
                move = input("Do you pick up the bow YES or NO?: ").lower().strip()
                if move == "yes":
                    player["inventory"].append("bow")
                    bow_obtained += 1
                    print("You got a bow!")
                elif move == "no":
                    print("You left the bow behind...")
                    bow_not_obtained = 1
                else:
                    print("That is not a valid choice, pick YES or NO: ")
            else:
                print("The bow disappeared, you wonder where it went.")
                print("You stay at this strange yet comforting place for a while, and then you see a door.")
                time.sleep(1)
                move = input("Do you leave this place (YES), go BACK, or open (INV)entory?: ").lower().strip()
                if move == "yes":
                    return 7
                elif move == "back":
                    return 2
                elif move == "inv":
                    inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
                else:
                    print("That is not a valid choice, pick YES to leave, BACK, or INV: ")
        else:
            print("You stay at this strange yet comforting place for a while, and then you see a door.")
            time.sleep(1)
            move = input("Do you go through the door (YES), go BACK, or open (INV)entory?: ")
            if move == "yes":
                return 7
            if move == "back":
                return 2
            elif move == "inv":
                inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
            else:
                print("That is not a valid choice, pick YES, BACK, or INV: ")



#VC 5th room
def room5(move, lost_attack):
    print("You walk into a room filled to the brim with clocks. Big clocks, small clocks. Clocks that tick backwards and three steps at a time...")
    while True:
        if attack_won == 0:
            clock_attack(player, clock_enemy, fight_enemy, fight_turn, lost_attack, attack_won)
            attack_won = 1
        else:
            if lost_attack == 1:
                return 12
            move = input("As you keep walking through, you see a door at the end. It looks plain and old. Will you go through (YES), retreat (BACK), or open (INV)entory?: ") .lower() .strip()
            if move == "yes":
                return 8
            if move == "back":
                return 7
            elif move == "inv":
                inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
            else:
                print("That is not a valid choice, pick YES, BACK, or INV: ")





#VC 6th room
def room6(move):
    print("You walk into a completely black room. The walls are covered in empty picture frames, but from the corner of your eye you see entities in the frames. They are gone by the time you turn your head and you feel yourself slowly spiraling.")
    while True:
        time.sleep(1.5)
        print("You keep walking through, and feel familiarity to the picture frames. It's almost as if you've already been here, but you haven't. Soon you reach the end, and are met with a blue door stained from moisture.")
        while True:
            time.sleep(1)
            move = input("Do you keep walking through this room (YES), go BACK, or open your (INV)entory?: ").strip() .lower()
            if move == "yes":
                return 3
            elif move == "no":
                return 6   
            elif move == "back":
                return 2
            elif move == "inv":
                    inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)  
            else:
                    print("That is not a valid choice, pick YES, BACK, or INV: ")

   
        


 #SP 7th room   
def room7(move, key1_obtained, player,):
    print("You walk through a hallway and see a door, but not before spotting a damaged clock and its weak, marching ticks. Something glistens under the clock. You crouch down to look, and see something small.")
    while True:
        time.sleep(1)
        if key1_obtained == 0:
            move = input("Do you pick up the item YES or NO?: ").lower().strip()
            if move == "yes":
                player["inventory"].append("key 1")
                key1_obtained += 1
                print("You found a key! To what it leads is a mystery...")
            elif move == "no":
                print("You left the item behind, I wonder what it was.")
            else:
                print("That is not a valid choice, pick YES or NO:")
        else:
            print("Moving on from the clock, you run into the door.")
            time.sleep(1)
            move = input("Do you open the door (YES), run BACK, or open (INV)entory?: ") .lower() .strip()
            if move == "yes":
                return 5
            elif move == "back":
                if three_four == 3:
                    return 3
                if three_four == 4:
                    return 4
            elif move == "inv":
                inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
            else:
                print("That is not a valid choice, pick YES, BACK, or INV: ")


    
#VC 8th room
def room8(move, key2_obtained, player,):
    print("You walk through to see a nearly endless hallway leading down to a single door. A wilting plant sits askew beside the the left corner of the hallway. A gray, dusty object under the pot catches your eye.")
    while True:
        if key2_obtained == 0:
            time.sleep(1)
            move = input("Do you pick up the object YES or NO?: ") .lower() .strip()
            if move == "yes":
                player["inventory"].append("key 2")
                key2_obtained += 1
                print("You got a key! To what it leads is a mystery...")
            elif move == "no":
                print("You walked past the plant without looking.")
            else:
                print("That is not a valid choice, pick YES or NO: ")
        else:
            print("Moving with haste through the hallway, you finally meet the door.")
            time.sleep(1)
            move = input("Do you go through this door (YES), go BACK, or open (INV)entory?: ") .lower() .strip()
            if move == "yes":
                return 9
            elif move == "back":
                return 5
            elif move == "inv":
                inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
            else:
                print("That is not a valid choice, pick YES, BACK, or INV: ")



    
#VC 9th room   
def room9(move):
    print("You stumble into a room completely covered in marble. The light is blinding, but you can't find its source.")
    while True:
        time.sleep(1)
        move = input("Do you proceed (YES), go BACK, or open (INV)entory?: ") .lower().strip()
        if move == "yes":
            print("You've successfully escaped...or have you?")
            return 11
        elif move == "back":
            return 8
        elif move == "inv":
            inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
        else:
            print("That is not a valid choice, pick YES, BACK, or INV: ")



  #SP room 10th      
def room10(move):
    print("You walk into a dingy hallway. Its yellow and blue wallpaper would have been beautiful if it weren't for a mold infestation. It seems like this was last visited by a human eons ago, and the fluorescent lights flicker and turn off at unpredictable intervals...")
    print("You see a door that is oddly in pristine condition, powder white with cerulean tiles surrounding its perimeter.")
    while True:
        time.sleep(2)
        move = input(" Do you go in (YES), leave (BACK), or open (INV)entory?: ") .lower() .strip()
        if move == "yes":
            return 3
        elif move == "back":
            return 1
        elif move == "inv":
            inventory_item(inventory_look, inventory_grab, player, duck_obtained, bow_obtained)
        else:
            print("That is not a valid choice, pick YES, BACK, or (INV)entory: ")





# KC the read and write stuff
with open ("read_write.txt","r") as file: 
    content = file.read().split(",")
    wins = int(content[0])
    losses = int(content[1])
print("wins:", wins, "losses:", losses)

# KC, the thing that calls all the functions
while True:

    with open ("read_write.txt","r") as file: 
        content = file.read().split(",")
        wins = int(content[0])
        losses = int(content[1])

    if player["sanity"] == 0:
        print("Insanity took your life.")
        current_room = 12
    print("sanity level:", player["sanity"])
    player["sanity"] -= 5
    time.sleep(1)
    if current_room == 1:
        current_room = room1(move)
    elif current_room == 2:
        current_room = room2(move)
    elif current_room == 3:
        three_four = 3
        current_room = room3(duck_obtained, player, move, three_four, duck_not_obtained)
    elif current_room == 4:
        three_four = 4
        current_room = room4(bow_obtained, move, player, three_four, bow_not_obtained)
    elif current_room == 5:
        current_room = room5(move, lost_attack)
    elif current_room == 6:
        current_room = room6(move)
    elif current_room == 7:
        current_room = room7(move, key1_obtained, player,)
    elif current_room == 8:
        current_room = room8(move, key2_obtained, player,)
    elif current_room == 9:
        current_room = room9(move)
    elif current_room == 10:
        current_room = room10(move)
    elif current_room == 11:
        wins += 1
        with open("read_write.txt", "w") as file2:
            file2.write(str(wins))
        with open("read_write.txt", "a") as file2:
            file2.write(",")
            file2.write(str(losses))
        break
    elif current_room == 12:
        losses += 1
        with open("read_write.txt", "w") as file2:
            file2.write(str(wins))
        with open("read_write.txt", "a") as file2:
            file2.write(",")
            file2.write(str(losses))
        break