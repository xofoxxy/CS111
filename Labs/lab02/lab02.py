
def even_weighted(s):
    new_s = []
    for element in s:
        if s.index(element) % 2 == 0:
            old_index = s.index(element)
            new_value = element * s.index(element)
            s[old_index] = 0 #This should effectively remove the element but maintain the index
            new_s.append(new_value)
    return new_s


def couple(s, t):
    assert len(s) == len(t)
    # This is the better way
    zipped_list = zip(s, t)

    # Now the way that they want it
    zipped_list = []
    for element in s:
        other_element = t[s.index(element)]
        zipped_list.append([element, other_element])

    return list(zipped_list)



def copy_file(input_filename, output_filename):
    input_file = open(input_filename, "r")
    output_filename = open(output_filename, "w")
    i =0
    for line in input_file:
        i += 1
        line = line.strip()
        if i == 1:
            output_filename.write(f"{i}: {line}")
        else:
            output_filename.write(f"\n{i}: {line}")


# E           "1: They say you should never eat dirt.\n2: It's not nearly as good as an onion.\n3: It's not as good as the CS pun on my shirt.\n" ==
#             "1: They say you should never eat dirt.\n2: It's not nearly as good as an onion.\n3: It's not as good as the CS pun on my shirt."
#


########################################################
# OPTIONAL QUESTIONS


def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    all_factors = []
    """*** YOUR CODE HERE ***"""
