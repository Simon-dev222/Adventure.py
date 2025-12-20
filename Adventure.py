import random

# Basic color codes
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'  # This resets the color back to default
#   Colorsystem: 
#   Green text is Storytelling
#   Red Text is Playerinput needed
#   Blue Color isnt set yet      


# Welcome messege to the Adventure
print(f"{GREEN}The wind carries the echo of a forgotten era through the narrow streets as the sun slowly sinks behind the jagged peaks.")
print("You stand on the threshold of a place that doesn't appear on any map.")
print("In your pocket rests an ancient parchment, its seal broken only this morning—and with it, the silence of the last hundred years.")
print("Your heartbeat sets the pace: there is no turning back.")

number_of_classes = 5 # Hero classes you to play with

player_name = input(f"{RED}""Whats your name?")
print(f"{GREEN}")
print(player_name + ", welcome to an epic adventure full of mysteries and danger.") # Welcome messege to new Player

Hero_class1 = 1
Hero_class2 = 2
Hero_class3 = 3
Hero_class4 = 4

print("Please choose your class for this adventure.") # Choose your Class you wanna play with
print("1. Paladin") # Paladin
print("2. Barbarian") # Barbarian
print("3. Cleric") # Cleric
print("4. Mage") # Mage
print("|_|" * number_of_classes) # Boxes to choose the class

guessed_Hero_class = input(f"{RED}""Please select your Class.")
guessed_Hero_class = int(guessed_Hero_class)

if guessed_Hero_class ==Hero_class1: # Paladin
    print(f"{RESET}""Youve choosen the Paladin.") # Paladin Story
    print("A paladin is a melee fighter who wears heavy armor (plate) and uses divine powers to support allies or punish enemies.")
    print("Your Adventure starts in a small Tavern in a town called Ardea")
    print("Next to your table u see a man coverd in a dark green cloak")
    print("Talk to him? 1 yes. 2 no.")
    green_cloak1 = 1
    green_cloak2 = 2
    guessed_green_cloak = input("Talk to him`?")
    guessed_green_cloak = int(guessed_green_cloak)
    if guessed_green_cloak == green_cloak1:
        print("Greetings stranger")
    if guessed_green_cloak == green_cloak2:
        print("You stay at your table, listening to the music the bard is playing") 
        print("Suddenly you hear footsteps next to you. You turn arround and see the man in that green cloak coming towards you")
        print("Greetings stranger, you look like a tought man. Could you help me with a problem i have?") 
        problem1 = 1
        problem2 = 2
        guessed_problem = input("Help him?") 
        guessed_problem = int(guessed_problem)  
        if guessed_problem == problem1:
            print("Thanks a lot. Outside the tavern theres a Goblin that stole my Mace. Please bring it back to me.")
            print("Youre leaving the tavern, moving into the nearby forest.")
        if guessed_problem == problem2:
            print("You son of a B****, then im gonna Kill you right here!")    

if guessed_Hero_class == Hero_class2: # Barbarian
    print("Youve choosen the Barbarian.") # Barbarian Story
    print("In contrast to the paladin, who is guided by moral oaths and divine magic, the barbarian follows his animal instincts and the primal force of his rage.")

if guessed_Hero_class == Hero_class3: # Cleric
    print("Youve choosen the Cleric.") # Cleric Story
    print("The cleric is a divine magician who acts as an intermediary between the mortal world and the gods.")

if guessed_Hero_class == Hero_class4: # Mage
    print("Youve choosen the Mage") # Mage Story
    print("The mage (often also spell wizard or mage) is the epitome of the intellectual magic user who manipulates reality through years of study and arcane arts.")   
    




