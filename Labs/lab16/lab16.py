# Note: The Tree implemenation is at the bottom of the file
# Please read the docstrings to learn how to interact with a Tree object.

def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and
    False otherwise.

    >>> scrat = Tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = Tree('roots', [Tree('branch1', [Tree('leaf'), Tree('berry')]), Tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = Tree(1, [Tree('berry',[Tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    if t.label == 'berry':
        return True
    for branches in t.branches:
        if berry_finder(branches):
            return True
    return False


def height(t):
    """Return the height of a Tree."""
    state = [t]
    deepest = 0
    deepest_state = []

    # Take a step
    # if you can, take another step
    # if you can't see if it works
    # if it doesn't go back and try other options
    # if none of them work return false
    def take_step(t):
        for branch in t.branches:
            if branch.is_leaf():
                nonlocal deepest
                nonlocal deepest_state
                if deepest < len(state):
                    deepest = len(state)
                    deepest_state = state.copy()
            else:
                state.append(branch)
                take_step(branch)
                state.pop()
    take_step(t)
    print(deepest_state)
    return deepest


def max_path_sum(t):
    """Return the maximum path sum of the Tree.

    >>> t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    >>> max_path_sum(t)
    11
    """
    state = [t]
    highest_value = 0
    deepest_state = []

    # Take a step
    # if you can, take another step
    # if you can't see if it works
    # if it doesn't go back and try other options
    # if none of them work return false
    def take_step(t):
        for branch in t.branches:
            if branch.is_leaf():
                nonlocal highest_value
                nonlocal deepest_state
                values = [x.label for x in state] + [branch.label]
                print(values)
                sum_of_path = sum(values)
                if sum_of_path > highest_value:
                    highest_value = sum_of_path
                    deepest_state = state.copy()
            else:
                state.append(branch)
                take_step(state[-1])
                state.pop()

    take_step(t)
    return highest_value


def find_path(t, x):
    if t.label == x:
        return [t.label]
    
    for branch in t.branches:
        path = find_path(branch, x)
        if path:  # If path is found in this branch
            return [t.label] + path
            
    return None  # If no path is found

# Optional Question
def has_path(t, word):
    """Return whether there is a path in a Tree where the entries along the path
    spell out a particular word.

    >>> greetings = Tree('h', [Tree('i'),
    ...                        Tree('e', [Tree('l', [Tree('l', [Tree('o')])]),
    ...                                   Tree('y')])])
    >>> print(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    state = [t]
    def recursive_word_search(t, word):
        for branch in t.branches:
            current_list = [x.label for x in state]
            print(current_list)
            current_word = ''.join(
                [x.label for x in state] + [branch.label]
            )
            if current_word == word:
                return [x.label for x in state] + [branch.label]
            else:
                state.append(branch)
                recursive_word_search(branch, word)
                state.pop()
        return None
    return recursive_word_search(t, word)

class Tree:

    def __init__(self, label, branches=[]):
        """
        A Tree is constructed by passing a label and an optional *list* of branches.
        The list passed must only contain objects of the Tree class.
        """
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        """
        Returns a boolean, true if this Tree object is a leaf (has no branches), false otherwise.
        """
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return f'Tree({self.label}{branch_str})'

    def __str__(self):

        def indented(self):
            lines = []
            for b in self.branches:
                for line in indented(b):
                    lines.append('  ' + line)
            return [str(self.label)] + lines

        return '\n'.join(indented(self))


if __name__ == '__main__':
    greetings = Tree('h', [Tree('i'), Tree('e', [Tree('l', [Tree('l', [Tree('o')])]), Tree('y')])])
    print(greetings)
    print(find_path(greetings, 'l'))