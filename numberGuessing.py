import random

print("LETS PLAY A GUESSING GAME")

nummm = random.randint(1,9)

chances = 0

print("GUESS ANY NUMBER BETWEEN 1 To 9")


while chances<5:
    guess = int(input("ENTER YOUR GUESS"))

    if guess == nummm:
        print("Correct")
        print("You Win! Congratulations!")
        print("🤝")
        break
    
    elif guess < nummm:
        print("Your Guess is too Low")
        print("Guess a Number higher than this")

    else:
        print("Your Guess is too high")
        print("Guess a Number lesser than this")
    
    chances+=1

if chances==5 and guess!= nummm:
    print("YOU LOSE")
    print("👎")
