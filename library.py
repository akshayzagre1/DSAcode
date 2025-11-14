from statistics import mode, StatisticsError

def compute_average_borrow(members):               # Compute the average number of books borrowed by all library members.
    if not members:
        return 0
    return sum(members) / len(members)

def find_book_extremes(books):                    # Find the book with the highest and lowest number of borrowings in the library.
    if not books:
        return None, None
    max_book = max(books, key=books.get)
    min_book = min(books, key=books.get)
    return max_book, min_book

def count_zero_borrowers(members):                       #  Count the number of members who have not borrowed any books (denoted by a
    return sum(1 for m in members if m == 0)

def most_frequent_borrowed(books):                      # Display the most frequently borrowed book (i.e., the mode of borrow counts).
    try:
        borrow_counts = list(books.values())
        freq_value = mode(borrow_counts)
        most_borrowed_books = [book for book, count in books.items() if count == freq_value]
        return most_borrowed_books
    except StatisticsError:
        return []

def display_statistics(members_dict, books):
    members = list(members_dict.values())
    avg = compute_average_borrow(members)
    max_book, min_book = find_book_extremes(books)
    zero_borrowers = count_zero_borrowers(members)
    most_freq_books = most_frequent_borrowed(books)

    print(f"Average books borrowed per member: {avg:.2f}")
    print(f"Most borrowed book: {max_book}")
    print(f"Least borrowed book: {min_book}")
    print(f"Members with 0 books borrowed: {zero_borrowers}")
    print(f"Most frequently borrowed count books: {most_freq_books}")

# Sample data
members = {
    "vinay": 3,
    "saif": 0,
    "shubham": 5,
    "alok": 2,
    "ansh": 4,
    "abhishek": 2
}

books = {
    "harry potter": 12,
    "the alchemist": 9,
    "inferno": 8,
    "the great gandhi": 14,
    "moby dick": 6
}

display_statistics(members, books)
