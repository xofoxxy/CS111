from byu_pytest_utils import max_score, with_import, tier

core = tier('Core', 1)
advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)


@core
@max_score(0)
@with_import('library_card', 'LibraryCard')
def test_CORE_initialize(LibraryCard):
    card = LibraryCard("Bob")


@core
@max_score(0)
@with_import('library_card', 'LibraryCard')
def test_CORE_checkout(LibraryCard):
    card = LibraryCard("Sam")

    assert card.checkout_book("Harry Potter") == 'Harry Potter has been checked out.'
    assert card.checkout_book("Brave New World") == 'Brave New World has been checked out.'
    assert card.checkout_book("The Hobbit") == 'The Hobbit has been checked out.'

    # Try to check out a fourth book
    assert "limit reached" in card.checkout_book("Dune").lower()
    assert "limit reached" in card.checkout_book("Brave New World").lower()



@advanced
@max_score(0)
@with_import('library_card', 'LibraryCard')
def test_ADVANCED_has_book(LibraryCard):
    card = LibraryCard("Terry")
    card.checkout_book("Harry Potter")
    assert card.has_book("Harry Potter") is True
    assert card.has_book("Brave New World") is False
    card.checkout_book("Brave New World")
    assert card.has_book("Brave New World") is True


@advanced
@max_score(0)
@with_import('library_card', 'LibraryCard')
def test_ADVANCED_return_book(LibraryCard):
    card = LibraryCard("Jamie")
    card.checkout_book("Harry Potter")
    card.checkout_book("Brave New World")

    # Valid return
    assert card.return_book("Harry Potter") == 'Harry Potter has been returned.'

    # Returning a book not checked out
    assert card.return_book("The Hobbit") == "The Hobbit hasn't been checked out."

    assert card.has_book("Harry Potter") is False
    assert card.has_book("Brave New World") is True


@advanced
@max_score(0)
@with_import('library_card', 'LibraryCard')
def test_ADVANCED_limit_edge_case(LibraryCard):
    card = LibraryCard("Dana")
    books = ["Book A", "Book B", "Book C", "Book D"]
    for book in books:
        card.checkout_book(book)
    assert card.has_book("Book C") is True
    assert card.has_book("Book D") is False

    # Now return one and check that you can check out another
    card.return_book("Book B")
    assert card.checkout_book("Book D") == 'Book D has been checked out.'
    assert card.has_book("Book D") is True


@excellent
@max_score(0)
@with_import('library_card', 'LibraryCard')
def test_EXCELLENT_str(LibraryCard):
    card = LibraryCard("Sam")
    assert str(card) == "Sam has no books checked out."

    assert card.checkout_book("Harry Potter") == 'Harry Potter has been checked out.'
    assert card.checkout_book("Brave New World") == 'Brave New World has been checked out.'
    assert card.checkout_book("The Hobbit") == 'The Hobbit has been checked out.'

    # List should show 3 books
    assert "Sam has checked out" in str(card)
    assert "Harry Potter" in str(card)
    assert "Brave New World" in str(card)
    assert "The Hobbit" in str(card)


@excellent
@max_score(0)
@with_import('library_card', 'LibraryCard')
def test_EXCELLENT_equals(LibraryCard):
    card = LibraryCard("John")
    card2 = LibraryCard("Mary")
    card3 = LibraryCard("Cam")
    books = ["Mistborn", "Lord of The Rings", "Fahrenheit 451"]
    for book in books:
        card.checkout_book(book)
        card2.checkout_book(book)
    assert card == card2
    assert card != card3

    card3.checkout_book("Mistborn")
    assert card3 != card

    card3.checkout_book("Fahrenheit 451")
    assert card3 != card

    card3.checkout_book("Lord of The Rings")
    assert card3 == card
