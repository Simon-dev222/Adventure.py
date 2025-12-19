print("Welcome to the Angry Goblin Hunt")
print("An award-winning game full of adventure and exitement (!)")

player_name = input("What is your Name?")
print(player_name + ",can you find the Goblin?")

print("|_| |_| |_| |_| |_|")

goblin_position1 = 3
goblin_position2 = 2
goblin_position3 = 1



guessed_position = input("Can you guess where the Goblin is hiding?")
guessed_position = int(guessed_position)

if guessed_position ==goblin_position1:
    print("Youve found the Goblin.")
    print("Choose a weapon to fight the Goblin")

    print("|_| |_|")
    weapon_1 = 1
    weapon_2 = 2

    guessed_weapon = input   ("what weapon will you choose?")
    guessed_weapon = int(guessed_weapon)
    if guessed_weapon ==weapon_1:
        print(player_name +",your weapon will be the Axe.")
    if guessed_weapon ==weapon_2:
        print(player_name +",your weapon will be the Sword.")    

if guessed_position ==goblin_position2:
    print("No, sorry. The Goblin is still hiding somewhere.")    
if guessed_position ==goblin_position3:
    print("Goblin isnt here. Try again")