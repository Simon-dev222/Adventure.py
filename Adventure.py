print("The wind carries the echo of a forgotten era through the narrow streets as the sun slowly sinks behind the jagged peaks.")
print("You stand on the threshold of a place that doesn't appear on any map.")
print("In your pocket rests an ancient parchment, its seal broken only this morning—and with it, the silence of the last hundred years.")
print("Your heartbeat sets the pace: there is no turning back.")

player_name = input("Whats your name?")
print(player_name + ", welcome to an epic adventure full of mysteries and danger")

Hero_class1 = 1
Hero_class2 = 2
Hero_class3 = 3
Hero_class4 = 4

print("Please choose your class for this adventure.")
print("1. Paladin")
print("2. Barbarian")
print("3. Cleric")
print("4. Mage")
print("|_| |_| |_| |_|")

guessed_Hero_class = input("Please select your Class.")
guessed_Hero_class = int(guessed_Hero_class)

if guessed_Hero_class ==Hero_class1:
    print("Youve choosen the Paladin.")
    print("A paladin is a melee fighter who wears heavy armor (plate) and uses divine powers to support allies or punish enemies.")

if guessed_Hero_class == Hero_class2:
    print("Youve choosen the Barbarian.") 
    print("In contrast to the paladin, who is guided by moral oaths and divine magic, the barbarian follows his animal instincts and the primal force of his rage.")

if guessed_Hero_class == Hero_class3:
    print("Youve choosen the Cleric.")    
    print("The cleric is a divine magician who acts as an intermediary between the mortal world and the gods.")
if guessed_Hero_class == Hero_class4:
    print("Youve choosen the Mage")   
    print("The mage (often also spell wizard or mage) is the epitome of the intellectual magic user who manipulates reality through years of study and arcane arts.")   
    



