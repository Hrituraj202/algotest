import random

def apply_random_percentage(number):
    percentage_range = 10

    if 0 == random.choice([0, 0, 0, 0, 0, 0, 1]):
        return number

    operation = random.choice(["add", "subtract"])
    percentage = random.uniform(0, percentage_range)
    change_amount = (number * percentage) / 100

    if operation == "add":
        result = number + change_amount
    else:
        result = number - change_amount

    return result
