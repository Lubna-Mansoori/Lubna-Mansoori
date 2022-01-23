class Library:
    total_books = ["Harry Potter", "Hunger Games", "Cindrella",
                   "Alice in wonderland"]
    records = {"Harry Potter": "", "Hunger Games": "", "Cindrella": "",
               "Alice in wonderland": ""}

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lended_books = []

    def display_books(self):
        print(f"We have the following books :")
        for items in self.list_of_books:
            print(items)

    def lend_books(self):
        user_name = input("Enter your name: ")
        book_to_lend = input("Enter the book you want to lend: ")
        if book_to_lend in self.list_of_books:
            for b in Library.records:
                if b == book_to_lend:
                    Library.records[book_to_lend] = user_name
            self.lended_books.append(book_to_lend)
            self.list_of_books.remove(book_to_lend)
            print(f"You have lended {book_to_lend} Book !")
        elif book_to_lend not in self.list_of_books:
            print(f"Sorry the book is not available as it is already taken "
                  f"by {Library.records[book_to_lend]}")
            for k in Library.records:
                if k == book_to_lend:
                    pass
        else:
            print("No such book, please check the name you entered.")
            Library.display_books(self)

    def add_book(self):
        book_to_add = input("Enter name of book you want to Add: ")
        self.list_of_books.append(book_to_add)
        Library.records.update({book_to_add: ""})
        print("Thank you book has been added...")

    def return_book(self):
        book_to_return = input("Enter the book you want to return: ")
        self.lended_books.remove(book_to_return)
        self.list_of_books.append(book_to_return)
        print("Thank you book has been returned...")


if __name__ == '__main__':
    Lub = Library(Library.total_books, "Best Library")
    while True:
        print("Welcome to Best Library")
        option = int(input("Select the option you want to perform : \n"
                           "1. Display Books\n"
                           "2. Lend Book\n"
                           "3. Add Book\n"
                           "4. Return Book\n"
                           "5. Exit\n"))
        if option == 1:
            Library.display_books(Lub)
        elif option == 2:
            Library.lend_books(Lub)
        elif option == 3:
            Library.add_book(Lub)
        elif option == 4:
            Library.return_book(Lub)
        elif option == 5:
            break
        else:
            print("Incorrect input ! Please try again")
