import random


def guess_code():
    val = input("Enter your value: ")
    print(generate_unique_code())


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

