from random import randint


def main():
    """
    main function. for random test!
    :return: void
    """

    print("Welcome to the number guessing game!")
    number = randint(1, 10)
    while True:
        # guess = raw_input ("Gess a number betweeen One and Ten:")
        guess = input("Guess a number between One and Ten:")

        if int(guess) == number:
            print("That's Right!")
            break
        elif int(guess) > number:
            print("Sorry, That's too high. Guess again!")
        elif int(guess) < number:
            print("Sorry, That's too low. Guess again!")


if __name__ == '__main__':
    main()
