import streamlit as st
import json
import os

# File path to store data
FILE_PATH = 'library.json'

# Load library from file
def load_library():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(FILE_PATH, 'w') as file:
        json.dump(library, file, indent=4)

# Custom CSS for modern, sleek UI
st.markdown(
    """
    <style>
        /* Global Settings */
        .stApp {
            background: linear-gradient(to right, #FF8A00, #E52D27);
            color: #fff;
            padding: 50px 0;
            border-radius: 20px;
        }
        
        .stTitle {
            font-family: 'Roboto', sans-serif;
            font-size: 40px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 50px;
        }

        /* Sidebar Style */
        .sidebar .sidebar-content {
            background-color: #333;
            color: white;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        /* Section Box Style */
        .content-box {
            background: rgba(255, 255, 255, 0.2);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            margin-bottom: 30px;
        }

        /* Text Input Styling */
        .stTextInput>div>div>input {
            background-color: #fff;
            border-radius: 8px;
            padding: 14px;
            border: none;
            width: 100%;
            font-size: 16px;
            color: #333;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: 0.3s;
        }

        .stTextInput>div>div>input:focus {
            outline: none;
            border: 2px solid #FF8A00;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #FF8A00;
            color: white;
            padding: 12px 30px;
            font-size: 18px;
            border-radius: 30px;
            border: none;
            transition: 0.3s;
            cursor: pointer;
        }

        .stButton>button:hover {
            background-color: #E52D27;
            transform: scale(1.05);
        }

        /* Section Headers */
        h2, h3 {
            color: #FF8A00;
            font-family: 'Roboto', sans-serif;
            margin-bottom: 20px;
        }

        /* Empty Library Info */
        .stInfo {
            font-size: 18px;
            color: #E52D27;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("📚 Personal Library Manager")

# Initialize library
library = load_library()

# Sidebar Navigation
menu = st.sidebar.radio("Navigate", ["Add Book", "Delete Book", "Search Books", "List All Books"])

# Main Content Area
with st.container():
    # Add Book Section
    if menu == "Add Book":
        st.subheader("Add a New Book")
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        
        title = st.text_input("Book Title:")
        author = st.text_input("Author:")
        category = st.text_input("Category:")

        if st.button("Add Book"):
            if title and author and category:
                library.append({"title": title, "author": author, "category": category})
                save_library(library)
                st.success(f"'{title}' by {author} added successfully!")
            else:
                st.warning("Please fill all fields!")

        st.markdown("</div>", unsafe_allow_html=True)

    # Delete Book Section
    elif menu == "Delete Book":
        st.subheader("Delete a Book")
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        
        book_titles = [book['title'] for book in library]
        book_to_delete = st.selectbox("Select a book to delete:", ["Select..."] + book_titles)

        if st.button("Delete Book"):
            if book_to_delete != "Select...":
                library = [book for book in library if book['title'] != book_to_delete]
                save_library(library)
                st.success(f"'{book_to_delete}' removed successfully!")
            else:
                st.warning("Please select a book!")

        st.markdown("</div>", unsafe_allow_html=True)

    # Search Books Section
    elif menu == "Search Books":
        st.subheader("Search Books")
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        
        query = st.text_input("Enter search query (Title/Author):")

        if st.button("Search"):
            results = [book for book in library if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
            if results:
                st.write("### Search Results:")
                for idx, book in enumerate(results, start=1):
                    st.write(f"{idx}. {book['title']} by {book['author']} ({book['category']})")
            else:
                st.warning("No matching books found!")
        
        st.markdown("</div>", unsafe_allow_html=True)

    # List All Books Section
    elif menu == "List All Books":
        st.subheader("All Books in Library")
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        
        if library:
            for idx, book in enumerate(library, start=1):
                st.write(f"{idx}. {book['title']} by {book['author']} ({book['category']})")
        else:
            st.info("Your library is empty.")
        
        st.markdown("</div>", unsafe_allow_html=True)