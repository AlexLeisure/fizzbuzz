# This program will play the game "fizzbuzz".
# Fizzbuzz is a game where 2 players will count from 1 to some number.
# Every time player one encounters a number that is divisible by 3, they will say "fizz".
# Every time player 2 encounters a number divisible by 5, they will say "buzz".
# When the number is divisible by both 3 AND 5, they will both say "fizzbuzz"

numCount = 100


def play_fizz_buzz():
    # An important part of software development is thinking about what will change over time,
    # and designing code so that it's easy to change when that time comes. This solution
    # makes changing the intervals for fizz and buzz very easy and also reduces repetition.
    for i in range(1, numCount+1):
        output = ""
        if i%3 == 0:
            output += "fizz"
        if i%5 == 0:
            output += "buzz"
        if output == "":
            output += str(i)
        print(output)



play_fizz_buzz()
