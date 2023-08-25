
def get_greeting(name):
    return f"Hello {name}!"


message = get_greeting("farooq")
print(message)


def increment(number, number2, by=1):
    return number + number2 + by


print(increment(2, 3))
