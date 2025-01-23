def negative_numbers():
    negative_count = 0  
    while True:
        number = int(input("Enter a number: "))
        if number == 0:
            break  
        if number < 0:
            negative_count += 1 
    print(negative_count)  

negative_numbers()
