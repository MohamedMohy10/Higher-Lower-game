from art import logo, vs
from data import data
import random
import os


def check_answer(account_a,account_b,answer,score):
    """Checks the user's response and calculates scores, also displays them"""
    #clear the screen :
    os.system('cls') 
    print(logo)
    #Show results:
    print(f"{account_a['name']} has {account_a['follower_count']}M followers ")
    print(f"{account_b['name']} has {account_b['follower_count']}M followers\n")
    #check the user's answer:
    if (answer == 'a' and account_a['follower_count'] >= account_b['follower_count']) or (answer == 'b' and account_b['follower_count'] >= account_a['follower_count']):
        # The user answer is right
        score += 1
        print(f"You are right, current score : {score}\n") #show user's score after increasing
        print("="*40)
        game(account_b,score) #continue the game, but with the value of account_b as 'account_a' in the next round
    else: #wrong answer
        print(f"Wrong answer, Your final score : {score} ") #show the final score
        return #the user loses ==> exit the game
    

def game(account_a = random.choice(data), score = 0): 
    """The main game, generates random values and asks the user for input
    -Default: begins with assigning a random value to account_a from the data , and begins with score = 0 """
    account_b = random.choice(data) # choosing a random value for account_b
    if account_a == account_b:
        account_b = random.choice(data)
    #Comparison and displaying accounts information 
    print("Compare between : \n")
    print(f"A: {account_a['name']}, a {account_a['description']} from {account_a['country']}")
    print(vs) #art
    print(f"B: {account_b['name']}, a {account_b['description']} from {account_b['country']}")
    # getting response from user:
    answer = input("Who has more followers ? Type 'A' or 'B' : ").lower()
    #checking user's answer with the check_answer function
    check_answer(account_a,account_b,answer,score)


os.system('cls') #clear the screen
print(logo) #printing the logo

game()


