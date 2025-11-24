# -*- coding: utf-8 -*-
import csv

def open_mapping(filename):
  #definition of a dictionary for mapping.
  mapping = {}
  # open tab delimiter mapping file 
  f = open(filename, "r")
  csv_reader = csv.reader(f, delimiter="\t")
  #for each line in the mapping file
  for row in csv_reader:
    # if the line has more than one colum
    if len(row) > 1:
      #map the first column according to the second (search for codes in the first column, if its a match, replace for the corresponding one in the second column)
      mapping[row[0]] = row[1]

  return mapping

# creates map according to this file
map1 = open_mapping('mapping_file.csv')

#open network to be modified
f = open('network_file.tsv')
csv_reader = csv.reader(f, delimiter="\t")

#ignores the first row
headers = next(csv_reader, None)

#prints headers
print("\t".join(headers))

#for each row from the network file
for row in csv_reader:
  #defines the first column of the row in g1 and the second in g2
  g1 = row[0]
  g2 = row[1]
  
  #uses the mapping to replace the first column value, ignores if there is no match
  try:
    row[0] = map1[g1]
  except KeyError:
      pass
  #the same for column 2
  try:
    row[1] = map1[g2]
  except KeyError:
    pass

  #print new lines with new columns
  print("\t".join(row))


