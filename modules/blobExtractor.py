import textblob

def getText(path, pagesPerChapter, linesPerPage):
	"""Get the text of a book as a string"""
	book = []
	pages = []
	with open(path, 'r') as f:
		counter = 0
		for line in f:
			if counter == 0:
				page = []
			
			page.append(line.replace("\n", ""))
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

def blobify(path, pagesPerChapter = 10, linesPerPage = 35):
	"""Make a text blob out of a string from a path"""
	book = getText(path, pagesPerChapter, linesPerPage)
	blobs = []
	for chapter in book:
		blob = textblob.TextBlob(chapter)
		blobs.append(blob)
	return blobs


