class Book:
    total_books = 3  #class variable 
        
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        
if __name__ == "__main__":
    Book.increment_book_count()
    
    print(f"Total Books Added: {Book.total_books}")