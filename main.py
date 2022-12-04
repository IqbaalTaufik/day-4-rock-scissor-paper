import random

rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissor = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

pilihan = [rock, paper, scissor]
print("0 for rock, 1 for paper, and 2 for scissor")
choice = int(input("What your choose? "))
if choice >= 3 or choice <0:
  print("Invalid Number,Game End")
else:
  choice1 = pilihan[choice]
  
  choice2 = random.randint(0, 2)
  choicee2 = pilihan[choice2]
  
  print("your choice : ")
  print(f"{choice1}\n")
  print("==========================")
  print("Computer choice : ")
  print(f"{choicee2}\n")
  print("==========================")
  
  if choice == choice2:
    print("You both draw")
  elif choice == 0 and choice2 == 1:
    print("You Lose")
  elif choice == 1 and choice2 == 2:
    print("You Lose")
  elif choice == 2 and choice2 == 0:
    print("You Lose")
  elif choice == 2 and choice2 == 1:
    print("You Win")
  elif choice == 0 and choice2 == 2:
    print("You Win")
  elif choice == 1 and choice2 == 0:
    print("You Win")
