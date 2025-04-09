from functools import reduce

numbers = [1, 2, 3, 4]

# using lambda
print("Lambda map:   ", list(map(lambda x: x**2, numbers)))
print("Lambda filter:", list(filter(lambda x: x % 2 == 0, numbers)))
print("Lambda reduce:", reduce(lambda x, y: x + y, numbers))
#for
def map_loop(nums):
    result = []
    for x in nums:
        result.append(x**2)
    return result

def filter_loop(nums):
    result = []
    for x in nums:
        if x % 2 == 0:
            result.append(x)
    return result

def reduce_loop(nums):
    total = 0
    for x in nums:
        total += x
    return total

print("Loop map:     ", map_loop(numbers))
print("Loop filter:  ", filter_loop(numbers))
print("Loop reduce:  ", reduce_loop(numbers))
