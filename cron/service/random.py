import random

def apply_random_percentage(number):
    percentage_range = 10
    if not (0 <= percentage_range <= 100):
        raise ValueError("Percentage range must be between 0 and 100.")

    operation = random.choice(["add", "subtract"])
    percentage = random.uniform(0, percentage_range)
    change_amount = (number * percentage) / 100

    if operation == "add":
        result = number + change_amount
    else:
        result = number - change_amount

    return operation, result
