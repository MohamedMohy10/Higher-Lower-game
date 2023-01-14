from art import logo, vs
from data import data
import random
import os

def game(a,score):
    b = random.choice(data)
    print(f"COMPARE :\nA: {a['name']}, a {a['description']} from {a['country']}")
    print(vs)
    print(f"B: {b['name']}, a {b['description']} from {b['country']}")
    answer = input("Who has more followers ? Type 'A' or 'B' : ").lower()
    if (answer == 'a' and a['follower_count'] >= b['follower_count']) or (answer == 'b' and b['follower_count'] >= a['follower_count']):
        score += 1
        os.system('cls')
        print(logo)
        print(f"{a['name']} has {a['follower_count']}M followers ")
        print(f"{b['name']} has {b['follower_count']}M followers\n")
        print(f"You are right, current score : {score}")
        game(b,score)
    else:
        os.system('cls')
        print(logo)
        print(f"{a['name']} has {a['follower_count']}M followers ")
        print(f"{b['name']} has {b['follower_count']}M followers\n")
        print(f"Wrong answer, Your final score : {score} ")
        return

score = 0
os.system('cls')
a = random.choice(data)
print(logo)

game(a,score)


