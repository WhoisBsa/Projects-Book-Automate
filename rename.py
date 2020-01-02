#! python3
# -*- coding: utf-8 -*-


""" File rename program for a sequential pattern """


import os
import sys
import time


# Indicates which directory to change
directory = sys.argv[1]

source = str(input('Default Name: '))
type = str(input('Type of file (txt, pdf, docx, etc...): '))
date = str(input('Year: '))

for root, _, files in os.walk(directory):
    for i, file in enumerate(files):
        if file.endswith(type):
             os.rename(os.path.join(root, file), f'{directory}{source}_{i+1:03}_{date}.{type}')
