# This program will play the game "fizzbuzz".
# Fizzbuzz is a game where 2 players will
# will count from 1 to some number. Every
# time player one encounters a number that
# is divisible by 3, they will say "fizz".
# Every time player 2 encounters a number
# divisible by 5, they will say "buzz".
# When the number is divisible by both
# 3 AND 5, they will both say "fizzbuzz"

numCount = 100


def play_fizz_buzz():
    for i in range(1, numCount+1):
        #just gonna try 3 if statements first

        if i%3 == 0 and i%5 != 0:
            print("fizz")
        elif i%3 != 0 and i%5 == 0:
            print("buzz")
        elif i%3 == 0 and i%5 == 0:
            print("fizzbuzz!")
        else:
            print(i)


play_fizz_buzz()
