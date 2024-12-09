print("/// Welcome to Rock Paper Scissors Game ///")
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
image = [rock, paper, scissors]
i_choose = int(input("Choose 0 for Rock , 1 for Paper and 2 for Scissors\n"))
print(f"I Choose: {i_choose}", image[i_choose])

computer = random.randint(0, 2)
print(f"Computer Choose: {computer}", image[computer])

if i_choose >2 or i_choose <0:
    print(f"You choose {i_choose}, which is invalid!")
elif i_choose ==0 and computer == 2:
    print("Yeahooo! I win.")
elif computer == 2 and i_choose== 0:
    print("Opps! You lose.")
elif computer > i_choose:
    print("Opps! You lose.")
elif i_choose > computer:
    print("Yeahooo! I win.")
elif computer == i_choose:
    print("What a nice play. It's a drow!")