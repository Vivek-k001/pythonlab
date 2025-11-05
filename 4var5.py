def add_numbers(*args):
    """This function adds variable number of integer arguments and returns the sum."""
    total = sum(args)
    return total

nums = list(map(int, input().split()))
result = add_numbers(*nums)
print(result)
print(add_numbers.__doc__)
