import json
import os

data_file = "books.json"

def load_books():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

def save_books(books):
    with open(data_file, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    books = load_books()
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    books.append(book)
    save_books(books)
    print("✅ Book added successfully!")

def remove_book():
    books = load_books()
    title = input("Enter book title to remove: ")
    new_books = [book for book in books if book["title"].lower() != title.lower()]
    
    if len(new_books) < len(books):
        save_books(new_books)
        print("🗑 Book removed successfully!")
    else:
        print("❌ Book not found!")

def search_book():
    books = load_books()
    search_by = input("Search by (title/author): ").lower()
    query = input("Enter search query: ")
    found_books = [book for book in books if book[search_by].lower() == query.lower()]
    
    if found_books:
        for book in found_books:
            print(f"📖 {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Not Read'}")
    else:
        print("❌ No books found!")

def all_books():
    books = load_books()
    if books:
        for book in books:
            print(f"📖 {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Not Read'}")
    else:
        print("📚 No books in the library yet!")

def library_stats():
    books = load_books()
    total_books = len(books)
    read_books = sum(1 for book in books if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    print(f"📚 Total books: {total_books}")
    print(f"✅ Books Read: {read_books}")
    print(f"📊 Percentage Read: {percentage_read:.2f}%")

while True:
    print("\n📚 Library Manager CLI")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Show All Books")
    print("5. Library Statistics")
    print("6. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        all_books()
    elif choice == "5":
        library_stats()
    elif choice == "6":
        print("Goodbye! 👋")
        break
    else:
        print("❌ Invalid choice! Try again.")
