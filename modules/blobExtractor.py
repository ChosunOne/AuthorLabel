from textblob import TextBlob
from blob import Blob

def getText(path, pagesPerChapter, linesPerPage):
	"""Get the text of a book as a string"""
	book = []
	pages = []
	with open(path, 'r') as f:
		counter = 0
		for line in f:
			if counter == 0:
				page = []
			
			page.append(unicode(line.replace('\n', ' ').replace('\r', ''), errors='replace'))
			counter += 1

			if counter > linesPerPage:
				counter = 0
				pages.append(page)
	chapter = []
	counter = 0
	for page in pages:
		if counter == 0:
			chapter = []

		chapter.append(page)
		counter += 1
		if counter > pagesPerChapter:
			counter = 0
			book.append(chapter)
	chapters = []
	for chapter in book:
		pages = ""
		for page in chapter:
			lines = ""
			for line in page:
				lines += line
			pages += lines
		chapters.append(pages)

	return chapters

def getInfo(book):
	divider = ' by '
	split = book.replace('.txt', '').rpartition(divider)
	return split[2], split[0]

def blobify(directory, book, pagesPerChapter = 10, linesPerPage = 35):
	"""Make a text blob out of a string from a path"""
	text = getText(directory + '/' + book, pagesPerChapter, linesPerPage)
	(author, title) = getInfo(book)
	blobs = []
	for chapter in text:
		tb = TextBlob(chapter)
		blobs.append(Blob(tb, author, title))
	return blobs
