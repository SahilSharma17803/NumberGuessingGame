import random
num=random.randint(1,10)
for i in range (3):
    guess=int(input("Enter number between 1&10 : "))
    if (guess>num):
        print("You guessed higher number try lower one")
    elif(guess<num):
        print("try higher value")    
    else :
        print("You won")
        break