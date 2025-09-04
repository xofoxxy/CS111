def average_temperature(temps):
    """
    Given a list of temperatures, TEMPS, compute the average
    temperature and return it to the user
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> average_temperature(temp_data)
    75.15
    """
    ### Your code goes here
    temp_total = 0
    for temp in temps:
        temp_total += temp
    return temp_total / len(temps)


def hot_days(temps):
    """
    Given a list of temperatures, TEMPS, count the number of days
    more than five degrees above the average.  Print the number of
    days and the average and return the number of days.
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> hot_days(temp_data)
    There were 2 day(s) more than 5 degrees above the average of 75.2.
    2
    """
    ### Your code goes here
    average = average_temperature(temps)
    hot_days = 0
    for temp in temps:
        if temp > average + 5:
            hot_days += 1
    print(f"There were {hot_days} day(s) more than 5 degrees above the average of {average:.1f}.")
    return hot_days

def is_palindrome(word):
    """
    Given a single word, WORD, determine if it is a palindrome or not.
    Print a message that includes the word stating it is or is not a
    palindrome and return True if it is and False otherwise
    >>> is_palindrome('rotator')
    rotator is a palindrome.
    True
    >>> is_palindrome('apple')
    apple is not a palindrome.
    False
    """
    for letters in range(len(word)):
        if word[letters] != word[-letters - 1]:
            print(f"{word} is not a palindrome.")
            return False
    print(f"{word} is a palindrome.")
    return True

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """

    # I used a list comprehension last time, so I just ripped it from that.
    new_s = []
    for element in s:
        if s.index(element) % 2 == 0:
            old_index = s.index(element)
            new_value = element * s.index(element)
            s[old_index] = 0  # This should effectively remove the element but maintain the index
            new_s.append(new_value)
    return new_s