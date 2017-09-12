#!/usr/bin/env python
from shutil import copy
import csv

#------------------------------------------------
def create_collection_stubs(data_file_path, template_file_path, out_dir):
    """
    Process the file line by line using the file's returned iterator
    """
    with open(data_file_path) as file_handle:
        tsv = csv.reader(file_handle, delimiter='\t')
        next(tsv, None) # skip header row
        for row in tsv:
            copy(template_file_path, out_dir + row[0] + '.md')

#------------------------------------------------
if __name__ == "__main__":
    data_file_path = '../_data/book_data.tsv'
    template_file_path = '../_data/gamebooks-template.md'
    out_dir = ''
    create_collection_stubs(data_file_path, template_file_path, out_dir)