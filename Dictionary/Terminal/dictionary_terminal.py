import json
import os
from difflib import get_close_matches


x = open('dictdata.json',)
data = json.load(x)

def query(w):
    w = w.lower()
    if w in data:
        print('THE MEANING FOR THE ENTERED WORD IS AS FOLLOW:\n') 
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y if yes (or) N if no:" %get_close_matches(w,data.keys())[0])
        if yn == 'Y':
                return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
                return "The word does not exist in the database."
        else:
                return "We did not understand your entry"
    else:
        return 'The word does not exist in the database.'


in_word = input("Enter the word:")
output = query(in_word)
if type(output) == list:
    for y in output:
        print(y)
print(output)
