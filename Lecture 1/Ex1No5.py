def negative_numbers():
    negative_count = 0 
    even = 0 
    while True:
        number = int(input("Enter a number: "))
        if number == 0:
            break  
        if number < 0:
            negative_count += 1
        if number % 2 == 0:  
         even += 1       
    print("the number of negative integers:",negative_count)
    print("the number of even integers:",even)

negative_numbers()