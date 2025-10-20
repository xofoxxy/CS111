# LibraryCard Class

## Overview

Your goal is to write a Python class that acts like a library card. The class
will have to track the name of the user, as well as the current books they have
checked out. The class should have methods that manage that data as described
below.

## Required Specifications

The class should:

1. Be initialized with only the user's name
2. For each user, be able to track what books have been checked out based on
   their titles
3. Include a method `checkout_book(title)` that:
    1. Does not allow more than 3 books to be checked out at once. If the user
       has already checked out 3 books, it should return `"Limit Reached."`
       Otherwise, it should add the title to the books this user has checked
       out and return `"<title> has been checked out."` (`<title>` being the
       title passed in)
4. Include a method `has_book(title)` that:
    1. Returns `True` if the user has this book currently checked out, otherwise
       `False`.
5. Include a method `return_book(title)` that:
    1. Removes the book from being checked out. If the book isn't checked out,
       return `"<title> hasn't been checked out."` Otherwise, return
       `"<title> has been returned."`
6. Include a `__str__(self)` dunder method that:
    1. Returns the string `"<Name> has checked out: <Books>"`. (With `<Books>`
       being all the titles of the checked-out books, in any format that's easy
       to read. And `<Name>` being the user's name.) If they have no books
       checked out, return `"<Name> has no books checked out."`
7. include a `__eq__(self, other)` dunder method that:
    1. Returns `True` if two LibraryCard objects have checked out the exact same
       set of books in any order, `False` otherwise. This means that if they
       checked out books in a different order, but still have the same books
       checked out, it should return `True`. (`other` is the other LibraryCard
       object being compared against `self`.)

***Note**: For the tests to pass, your output must match exactly what is
described in the specification above anywhere specific output strings are
given.*

## Sample Execution

```Python
>>> card = LibraryCard("Dan")
>>> card.checkout_book("Harry Potter")
"Harry Potter has been checked out."
>>> card.checkout_book("Mistborn")
"Mistborn has been checked out."
>>> card.checkout_book("Brave New World")
"Brave New World has been checked out."
>>> card.checkout_book("The Hobbit")
"Limit reached. Return a book before checking out another."
>>> card.has_book("Mistborn")
True
>>> card.has_book("The Hobbit")
False
>>> card.return_book("Mistborn")
"Mistborn has been returned."
>>> card.return_book("Mistborn")
"Mistborn hasn't been checked out."
>>> print(card)
Dan has checked out: Harry Potter, Brave New World
>>> card2 = LibraryCard("Mike")
>>> card2.checkout_book("Brave New World")
"Brave New World has been checked out."
>>> card2.checkout_book("Harry Potter")
"Harry Potter has been checked out."
>>> card2 == card
True
```

## Testing Your Code

You can test your code and run all the pytests by running one of these two
commands in your terminal:

```sh
python3 -m pytest -vv .
```

or

```sh
python -m pytest -vv .
```

## Rubric {#rubric}

| Grade Level   | Required standards                                                                                                                                                                                                                                                                    |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Core**      | - Creates a class that can be correctly initialized<br/> - `checkout_book` method correctly tracks which books have been checked out<br/> - `checkout_book` method returns the correct string based on the input<br/> - Class and variable names are clear and use a consistent style |
| **Advanced**  | -`has_book` correctly returns True or False<br/> - `return_book` can remove a book from being checked out<br/> - `return_book` method returns the correct string based on the input<br/> - There is no unused or duplicated code.                                                     |
| **Excellent** | - `__str__` returns a string that contains the required information<br/> `__eq__` properly returns True or False if two cards have checked out the same books in any order                                                                                                            |

When submitting your code to the autograder, each test is keyed to one of the
grade levels above. If you pass all the "CORE" tests, you receive the Core grade
(assuming you also meet the Core style requirements). Passing all the "CORE" and
"ADVANCED" tests gives you the Advanced grade, and passing all tests gives you
Excellent grade.

## Turn In Your Work

Submit your `library_card.py` file.

The function's names need to be exactly the same as in the specifications for
the autograder to work.
