import streamlit as st  # type: ignore
import json
import time

# Load library from file
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save library to file
def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# Initialize library
library = load_library()

st.title("📚 Awesome Library Manager 📖")
st.write("Manage your personal book collection easily! 📓")

st.sidebar.image("images/book1.png", width=200)
st.sidebar.header("📕 Create your Library!")  # Sidebar header
menu = st.sidebar.radio("📌 Select an Option", 
                        ["Add a Book 🆕", "Remove a Book ❌", "Search a Book 🔍", 
                         "Display All Books 📚", "View Library 📊", "Save & Exit 💾"])

def animated_success(message):
    with st.spinner("Processing..."):
        time.sleep(1)
    st.toast(message, icon="✅")
    st.snow()
    time.sleep(1)  # Ensure animation is visible before rerun

def animated_warning(message):
    with st.spinner("Processing..."):
        time.sleep(1)
    st.toast(message, icon="⚠️")
    st.snow()
    time.sleep(1)  # Ensure animation is visible before rerun

if menu == "Add a Book 🆕":
    st.header("📗 Add a New Book")
    title = st.text_input("📑 Enter Book Title")
    author = st.text_input("✍️ Enter Author Name")
    year = st.number_input("📅 Enter Publication Year", min_value=1000, max_value=2100, step=1)
    genre = st.text_input("📂 Enter Genre")
    read_status = st.checkbox("📖 Mark as Read")
    content = st.text_area("📜 Enter Book Summary or Content")  # New field for book content
    
    if st.button("➕ Add Book"):
        if title and author:
            library.append({
                "title": title, "author": author, "year": year, 
                "genre": genre, "read": read_status, "content": content
            })
            save_library()
            animated_success("🎉 Book Added Successfully! 📚")
            st.rerun()
        else:
            animated_warning("⚠️ Please enter both Title and Author!")

elif menu == "Remove a Book ❌":
    st.header("🗑️ Remove a Book")
    book_titles = [book["title"] for book in library]
    
    if book_titles:
        selected_book = st.selectbox("📖 Select a book to remove", book_titles, key="remove_book")
        
        if st.button("❌ Remove Book"):
            library[:] = [book for book in library if book["title"] != selected_book]  # Fix: Update global list
            save_library()
            animated_success("🚀 Book Removed Successfully! 📖")
            st.rerun()
    else:
        st.warning("📭 No books available to remove!")

elif menu == "Search a Book 🔍":
    st.header("🔍 Search for a Book")
    search_term = st.text_input("🔎 Enter title or author name to search")
    
    if st.button("🔍 Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() 
                   or search_term.lower() in book["author"].lower()]
        
        if results:
            st.write("🎯 Matching Books:")
            for book in results:
                st.write(f"📖 **Title:** {book['title']}")
                st.write(f"✍️ **Author:** {book['author']}")
                st.write(f"📅 **Year:** {book['year']}")
                st.write(f"📂 **Genre:** {book['genre']}")
                st.write(f"✅ **Read:** {'Yes' if book['read'] else 'No'}")
                st.write(f"📜 **Summary:** {book.get('content', 'No summary available')}")
                st.write("---")
        else:
            animated_warning("❌ No books found with this search term!")

elif menu == "Display All Books 📚":
    st.header("📖 Your Library")
    library = load_library()  # Ensure updated books are displayed
    
    if library:
        st.write("📚 Here are all the books in your library:")
        for book in library:
            st.write(f"📖 **Title:** {book['title']}")
            st.write(f"✍️ **Author:** {book['author']}")
            st.write(f"📅 **Year:** {book['year']}")
            st.write(f"📂 **Genre:** {book['genre']}")
            st.write(f"✅ **Read:** {'Yes' if book['read'] else 'No'}")
            st.write(f"📜 **Summary:** {book.get('content', 'No summary available')}")
            st.write("---")
    else:
        animated_warning("📭 Your library is empty! Start adding books! 📚")

elif menu == "View Library 📊":
    st.header("📊 Library Statistics")
    total_books = len(library)
    books_read = sum(1 for book in library if book["read"])
    percentage_read = (books_read / total_books * 100) if total_books > 0 else 0
    
    st.write(f"📚 **Total Books:** {total_books}")
    st.write(f"✅ **Books Read:** {books_read}")
    st.write(f"📊 **Percentage Read:** {percentage_read:.2f}%")
    st.snow()

elif menu == "Save & Exit 💾":
    animated_success("💾 Library Saved! Exiting... 👋")
