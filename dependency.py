class Document:
  def __init__(self, content):
    self.content = content

class Printer:
  def print_document(self, doc):
    print(f"Printing document content: {doc.content}")

if __name__ == "__main__":
  doc = Document("Hello World!")
  printer = Printer()
  printer.print_document(doc)