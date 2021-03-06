import random


def guess_code():
    answer = generate_unique_code()
    allowedGuesses = 10
    # print(answer)
    for i in range(0, allowedGuesses):
        guess = input("Enter your guess: ")
        if guess == answer:
            print("right")
            break
        else:
            correctCorrect = 0
            correctIncorrect = 0

            if guess[0] == answer[0]:
                correctCorrect += 1
            if guess[1] == answer[1]:
                correctCorrect += 1
            if guess[2] == answer[2]:
                correctCorrect += 1
            if guess[3] == answer[3]:
                correctCorrect += 1

            if guess[0] == answer[1] or guess[0] == answer[2] or guess[0] == answer[3]:
                correctIncorrect += 1
            if guess[1] == answer[0] or guess[1] == answer[2] or guess[1] == answer[3]:
                correctIncorrect += 1
            if guess[2] == answer[0] or guess[2] == answer[1] or guess[2] == answer[3]:
                correctIncorrect += 1
            if guess[3] == answer[0] or guess[3] == answer[1] or guess[3] == answer[2]:
                correctIncorrect += 1

            print("wrong code. you have {0} guesses left.".format(allowedGuesses - i - 1))
            print(guess + " had {0} correct digits in correct positions "
                          "and {1} correct digits in incorrect positions.".format(correctCorrect, correctIncorrect))

    print("it exploded and you died.")


def generate_unique_code():
    # im using integers in variable names and one can stop me.
    code1 = random.randrange(9)
    code2 = random.randrange(9)
    code3 = random.randrange(9)
    code4 = random.randrange(9)

    # for sure not the right way to do this, but hackathon
    while code1 == code2 or code1 == code3 or code1 == code4:
        code1 = random.randrange(9)

    while code2 == code1 or code2 == code3 or code2 == code4:
        code2 = random.randrange(9)

    while code3 == code1 or code3 == code2 or code3 == code4:
        code3 = random.randrange(9)

    return str(code1) + str(code2) + str(code3) + str(code4)


def generate_duplicate_code():
    # im using integers in variable names and one can stop me.
    code1 = random.randrange(9)
    code2 = random.randrange(9)
    code3 = random.randrange(9)
    code4 = random.randrange(9)

    return str(code1) + str(code2) + str(code3) + str(code4)


if __name__ == '__main__':
    guess_code()

