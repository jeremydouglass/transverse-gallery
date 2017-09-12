#!/usr/bin/env python2

# using homebrew requirements:

# pip2 install unidecode
import unidecode
import codecs
import os

#------------------------------------------------
def unidecode_file_contents(filename):
    """
    """
    orig_data=""
    unidecode_data=""

    with codecs.open(filename, encoding='utf-8', mode='r') as f:
        orig_data = f.read()
        unidecode_data = unidecode.unidecode(orig_data)

    if orig_data != unidecode_data:
        print filename
        with codecs.open(filename, encoding='utf-8', mode='w+') as f:
            f.write(unidecode_data)

#------------------------------------------------
if __name__ == "__main__":
    # input is of type 'unicode'
    unidecode_file_contents('graph_data.tsv')
    unidecode_file_contents('image_list.tsv')
    unidecode_file_contents('signatures_list.tsv')

# https://stackoverflow.com/a/2633310/7207622
