class Book:
  def __init__(self, title):
    self.title = title

class Library:
  def __init__(self, books=None):
    self.books = books if books else []

if __name__ == "__main__":
  b = Book("Python 101")
  lib = Library([b])
  print(f"Library has book: {lib.books[0].title}")