# Linked List Targets

## Overview

Given a linked list and a list of target values, write functions to count and
remove all nodes with those values from the linked list.

## Specification

You will write functions to count and remove all instances of the specified
targets in a linked lists. Targets will be provided as a standard Python List.

The functions to count targets will return a dictionary with the target as the
key and the number of occurrences as the value. If the target is not found in
the linked list, it will not be included in the dictionary. If no targets are
found, the functions should return an empty dictionary.

The functions to remove targets will return a new list with all instances of the
target values removed and not modify the original linked list.

You will implement 4 functions, all of which have stubs in your starter file.

- `count_targets(link, targets)` - This is a helper function that will call one
  of the next two functions.
- `count_targets_iterative(link, targets)` - This function uses iteration to
  process the list and count the target occurrences.
- `count_targets_recursive(link, targets)` - This function uses recursion to
  process the list and count the target occurrences.
- `remove_targets(link, targets)` - This method uses recursion to process the
  list and remove all instances of the target values.

## Sample Execution

```python
>> link = Link('c', Link(2, Link(2, Link('a', Link('b', Link(4, Link('t', Link(2, Link('s', Link(4))))))))))
>> targets = [2, 4, 'b']
>> count_targets(link, targets)
{2: 3, 'b': 1, 4: 2}
>> link = remove_targets(link, targets)
>> print(link)
<c a t s>
>> counts = count_targets(link, targets)
{}
```

## Link Class

{% note "Note" %}

If you did the linked list lab, this is the same class we used there.

{% endnote %}

You are given the following `Link` class:

```python
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
```

This `Link` class represents a linked list object. Each instance of `Link` has
two instance attributes, `first` and `rest`.

A valid linked list can be one of the following:

1. An empty linked list (`Link.empty`)
2. A `Link` object containing the first value of the linked list and a reference
   to the rest of the linked list

## Rubric

| Grade Level   | Required standards                                                                                                                                                                                                               |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Core**      | - `count_targets` returns the correct target count dictionary<br/>                                                                                                                                                               |
| **Advanced**  | - `remove_targets` is implemented using recursion<br/> - `remove_targets` returns the correct linked list<br/> - `remove_targets` returns a new linked list instead of mutating the original<br/> - There is no unused code<br/> |
| **Excellent** | - Targets are counted iteratively in `count_targets_iterative` and recursively in `count_targets_recursive`<br/> - Code has no large sections of duplicate code<br/> - Code is easy to read                                      |

## Task 1

Given the `Link` class from lab, write a function `count_targets(link, targets)`
that takes a linked list and a list of target values, and returns a dictionary
where the keys are the target values and the values are the counts of how many
times each target appears in the linked list.

You can choose whether to write this function iteratively in
`count_targets_iterative`, or recursively in `count_targets_recursive`.
Whichever you choose, make sure to uncomment that implementation under the
`count_targets` function definition.

For example, if you chose iterative, `count_targets` should look like this:

```python
def count_targets(link, targets):
    return count_targets_iterative(link, targets)
    # return count_targets_recursive(link, targets)
```

## Task 2

Write a function `remove_target(link, target)` that takes a linked list and a
target value, and returns a new linked list with all nodes containing the target
value removed. Do not mutate the original linked list.

## Task 3

Look back at the code you wrote for Task 1. If you chose to write the function
iteratively, now add a recursive implementation of the same function under
`count_targets_recursive`. If you chose to write the function recursively, now
add an iterative implementation of the same function under
`count_targets_iterative`.
