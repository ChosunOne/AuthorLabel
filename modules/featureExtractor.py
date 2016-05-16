from textblob import TextBlob
from attribute import Attribute
from blob_result import BlobResult

def get_tags(blob):
	"""Get the parts of speech tags from a blob"""
	return blob.tags

def get_tag_counts(tags):
	"""Returns a dicitonary with the counts for each part of speech in the blob"""
	tagCounts = {}
	for t in tags:
		count = tagCounts.get(t[1], 0)
		tagCounts[t[1]] = count + 1
	return tagCounts

def get_tag_percentages(tagCounts):
	"""Returns a dictionary of the parts of speech and the composition of the blob"""
	tagPercents = {}
	total = float(sum(tagCounts.values()))
	for t in tagCounts.keys():
		tagPercents[t] = tagCounts[t] / total
	return tagPercents

def get_sentiment(blob):
	"""Returns the sentiment of a blob"""
	return blob.sentiment

def get_word_length(blob):
	"""Returns the average word length of a blob"""
	words = blob.words
	totalWords = len(words)
	totalChars = sum(len(s) for s in words)
	return float(totalChars) / totalWords

def get_sentence_length(blob):
	"""Returns the average sentence length of a blob"""
	sentences = blob.sentences
	totalSentences = len(sentences)
	totalWords = sum(len(s.words) for s in sentences)
	return float(totalWords) / totalSentences

def get_features(blobs):
	blob_results = []
	for b in blobs:
		tags = get_tags(b.textblob)
		tag_counts = get_tag_counts(tags)
		tag_percentages = get_tag_percentages(tag_counts)
		sentiment = get_sentiment(b.textblob)
		word_length = get_word_length(b.textblob)
		sentence_length = get_sentence_length(b.textblob)
		blob_results.append(BlobResult(tag_percentages, sentiment.polarity, sentiment.subjectivity, word_length, sentence_length, "'" + b.author + "'"))
	return blob_results
	
def get_tag_percentages_keys(blob_results):
	all_tag_percentages_keys = []
	for br in blob_results:
		all_tag_percentages_keys += br.tag_percentages.keys()
	return sorted(set(all_tag_percentages_keys))

def get_authors(blob_results):
	all_authors = []
	for br in blob_results:
		all_authors.append(br.author)
	return sorted(set(all_authors))		

def sort_data(blob_results):
	tag_percentages_keys = get_tag_percentages_keys(blob_results)
	attributes = []
	for key in tag_percentages_keys:
		attributes.append(Attribute(key, 'numeric'))
	for key in ['polarity', 'subjectivity', 'word length', 'sentence length']:
		attributes.append(Attribute(key, 'numeric'))
	authors = get_authors(blob_results)	
	attributes.append(Attribute('author', '{' + ','.join(authors) + '}'))	

	data = []
	for br in blob_results:
		row = []
		for key in tag_percentages_keys:
			row.append(br.tag_percentages.get(key, 0))
		row.append(br.polarity)
		row.append(br.subjectivity)
		row.append(br.word_length)
		row.append(br.sentence_length)
		row.append(br.author)
		data.append(row)

	return (attributes, data)	
