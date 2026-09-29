import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit("Next time type a number larger than 0 fr")

else:
    print("Please type a number next time")
    quit("You didnt type a number bro!")


random_number = (random.randint(0,top_of_range))
print(random_number)
guesses = 0

while True: 
    guesses += 1
    user_guess=input("Guess the number ")
    if user_guess.isdigit():
        user_guess = int(user_guess)


    else:
        print('Please type a number next time.')
        continue 


    if user_guess == random_number:
        print("you got it bro :)")
        break
    elif user_guess > random_number:
            print('You were above the number!')
            
    else:
            print('You were below the number!')

print('You got in',guesses, 'guesses')


