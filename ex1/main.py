#!/usr/bin/env python3
import mmap
import re

filename = input("Enter the file name to search: ")
wordname = input("Enter the word to be searched: ")

with open(filename, 'rb', 0) as file, \
        mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:

    wordnamebyte = str.encode(wordname)
    wordat = s.find(wordnamebyte)
    #wordat = re.search(wordnamebyte, s, re.IGNORECASE)

    if wordat != -1:
        print('Found at position # :' + str(wordat))
        print(s[wordat - 20:wordat + 25].decode())
        s.close()
    else:
    	print(' cant fine phrase ' + wordname + ' in filename ' + filename)
