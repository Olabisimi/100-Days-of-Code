import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Declare variable for the images
Game_images = [rock, paper, scissors]
# Ask for the players choice and convert to integer
Player_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, "
                           "2 for Scissors \n"))
# Declare Variable for the computer choice
# it should be random int between 0 and 2
Computer_choice = random.randint(0, 2)
print("Computer_choice is :")
# Represent Computer choice as image
print(Game_images[Computer_choice])
#Represent Computer choice as image
if Player_choice >= 0 and Computer_choice <=2:
    print (Game_images[Player_choice])
if Player_choice >= 3 or Player_choice < 0:
    print("Not Valid")
elif Player_choice == 0 and Computer_choice == 2:
    print("Player wins ")
elif Computer_choice == 0 and Player_choice == 2:
    print("Computer wins")
elif Computer_choice == Player_choice:
    print("That's a draw")
elif Computer_choice > Player_choice:
    print("Computer wins")
elif Player_choice > Computer_choice:
    print("Player wins")