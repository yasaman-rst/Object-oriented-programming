def smallest_average(person1, person2, person3):
    return min([person1, person2, person3], key=lambda p: (p["result1"] + p["result2"] + p["result3"]) / 3)

# Example data
person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))
