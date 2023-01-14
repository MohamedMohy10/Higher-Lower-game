from art import logo, vs
from data import data
import random
import os

def check_answer(account_a,account_b,answer,score): #Checks user response and scores
    os.system('cls')
    print(logo)
    print(f"{account_a['name']} has {account_a['follower_count']}M followers ")
    print(f"{account_b['name']} has {account_b['follower_count']}M followers\n")
    if (answer == 'a' and account_a['follower_count'] >= account_b['follower_count']) or (answer == 'b' and account_b['follower_count'] >= account_a['follower_count']):
        score += 1
        print(f"You are right, current score : {score}\n")
        print("="*40)
        game(account_b,score) #continue the game with account_b which is the new value to compare with
    else:
        print(f"Wrong answer, Your final score : {score} ")
        return

def game(account_a = random.choice(data), score = 0):
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print("Compare between : \n")
    print(f"A: {account_a['name']}, a {account_a['description']} from {account_a['country']}")
    print(vs)
    print(f"B: {account_b['name']}, a {account_b['description']} from {account_b['country']}")
    answer = input("Who has more followers ? Type 'A' or 'B' : ").lower()

    check_answer(account_a,account_b,answer,score)


os.system('cls')
print(logo)

game()


