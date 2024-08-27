import random


def generateRefNo():
    number = random.randrange(1, 999)
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = 8
    all = upper + str(number)
    randomString = "".join(random.sample(all, length))

    return randomString
