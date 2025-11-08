def generate_random_number():
    import random
    return random.randint(1, 100)

def check_guess(guess, secret_number):
    if guess < secret_number:
        return "Too low! Try again."
    elif guess > secret_number:
        return "Too high! Try again."
    else:
        return "Congratulations! You've guessed the number!"
