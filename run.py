from modules import blobExtractor

book = blobExtractor.getText('books/The Iliad by Homer.txt', 10, 35)
print len(book)
blobs = blobExtractor.blobify('books/The Iliad by Homer.txt', 10, 35)
print len(blobs)