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

# Get user input
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

# Display user's choice
if user == 0:
   print("You chose Rock:")
   print(rock)
elif user == 1:
   print("You chose Paper:")
   print(paper)
elif user == 2 :
   print("You chose Scissors:")
   print(scissors)
else:
    print("invalid choice")

# Generate computer's choice
computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")

# Display computer's choice
if computer_choice == 0:
     print("Computer chose Rock:")
     print(rock)
elif computer_choice == 1:
     print("Computer chose Paper:")
     print(paper)
else:
    print("Computer chose Scissors:")
    print(scissors)

    # Determine the outcome
if computer_choice == 0 and user == 2 or computer_choice == 2 and user == 1 or computer_choice == 1 and user == 0 :
    print("You lose !!")
elif computer_choice == user:
    print("it is tie !!")
elif user < 0 or user > 2:
    print("You typed an invalid number, you lose !!")
else :
    print("you win !!")
