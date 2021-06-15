import json
import os
from difflib import get_close_matches
import easygui as eg

x = open('dictdata.json',)
data = json.load(x)

def query(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return 'Please check the word, the word does not exist in the database.'

title   = "Dictionary"
text    = "Enter the word"
d_text  = ""
output  = eg.enterbox(text, title, d_text)


result = query(str(output))
if type(output) == list:
    for y in output:
        print(y)
msg= eg.msgbox(result)
