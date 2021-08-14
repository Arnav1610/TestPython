import random

print("Hi, we are going to play rock, paper, scissors!")

cpu_choices = ["rock", "paper", "scissor"]
cpu_choice = random.choice(cpu_choices)

user_choice = input("Chose: Rock, Paper or Scissor - ")
user_choice = user_choice.lower()

if cpu_choice == user_choice:
    print(f"It is a tie. I chose {cpu_choice} too. ")

elif cpu_choices.index(user_choice) == 0 and cpu_choices.index(cpu_choice) == 1:
    print("You lost! I chose Paper. ")

elif cpu_choices.index(cpu_choice) == 0 and cpu_choices.index(user_choice) == 1:
    print("You won. I chose Rock. ")

elif cpu_choices.index(user_choice) == 1 and cpu_choices.index(cpu_choice) == 2:
    print("You lost! I chose Scissor")

elif cpu_choices.index(cpu_choice) == 1 and cpu_choices.index(user_choice) == 2:
    print("You win. I chose paper")

elif cpu_choices.index(user_choice) == 2 and cpu_choices.index(cpu_choice) == 0:
    print("You lose! I chose rock")

elif cpu_choices.index(cpu_choice) == 2 and cpu_choices.index(user_choice) == 0:
    print("You win. I chose scissors.")