#import random
#mynum = random.randint(1,100)

#print("I have a number in my mind. Can you Guess it?")

#number_of_guess_left=3
#while number_of_guess_left > 0:
    #usernum=int(input("Enter your Guess : "))
    #if usernum != mynum:
        #number_of_guess_left -= 1

    #if ( mynum == usernum ):
        #print("Yes you are Right")
        #break
    #elif (mynum > usernum):
        #print("too low")
    #else:
        #print("too high")
#if ( mynum == usernum ):
    #print("congratulation")
#else:
    #print("better luck next time")


        

import random
number = random.randint(0,100)
print("I have a number in my mind. Can you Guess it?")
number_of_guess_left = 3
while number_of_guess_left > 0:
    guess = int(input('Guess a number: '))
    if guess != number:
        number_of_guess_left -= 1

    if guess == number:
        print('"congratulation you win"','Your Score',10)
    elif guess < number:
        print('"have one more try"','your guess was too small')
    else:
        print('"have one more chance"','Your guess was too high')
        break
if guess == number:
    print('"congratulation you win"','Your Score',10)
else:
    print('"better luck next time"','Your Score',0)


  
