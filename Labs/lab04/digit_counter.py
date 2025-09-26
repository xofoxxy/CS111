def even_digit_counter(num):
    """Return the number of even digits"""
    counter = 0
    print("DEBUG: Value of num: " + str(num))

    while num > 0:
        current_digit = num % 10
        print("DEBUG: Value of current_digit: " + str(current_digit))
        print("DEBUG: value of num (middle of loop): " + str(num))
        if current_digit % 2 == 0:
            counter += 1
            print("DEBUG: Value of counter: " + str(counter))
            num = num // 10
            print("DEBUG: Value of num (after division): " + str(num))
            # input("DEBUG: Press enter to continue...") Uncomment this to go through each iteration of the loop.
        else:
            num = num // 10

    return counter

print(even_digit_counter(1234567890))

print(even_digit_counter(1011121314151617181920))