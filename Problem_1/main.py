# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def Problem(list: list, k: int):
    resultado = [(second_value, value) for second_value in list for value in list
            if second_value != value and second_value + value == k]

    if resultado:
        return True

    return False
