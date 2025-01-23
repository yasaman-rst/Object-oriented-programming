def arithmetic_progression(max_value):
    starting_no = 3  
    count = 0  
    sum = 0  
    sum_squares = 0  

    while starting_no <= max_value:
        count += 1
        sum += starting_no 
        sum_squares += starting_no * starting_no
        starting_no += 3  

    print("Number of terms:", count)
    print("Sum of the terms:", sum)
    print("Sum of squared terms:", sum_squares)
    
max_value = int(input("Enter the maximum value: "))
arithmetic_progression(max_value)
