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


def count_targets(link, targets):
    # return count_targets_iterative(link, targets)
    # return count_targets_recursive(link, targets)
    dictionary = {}
    dictionary = count_targets_recursive(link, targets)
    return dictionary


def count_targets_iterative(link, targets):
    dictionary = {}
    while link.rest is not Link.empty:
        if link.first in targets and link.first in dictionary.keys():
            dictionary[link.first] += 1
        elif link.first in targets:
            dictionary[link.first] = 1
        link = link.rest
    if link.first in targets and link.first in dictionary.keys():
        dictionary[link.first] += 1
    elif link.first in targets:
        dictionary[link.first] = 1
    return dictionary


def count_targets_recursive(link, targets):

    def recursive_search(link, targets, dictionary):
        if link.rest == Link.empty:
            if link.first in targets and link.first in dictionary.keys():
                dictionary[link.first] += 1
            elif link.first in targets:
                dictionary[link.first] = 1
            return dictionary
        else:
            if link.first in targets and link.first in dictionary.keys():
                dictionary[link.first] += 1
            elif link.first in targets:
                dictionary[link.first] = 1
            return recursive_search(link.rest, targets, dictionary)
    dictionary = {}
    return recursive_search(link, targets, dictionary)


def remove_targets(link, targets):
    print(link)
    def clone_link(link):
        if link == Link.empty:
            return Link.empty
        return Link(link.first, clone_link(link.rest))

    def remove_targets_helper(link, targets):
        if link.rest == Link.empty:
            if link.first in targets:
                return Link.empty
            else:
                return link
        if link.first in targets:
            link.first = link.rest.first
            link.rest = link.rest.rest
            return remove_targets_helper(link, targets)
        else:
            return Link(link.first, remove_targets_helper(link.rest, targets))

    new_link = clone_link(link)
    return remove_targets_helper(new_link, targets)

if __name__ == "__main__":
    link = Link(0, Link(1, Link(4, Link(1, Link(4, Link(2, Link(3, Link(4, Link(5, Link(8, Link(12, Link(13))))))))))))
    targets = [4, 12, 0]
    key = {4: 3, 12: 1, 0: 1}
    output = count_targets(link, targets)
    print(output)
    print(key)
    print(link)
    print(remove_targets(link, targets))