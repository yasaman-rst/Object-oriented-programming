class ListHelper:
    def greatest_frequency(my_list:list):
        return max(set(my_list), key=my_list.count)

    def doubles(my_list:list):
        return len([item for item in set(my_list) if my_list.count(item) > 1])

numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))  
print(ListHelper.doubles(numbers))  