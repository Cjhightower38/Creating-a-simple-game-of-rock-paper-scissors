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

#Write your code below this line 👇
import random
hand_gestures=[rock, paper, scissors]

player_hand_gestures=[rock, paper, scissors]

player=int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n"))
print("Player's choice ")
# (list[len(list)-1]) stops the list from error when a player chooses a number out of range.
print(player_hand_gestures[len(player_hand_gestures) -1])

cpu=random.randint(0,2)

'''
cpu=random.choice(hand_gestures) will allow for a random cpu choice but when it is compared 
against the players int\str occurs because random.choice will print the item from the list
in str form while the player's will print in int form which is what was asked for in the 
question 0 = rock, 1 = paper, and 2 = scissors.

'''
print("Computer's choice ")
print(hand_gestures[cpu])

if player >=3 or player < 0:
  print('Sorry this number is incorrect you lose.')
elif player == cpu:
  print("It's a draw!")
elif player == 0 and cpu == 1:
  print('You lose!')
elif player == 1 and cpu == 2:
  print('You lose!')
elif player == 2 and cpu == 0:
  print('You lose!')
elif cpu == 0 and player == 1:
  print('You win!')
elif cpu == 1 and player == 2:
  print('You win!')
elif cpu == 2 and player == 0:
  print('You win!')