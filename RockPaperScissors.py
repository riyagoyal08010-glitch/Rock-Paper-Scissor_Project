import random
import time

def game():
    s = "Scissors"
    r = "Rock" 
    p = "Paper"
    a = random.choice([s , r , p])
    print("Hey!!!Welcome to the Rock-Paper-scissor Game!!!")
    b = input("Do you want to play this interesting game (yes/no): ").lower()
    if b == "yes":
        c = input("Choose what you want (s/r/p): ")
        print(f"I chose {a}")
        if c == a :
            print("Oh nooo....it's a tie")
        elif (a == r and c == s) or (a ==p and c==r) or (a==s and c==p):
            print("YOU WIN!!")
        else:
            print("You Loosseee....")
    elif b == "no":
       print("The game is terminated.....")
       return False
    else:
       print("Invalid choice")
       return True
    return True

while True:
    if not game():  # stop if user says no
        break
    again = input("Do you want to play again (yes/no): ").lower()
    if again == "no":
        print("Thank you for playing!")
        break
    elif again != "yes":
        print("Invalid choice, exiting the game.")
        break
