from library import Library


def main():
    """Make the app interactive"""
    # Load the books from the file
    library = Library("data/books.txt")

    try:
        while True:
            print("\n-------Library Management System------")
            print()
            print("1. View Books")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Add Book")
            print("5. Exit")

            try:
                choice = int(input("Enter your choice from (1-5): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
                continue

            if choice == 1:
                library.view_books()
            elif choice == 2:
                title = input(
                    "Enter the title of the book you want to borrow: ").strip()
                user = str(input("Enter your name: ").strip())
                library.borrow_book(title, user)
            elif choice == 3:
                title = input(
                    "Enter the title of the book you want to return: ").strip()
                user = str(input("Enter your name: ").strip())
                library.return_book(title, user)
            elif choice == 4:
                title = input("Enter the title of the book: ").strip()
                author = input("Enter the author's name: ").strip()
                year = input("Enter the publication year: ").strip()
                library.add_book(title, author, year)
            elif choice == 5:
                print("Thank you for using the library Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Returning to the main menu.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
