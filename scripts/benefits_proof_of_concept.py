# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:05:58 2023

@author: COnnor.gibbs
"""

from py import data_loader

# Get the data folder
chosen_data_directory = data_loader.choose_directory()

# Get all data files in the directory
files = data_loader.get_files(chosen_data_directory)

# Get the text associated with a pdf
text = data_loader.read_pdf(files['.pdf'])

# Ask about fertility benefits
question = 'Do employees have access to fertility treatment based on this description of benefits?: \n'

# Get text
text_with_pages = list()
for x, y in enumerate(text):
    xp = x + 1
    if x == 0:
        text_with_pages.append('Page ' + str(xp) + '\n\n' + y)
    else:
        text_with_pages.append('\n\n' + 'Page ' + str(xp) + '\n\n' + y)
text_with_pages = ''.join(text_with_pages)

question_with_doc = question + ': \n "' + text_with_pages + '"'
question_with_text = [question + '"' + i + '"' for i in text]


import pyperclip

# split up documnent by table of contents
toc_pages = [int(s) for s in text[1].split("\n") if s.isdigit()]
toc_pages.append(len(text))
sections = list()
for x in range(len(toc_pages)-2):
    new_text = ''
    y = x + 1
    xp = toc_pages[x]
    yp = toc_pages[y]
    
    while xp <= yp:
        if xp == yp:
            new_text = new_text + '\n' + text[yp]
        else:
            new_text = new_text + text[xp]
        xp = xp + 1
    sections.append(new_text)
    
# append question
question_with_text = [question + '"' + i + '"' for i in sections]
    

# copy into free GPT and store responses
j = 1
pyperclip.copy(question_with_text[j])
    