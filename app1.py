import json
from difflib import get_close_matches

data=json.load(open("EngThe/data.json"))

def translate(w):
    w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean %s instead ? Y for yes and N for No. " %get_close_matches(w,data.keys())[0])
        if yn=='Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=='N':
            return "The word doesn't exist. Please double check"
        else:
            return "We didn't understood your query."
    else:
        return "The word doesn't exist. Please double check"

word=input("Enter a word: ")
output=translate(word)
print(type(output))
j=1

if type(output)==list:
    for i in output:
        print(j ,i)
        j+=1
else:
    print(output)