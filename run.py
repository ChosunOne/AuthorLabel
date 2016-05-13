from modules import blobExtractor
from modules import featureExtractor
import os
import random

books = []
for f in os.listdir('books'):
	if f.endswith("by Jonathan Swift.txt"):
		books.append(f)

book = random.sample(books, 1)[0]
print book
blobs = blobExtractor.blobify('books/' + book)
blob = random.sample(blobs, 1)[0]
#tags = featureExtractor.getTags(random.sample(blobs, 1)[0])
#tagCounts = featureExtractor.getTagCounts(tags)
#print featureExtractor.getTagPercentages(tagCounts)
#print featureExtractor.getSentiment()
print featureExtractor.getWordLength(blob)
print featureExtractor.getSentenceLength(blob)