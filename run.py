from modules import blobExtractor
from modules import featureExtractor
from modules import arff_writer
import os
import random

books = []
for f in os.listdir('books'):
  books.append(f)

blobs = []
directory = 'books'
for b in books:
  blobs += blobExtractor.blobify(directory, b) 

blob_results = featureExtractor.get_features(blobs)
(attributes, data) = featureExtractor.sort_data(blob_results)
arff_writer.write_file('output/output.arff', attributes, data)
