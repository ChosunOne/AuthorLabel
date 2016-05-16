def write_file(path, attributes, data):
  with open(path, 'w') as f:
    f.write('@relation training\n\n')
    for attr in attributes:
      f.write(' '.join(['@attribute', "'" + attr.name + "'", attr.type]))
      f.write('\n')
    f.write('\n@data\n')
    for d in data:
      f.write(','.join(map(str, d)))
      f.write('\n')
