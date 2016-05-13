from textblob import TextBlob


def getTags(blob):
	"""Get the parts of speech tags from a blob"""
	return blob.tags

def getTagCounts(tags):
	"""Returns a dicitonary with the counts for each part of speech in the blob"""
	tagCounts = {}
	for t in tags:
		count = tagCounts.get(t[1], 0)
		tagCounts[t[1]] = count + 1
	return tagCounts

def getTagPercentages(tagCounts):
	"""Returns a dictionary of the parts of speech and the composition of the blob"""
	tagPercents = {}
	total = float(sum(tagCounts.values()))
	for t in tagCounts.keys():
		tagPercents[t] = tagCounts[t] / total
	return tagPercents

def getSentiment(blob):
	"""Returns the sentiment of a blob"""
	return blob.sentiment

def getWordLength(blob):
	"""Returns the average word length of a blob"""
	words = blob.words
	totalWords = len(words)
	totalChars = sum(len(s) for s in words)
	return float(totalChars) / totalWords

def getSentenceLength(blob):
	"""Returns the average sentence length of a blob"""
	sentences = blob.sentences
	totalSentences = len(sentences)
	totalWords = sum(len(s.words) for s in sentences)
	return float(totalWords) / totalSentences