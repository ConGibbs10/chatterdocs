# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:08:47 2023

@author: COnnor.gibbs
"""

# count files
import os
import pandas as pd
import numpy as np
from py import FileIO
from py import TokenUtils

## number of people
len(os.listdir('data/enron_mail_20150507'))

## get list of fields by person
path = os.path.abspath('data/enron_mail_20150507')
persons_path = [path + '\\' + x for x in os.listdir(path)]
person_files = [[*FileIO.absolute_file_paths(x)] for x in persons_path]
person_files = [item for row in person_files for item in row] #flatten

## create dataframe
files = pd.DataFrame({'path': person_files})
files['file_name'] = np.array([os.path.basename(x) for x in files['path']])
files['file_type'] = np.array([os.path.basename(os.path.dirname(x)) for x in files['path']])
files['person'] = np.array([os.path.basename(os.path.dirname(os.path.dirname(x))) for x in files['path']])
files = files[['path', 'person', 'file_type', 'file_name']]

## count words in a file
def count_words_and_tokens(path):
    file_lines = FileIO.read_txt_lines(path)
    file_lines = '\n'.join([' '.join(inner_list) for inner_list in file_lines])
    number_of_words = len(file_lines.split())
    thousands_of_tokens = TokenUtils.token_counter(file_lines, "gpt-3.5-turbo")/1000
        
    return (number_of_words, thousands_of_tokens)

## loop and record
words = []
tokens = []
for index, path in enumerate(files['path'], start = 1):
    print(f"{index} of {files.shape[0]}")
    words_and_tokens = count_words_and_tokens(path)
    words.append(words_and_tokens[0])
    tokens.append(words_and_tokens[1])
    
## update the dataframe
files['num_of_words'] = words
files['thousands_of_tokens'] = tokens

# save the data frame
files.to_csv('data/enron_mail_summarize_files.csv', index = False)
files.to_excel('data/enron_mail_summarize_files.xlsx', sheet_name='Enron Data', index=False)
