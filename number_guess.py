import random as r 
n = r.randrange(1,100)
# to take a user input to enter a number
guess = int(input("Enter any number: "))

while n!= guess: 
    if guess < n:
        print("Too low")
        
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        
        guess = int(input("Enter number again: "))
    
    else:
        break
print("you guessed it right!!")