#!/usr/bin/env python

import csv

source = 'book_data_2.tsv'
output = 'book_data.tsv'

with open(source, 'r') as infile, open(output, 'a') as outfile:
    # output dict needs a list for new column ordering
    fieldnames = ['id',
                  'box',
                  'folder', 
                  'series', 
                  'title', 
                  'author',
                  'citation', 
                  'book_id', 
                  'series_id',
                  ]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t', extrasaction='ignore')
    # reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile, delimiter='\t'):
        # writes the reordered rows to the new file
        writer.writerow(row)

