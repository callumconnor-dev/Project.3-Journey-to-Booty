print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

health = 100

while not health == 0:
    direction = input("You arrive at Treasure Island. For the sake of the tutorial, you can only go forward, despite it being an island. Type 'forward' to proceed.\n").lower()
    if direction == "forward":
        print("You walk through a dense jungle.")
        direction = input("You see a river blocking your path. Do you want to swim across or look for a bridge? Type 'swim' or 'bridge'.\n").lower()
        if direction == "swim":
            print("Dense Jungle + River + You = Dead.")
            health = 0
            break
        elif direction == "bridge":
            print("You find a sturdy bridge and cross it.")

        direction = input("You come across a fork in the road. Do you want to go left or right? Type 'left' or 'right'.\n").lower()
        if direction == "left":
            print("You take the left path and find a hidden cave.")
        elif direction == "right":
            print("You take the right path and encounter a wild beast.")
            health -= 50
            print("The beast attacks you, and your health decreases by 50.")
            print("You run ahead and find a hidden cave.")

        while True:
            direction = input("Inside the cave, you see three tunnels. Which tunnel do you want to explore? Type '1', '2', or '3'.\n").lower()
            if direction == "1":
                print("You enter the first tunnel and discover a secret chamber with ancient artifacts. You turn back.")
                
            elif direction == "2":
                print("You enter the second tunnel and encounter a booby trap. You narrowly escape, losing 25 Health.")
                health -= 25
                
            elif direction == "3":
                print("You enter the third tunnel and find the hidden treasure!")
                direction = input("As you leave the cave with the treasure, you hear a rumbling sound. Do you want to run or hide? Type 'run' or 'hide'.\n").lower()
                if direction == "run":
                    print("You sprint towards safety and manage to evade the danger.")
                    print("Congratulations! You have completed your mission.")
                    exit()
                elif direction == "hide":
                    print("You get crushed by the ceiling caving in on itself.")
                    health = 0
                
            else:
                print("Invalid input. Please try again.")

    else:
        print("There's a certain degree that I can be arsed programming. I'm not fixing your mistake, just restart.\n\n\n")

if health == 0:
    print("You died. Better luck next time.")




