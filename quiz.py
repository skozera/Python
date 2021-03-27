# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:31:00 2021
"""

import random
import time

level = 1
score = 1 # inittial points
rounds = 10 # how many rounds do you want to play
limit = 30 # max result of addition or subtraction
prize = 10 # points for every corect oraz uncorrect (with minus) answear
timetotal = 0

def start_game(limit, rounds, prize):
    start = input(f"Wykonaj {rounds} zadań z dodawania i odejmowania do {limit}.\r\nOtrzymasz {prize} punktów za każdą prawidłową odpowiedź.\r\n\r\nNaciśnij ENTER, aby rozpocząć zadania...")
    quiz = level_one(limit)
    print("\r\n-- PODSUMOWANIE --")
    print("Punktów:", str(quiz[0])+'/'+str(rounds*prize), "\r\nCzas wykonania:", str(format(quiz[1], '.1f')) + " sek.")

def level_one(limit):
    
    def print_time(end, start):
        return str(format(end-start, '.1f')) + " sek."
    
    def get_answear(response, answear, start, end):
                
            global score
            global rounds
            global prize
            global timetotal
            global limit
            
            rounds -= 1
            
            if int(response) == answear:
                score += prize
                timetotal += end-start
                print(prize, 'pkt. /', str(format(end-start, '.1f')) + " sek.")
                level_one(limit)
            else:
                timetotal += end-start
                print('0 pkt. /', str(format(end-start, '.1f')) + " sek.")
                level_one(limit)

    while rounds > 0:
        
        random_operator = random.choice(["+", "-"])
        start = time.time()

        if random_operator == "+":
            first_number = random.randint(1, limit/2)
            second_number = random.randint(1, limit/2)
            response = input(f"{rounds}) {first_number} + {second_number}: ")
            end = time.time()
            answear = first_number + second_number
            get_answear(response, answear, start, end)

        else:
            first_number = random.randint(1, limit)
            second_number = random.randint(1, first_number)
            response = input(f"{rounds}) {first_number} - {second_number}: ") 
            end = time.time()
            answear = first_number - second_number
            get_answear(response, answear, start, end)
    
    #summary
    return [score-1, timetotal]
    

# def main():

# if __name__ = "__main__":
#     main()

start_game(limit, rounds, prize)
