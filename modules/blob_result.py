class BlobResult:
  def __init__(self, tag_percentages, polarity, subjectivity, word_length, sentence_length, author):
    self.tag_percentages = tag_percentages
    self.polarity = polarity
    self.subjectivity = subjectivity
    self.word_length = word_length
    self.sentence_length = sentence_length
    self.author = author
