def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    # Iterative method
    list = []
    while link is not Link.empty:
        list.append(link.first)
        link = link.rest

    # Recursive method
    def recursive_convert(link):
        if link is Link.empty:
            return []
        else:
            return [link.first] + recursive_convert(link.rest)
    return list


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    s = Link.empty
    while n > 0:
        digit = n % 10
        n = n // 10
        s = Link(digit, s)

    return s

def every_other(link):
    """Mutates a linked list so that all the odd-indexed elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    while link and link.rest:
        link.rest = link.rest.rest
        link = link.rest

def deep_map_mut(fn, link):
    """
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> link1
    Link(9, Link(Link(16), Link(25, Link(36))))
    """
    if link is Link.empty:
        return
        
    # Handle current value
    if isinstance(link.first, Link):
        deep_map_mut(fn, link.first)
    else:
        link.first = fn(link.first)
    
    # Process rest of the list
    deep_map_mut(fn, link.rest)


class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(
            rest, Link), "Link does not follow proper structure"
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'