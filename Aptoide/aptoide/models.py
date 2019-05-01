# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import csv

# Create your models here.

import csv

"""Since we work only with the data from csv and 
only in memory, there is no need to create a  mode.
Specify the file path and load csv into a list when system loads
"""

filepath1='static/test_files/190titles.csv' #csv file path
filepath2='static/test_files/6500titles.csv' #csv file path

file_len = 0
file_path = ''
def openmy_file(filepath):
    """Function to load csv file and read data to list"""

    with open(filepath, 'rb') as f:
        reader = csv.reader(f)
        data = list(reader)
        file_len = len(data)
        file_path= filepath
        return data

choice_list = openmy_file(filepath2) # put list in a variable

