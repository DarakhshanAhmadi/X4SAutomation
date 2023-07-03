from random import randrange

randomValue = None


def GenerateRandomNum():
    random_value = randrange(0, 100001, 4)
    random_value = str(random_value)
    return random_value
