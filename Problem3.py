###1. Minimum Height Check

def check_height():
    minimum_height = 120
    user_height = int(input("Enter your height in cm: "))
    
    if user_height >= minimum_height:
        print("You can ride the rollercoaster!")
    else:
        print("Sorry. You can't ride the rollercoaster.")
        
###2. Choose Your Own Adventure: Treasure Island

def treasure_island_adventure():
    print("You are exploring a rainforest in search of treasure.")
    print("Legend has it that there are some buried on a nearby island.")
    
    # First choice
    choice1 = input("You come across a lake. Do you want to swim across, or wait for a boat? (swim/wait): ").lower()
    
    if choice1 == "swim":
        print("You get eaten by a hungry shark. Game over.")
        return
    elif choice1 == "wait":
        print("A boat arrives and you arrive at the island safely.")
    else:
        print("Invalid choice. Game over.")
        return
    
    # Second choice
    choice2 = input("You come to a cave. Do you want to venture inside or walk on? (venture/walk): ").lower()
    
    if choice2 == "venture":
        print("You are squished by boulders never to be seen again. Game over.")
        return
    elif choice2 == "walk":
        print("You walk on and find yourself at a crossroads.")
    else:
        print("Invalid choice. Game over.")
        return
    
    # Third choice
    choice3 = input("You're at a crossroads. Do you go left, right, or straight? (left/right/straight): ").lower()
    
    if choice3 == "left":
        print("You are trampled by a herd of wildebeest. Game over.")
        return
    elif choice3 == "straight":
        print("You get stung by a poisonous wasp. Game over.")
        return
    elif choice3 == "right":
        print("Congratulations! You find the treasure and become rich beyond your wildest dreams!")
    else:
        print("Invalid choice. Game over.")
        return
