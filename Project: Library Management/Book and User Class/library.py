class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def __str__(self):
        return f"{self.name} Library with {len(self.books)} books and {len(self.users)} users"
