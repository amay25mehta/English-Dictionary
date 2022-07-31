import json
from difflib import get_close_matches  #difflib is a library in which method get_close_matches exist,it is used to compare best matches

data = json.load(open("data.json"))  #to open json file as a dictionary

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]   # using [] to access key value in the dict data.json
    elif w.title() in data: #in case of  proper nouns like Delhi,Mumbai
        return data[w.title()]    
    elif w.upper() in data: #in case user inputs words like USA etc    
        return data[w.upper()]


    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if YES ,N for NO: " %get_close_matches(w,data.keys())[0])  #%s is a string formater
        if yn == "Y" or yn =="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N" or yn=="n":
            return "Word doesn't exist,Please double  check it"
        else :
            return "We didn't understand your query :["    


    else:
        return "Word doesn't exist,Please double  check it "

word = input("Enter a word : ")

output = translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)        