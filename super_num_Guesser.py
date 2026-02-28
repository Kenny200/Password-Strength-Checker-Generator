import random


chance_total = 10
guess_count = 0

# Generate two random numbers between 1 and 999
rangeNum1 = random.randint(1, 999)
rangeNum2 = random.randint(1, 999)


print(f'rangeNum1 = {rangeNum1}')
print(f'rangeNum2 = {rangeNum2}')

lower_bound = min(rangeNum1, rangeNum2)
upper_bound = max(rangeNum1, rangeNum2)

print(f'rangeNum1 = {lower_bound}')
print(f'rangeNum2 = {upper_bound}')

num = random.randint(lower_bound, upper_bound) 


chance_total = 10
guess_count = 0

# Welcome message
print("Welcome to the Super-Random Number Guesser Game!")
print(f"You have 10 chances to guess the number between {lower_bound} and {upper_bound}.")

print(num)

# Start the guessing loop
while guess_count < chance_total:
    guess_count += 1
    userGuess = int(input('Enter guess:'))

    if userGuess == num:
        print(f'Congratulations! You guessed the number in {guess_count} tries!')
        break
    elif guess_count >= chance_total and userGuess != num:
        print(f'Sorry! The number was {num}. Better luck next time.')
    elif userGuess < num:
        print('Too low! Try again.')
        print(f'You have {chance_total - guess_count} chances left.')
    elif userGuess > num:
        print('Too high! Try again.')  
        print(f'You have {chance_total - guess_count} chances left.')  