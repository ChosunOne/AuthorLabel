from textblob import TextBlob
from blob import Blob

def getText(path, linesPerChapter):
	"""Get the text of a book as a string"""
	starting_line = 0
	ending_line = 0
	encoding = ''
	with open(path, 'r') as f:
		line_index = 0
		for line in f:
			if line.startswith('*** START OF THIS PROJECT GUTENBERG EBOOK') or line.startswith('***START OF THE PROJECT GUTENBERG EBOOK') or line.startswith('*END*THE SMALL PRINT'):
				starting_line = line_index + 1
			elif line.startswith('End of the Project Gutenberg EBook') or line.startswith('End of Project Gutenberg') or line.startswith('***END OF THE PROJECT GUTENBERG EBOOK'):
				ending_line = line_index - 1
			elif line.startswith('Character set encoding: '):
				encoding_label = 'Character set encoding: '
				line_end = line.find('\r')
				encoding = line[len(encoding_label):line_end]
			line_index += 1
		if ending_line == 0:
			ending_line = line_index - 1	

	chapters = []
	with open(path, 'r') as f:		
		line_index = 0
		line_count = 0
		chapter = ''
		for line in f:
			if starting_line <= line_index <= ending_line:
				line_text = line.replace('\n', ' ').replace('\r', '')
				if encoding in ['ASCII', 'US-ASCII', 'ISO-646-US (US-ASCII)']:
					line_text = line_text.decode('ascii', errors='replace')
				elif encoding == 'ISO-8859-1':
					line_text = line_text.decode('iso-8859-1', errors='strict')
				else:
					line_text = line_text.decode('iso-8859-1', errors='strict')
				chapter += line_text 
				if line_count == linesPerChapter:
					chapters.append(chapter)
					chapter = ''
					line_count = 0
				else:
					line_count += 1
			line_index += 1
		if chapter:
			chapters.append(chapter)	

	return chapters		

def getInfo(book):
	divider = ' by '
	split = book.replace('.txt', '').rpartition(divider)
	return split[2], split[0]

def blobify(directory, book, linesPerChapter = 350):
	"""Make a text blob out of a string from a path"""
	text = getText(directory + '/' + book, linesPerChapter)
	(author, title) = getInfo(book)
	blobs = []
	for chapter in text:
		tb = TextBlob(chapter)
		blobs.append(Blob(tb, author, title))
	return blobs
