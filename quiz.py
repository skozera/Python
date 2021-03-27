# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:31:00 2021
"""

import random
import time

level = 1
score = 1 # inittial points
rounds = 3 # how many rounds do you want to play
limit = 30 # max result of addition or subtraction
prize = 10 # points for every corect oraz uncorrect (with minus) answear

def start_game(limit):
    start = "ll"
    start = input("Please press any key to start the game")
    if start != "ll" and level == 1:
        level_one(limit)


def level_one(limit):
    global score
    global rounds
    global prize
    
    def print_time(end, start):
        return int(end-start)

    if score <= 0:
        return print("You lost!")

    while ((rounds > 0) & (score > 0)):
        
        start = time.time()
        
        answer = 0
    
        random_operator = random.choice(["+", "-"])
        if random_operator == "+":
            first_number = random.randint(1, limit/2)
            second_number = random.randint(1, limit/2)
            response = input(f"{first_number} + {second_number}: ")
            end = time.time()
            answer = first_number + second_number
            if int(response) == answer:
                
                score += prize
                rounds -= 1
                print(score, print_time(end,start))
                level_one(limit)
            else:
                score -= prize
                rounds -= 1
                print(score)
                level_one(limit)

        else:
            first_number = random.randint(1, limit)
            second_number = random.randint(1, first_number)
            response = input(f"{first_number} - {second_number}: ") 
            end = time.time()
            answer = first_number - second_number
            if int(response) == answer:
                score += prize
                rounds -= 1
                print(score, print_time(end,start))
                level_one(limit)
            else:
                score -= prize
                rounds -= 1
                print(score)
                level_one(limit)

# def main():

# if __name__ = "__main__":
#     main()

start_game(limit)
