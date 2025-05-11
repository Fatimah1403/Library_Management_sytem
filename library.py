import os
from datetime import datetime


class Library:
    """Library class that performs all the
    methods for the library management.
    """

    def __init__(self, file_path):
        """Initialize the library object"""
        self.file_path = file_path
        self._books = {}  # Private attrrbute to store books
        self._borrowers = {}  # Private attrrbute to track borrowed books
        self._load_books()

    def __repr__(self):
        """Return a string representation of
        the library"""
        return f"<Library: {len(self._books)} books available>"

    def __len__(self):
        """Returns the total number of books in the library"""
        return len(self._books)

    def _load_books(self):
        """Load books from a file into the library"""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, mode="r", encoding="utf-8") as file:
                    for line in file:
                        try:
                            title, author, year = line.strip().split(", ")
                            self._books[title] = {
                                "author": author,
                                "year": int(year),
                                "available": True,  # Assuming all books are initially available
                            }
                        except ValueError:
                            print(f"Skipping malformed line: {line.strip()}")
            else:
                print(
                    f"Books file '{self.file_path}' not found. "
                    "Starting with an empty library."
                )

        except FileNotFoundError:
            print(f"Books file '{self.file_path}' is missing or inaccessible.")
        except OSError as e:
            print(f"An error occurred while accessing the file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _log_borrowing(self, action, title, user):
        """Log borrowing and returning actions to a file."""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("data/borrow_logs.txt", mode="a", encoding="utf-8") as log_file:
                log_file.write(f"{timestamp} - {action}: {title} by {user}\n")
        except Exception as e:
            print(
                f"An error occurred while logging borrowing and returning actions: {e}"
            )

    def view_books(self):
        """Display all available books in the library"""
        try:
            if not self._books:
                print("No books available")
                return
            print("\nAvailable Books: ")

            for title, details in self._books.items():
                status = "available" if details["available"] else "Not Available"
                print(
                    f" - {title} by {details["author"]} ({details["year"]} - {status})"
                )
        except Exception as e:
            print(f"An error occurred while viewing books: {e}")

    def borrow_book(self, title, user):
        """Allow a user to borrow a book from the Library."""
        try:
            # Convert the input title to lowercase for case-insensitive
            # comparison
            title_lower = title.lower()

            # Find the actual book title in the library by comparing in
            # lowercase
            matching_title = next(
                (book for book in self._books if book.lower() == title_lower), None
            )

            if matching_title and self._books[matching_title]["available"]:
                # Borrow the book
                self._books[matching_title]["available"] = False
                self._borrowers[matching_title] = user
                self._log_borrowing("Book borrowed", matching_title, user)
                print(f"You have successfully borrowed '{matching_title}'.")
            elif matching_title:
                print(f"Sorry, '{matching_title}' is currently not available.")
            else:
                print(f"'{title}' is not in the library.")
        except Exception as e:
            print(f"An error occurred while borrowing a book: {e}")

    def return_book(self, title, user):
        """Allow user to return books borrowed"""
        try:
            if title in self._borrowers and self._borrowers[title] == user:
                self._books[title]["available"] = True
                del self._borrowers[title]
                self._log_borrowing("Book returned", title, user)
                print(f"You have successfully returned '{title}'")
            else:
                print(f"You have not borrowed '{title}' or you are not the borrower.")
        except Exception as e:
            print(f"An error occurred while returning a book: {e}")

    def add_book(self, title, author, year):
        """Add a new book to the library."""
        try:
            if title in self._books:
                print(
                    f"Book '{title}' by {author} ({year}) already exists in the library."
                )
            else:
                self._books[title] = {
                    "author": author,
                    "year": int(year),
                    "available": True,
                }
                # Write the new book entry to the file
                with open(self.file_path, "a", encoding="utf-8") as file:
                    if (
                        os.path.getsize(self.file_path) > 0
                    ):  # Check if file is not empty
                        file.write(f"\n{title}, {author}, {year}")
                    else:
                        file.write(f"{title}, {author}, {year}")
                print(f"'{title}' by {author} ({year}) added successfully.")
        except Exception as e:
            print(f"An error occurred while adding a book: {e}")
