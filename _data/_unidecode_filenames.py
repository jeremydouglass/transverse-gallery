#!/usr/bin/env python2

# using homebrew requirements:

# pip2 install unidecode
import unidecode
import os

#------------------------------------------------
def unidecode_filename(path):
    """
    """
    files = os.listdir(path)
    for file in files:
        orig = os.path.join(path, file)
        new = os.path.join(path, unidecode.unidecode(file))
        if orig != new:
            print orig
            print new
            os.rename(os.path.join(path, file), os.path.join(path, unidecode.unidecode(file)))

#------------------------------------------------
if __name__ == "__main__":
    # input is of type 'unicode'
    unidecode_filename(u'../assets/gamebooks/edges/')
    unidecode_filename(u'../assets/gamebooks/graphviz/')
    unidecode_filename(u'../assets/gamebooks/image/')
    unidecode_filename(u'../assets/gamebooks/log/')
    unidecode_filename(u'../assets/gamebooks/signatures/counts/')
    unidecode_filename(u'../assets/gamebooks/signatures/nocounts/')
    unidecode_filename(u'../assets/gamebooks/signatures/thumbs/')
    unidecode_filename(u'../assets/gamebooks/tgf/')
    unidecode_filename(u'../assets/gamebooks/thumb/')

# https://stackoverflow.com/a/2633310/7207622
