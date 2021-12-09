# Learning Function in python
# Fuzzbuzz function
def fuzzbuzzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fuzzbuzz"
    if number % 3 == 0:
        return "fuzz"
    if number % 5 == 0:
        return "buzz"
    return number


print(fuzzbuzzz(15))
