class LibraryCard:
    def __init__(self, name):
        self.name = name
        self.books = []

    def checkout_book(self, title):
        if len(self.books) < 3:
            print(f"Checking out {title} to {self.name}")
            self.books.append(title)
            return f"{title} has been checked out."
        else:
            return "limit reached"

    def has_book(self, title):
        if title in self.books:
            return True
        else:
            return False

    def return_book(self, title):
        if title in self.books:
            self.books.remove(title)
            return f"{title} has been returned."
        else:
            return f"{title} hasn't been checked out."

    def __str__(self):
        if len(self.books) > 0:
            return f"{self.name} has checked out {self.books}"
        else:
            return f"{self.name} has no books checked out."

    def __eq__(self, other):
        other_list = other.books.copy()
        self_books = self.books.copy()
        if other is None:
            return False
        if not isinstance(other, LibraryCard):
            return False
        for book in self_books:
            if book in other.books:
                other_list.remove(book)
                self_books.remove(book)
            else:
                return False
        if other_list != self_books: # Both of them should be empty at this point.
            return False
        return True
