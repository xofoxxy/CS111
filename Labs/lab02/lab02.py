
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    new_s = []
    for element in s:
        if s.index(element) % 2 == 0:
            new_value = element * s.index(element)
            new_s.append(new_value)
    return new_s

def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
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
    """Print each line from input with the line number and a colon prepended,
    then write that line to the output file.
    >>> copy_file('text.txt', 'output.txt')
    1: They say you should never eat dirt.
    2: It's not nearly as good as an onion.
    3: It's not as good as the CS pun on my shirt.
    """
    """*** YOUR CODE HERE ***"""
    input_file = open(input_filename, "r")
    output_filename = open(output_filename, "w")
    i =0
    for line in input_file:
        i += 1
        line = line.strip()
        output_filename.write(f"{i}: {line}")
        print(f"{i}: {line}")



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
