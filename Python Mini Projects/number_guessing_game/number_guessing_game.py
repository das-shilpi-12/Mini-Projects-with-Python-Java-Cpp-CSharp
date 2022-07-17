'''NUMBER GUESSING GAME'''
import random
import math
#taking inputs
lower = int(input("***Enter your lower bound***: "))
upper = int(input("***Enter your upper bound***: "))
#generating random no between upper and lower bound
n = random.randint(lower,upper)
#creating chances
print("YOU have only", round(math.log(upper-lower+1,2)),"chances to guess the correct no!!!\n")
#initilazing the guesses
count = 0
while count < math.log(upper-lower+1,2) :
    count += 1
    # taking the guessing no
    guess = int(input("let's guess a no: "))
    #matching the guessing no 
    if n == guess:
        print("congratulations you did it in",count,"try")
        break
    elif n > guess:
        print("you guessed too small")
    elif n < guess:60
        print("you guessed too high")
#if can't guess in given try print the no
if count >= math.log(upper-lower+1,2):
    print("\n the no is: %d" %n)
    print("better try next time")
