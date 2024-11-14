from collections import defaultdict

class BookIndex:
    def __init__(self):
        self.word_to_pages = defaultdict(set)
    
    def index_pages(self, pages):
        for page_number, page in enumerate(pages, 1):  # page_number starts at 1
            words = page.split()  # split the page into words
            for word in words:
                self.word_to_pages[word].add(page_number)
    
    def get_pages(self, word):
        return self.word_to_pages.get(word, set())  # return the pages the word appears on

# Example Usage:
pages = [
    "The quick brown fox jumps over the lazy dog",  # Page 1
    "The fox is quick",  # Page 2
    "A quick red fox runs"  # Page 3
]

book_index = BookIndex()
book_index.index_pages(pages)

# Get pages for the word "quick"
print(book_index.get_pages("quick"))  # Output: {1, 2, 3}

# Get pages for the word "fox"
print(book_index.get_pages("fox"))  # Output: {1, 2, 3}

# Get pages for a word that doesn't appear in the book
print(book_index.get_pages("cat"))  # Output: set()

# ------
from collections import defaultdict

class BookIndex:
    def __init__(self):
        # Initialize a dictionary where the key is a word,
        # and the value is another dictionary mapping page numbers to word count.
        self.word_to_pages = defaultdict(lambda: defaultdict(int))
    
    def index_pages(self, pages):
        for page_number, page in enumerate(pages, 1):  # page_number starts at 1
            words = page.split()  # split the page into words
            for word in words:
                self.word_to_pages[word][page_number] += 1  # increment the count for this word on the page
    
    def get_word_count_on_page(self, word, page_number):
        return self.word_to_pages.get(word, {}).get(page_number, 0)  # return the count or 0 if not found
    
    def get_word_all_counts(self, word):
        return self.word_to_pages.get(word, {})  # return the dictionary of counts across all pages

# Example Usage:
pages = [
    "The quick brown fox jumps over the lazy dog",  # Page 1
    "The fox is quick",  # Page 2
    "A quick red fox runs"  # Page 3
]

book_index = BookIndex()
book_index.index_pages(pages)

# Get the count for the word "quick" on page 1
print(book_index.get_word_count_on_page("quick", 1))  # Output: 1

# Get the count for the word "fox" on page 2
print(book_index.get_word_count_on_page("fox", 2))  # Output: 1

# Get the count for the word "fox" across all pages
print(book_index.get_word_all_counts("fox"))  
# Output: {1: 1, 2: 1, 3: 1}

# Get the count for a word that doesn't exist
print(book_index.get_word_count_on_page("cat", 1))  # Output: 0
