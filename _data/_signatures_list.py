#!/usr/bin/env python
import os
import csv

#------------------------------------------------
def write_file_list(directory_path, data_file_path, out_dir):
    """
    """
    arr_txt = [f for f in os.listdir(directory_path)]
    print(arr_txt)
    with open(data_file_path,'w') as resultFile:
        wr = csv.writer(resultFile, delimiter='\t')
        wr.writerow(['box_folder','box','folder','image'])
        for txt in arr_txt:
            wr.writerow([txt[0:5],txt[0:2],txt[3:5],txt])

#------------------------------------------------
if __name__ == "__main__":
    directory_path = '../assets/gamebooks/signatures/counts/'
    data_file_path = 'signatures_list.tsv'
    out_dir = ''
    write_file_list(directory_path, data_file_path, out_dir)
