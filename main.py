import json
import random
import string

input = "Hello. How are you?"

print("Hello. Beggining translation....")

wordsInInput = input.split()
#print(wordsInInput)

with open('flat/book-of-mormon-flat.json') as json_file:  
    bom = json.load(json_file)
with open('flat/doctrine-and-covenants-flat.json') as json_file:  
    dnc = json.load(json_file)
with open('flat/new-testament-flat.json') as json_file:  
    new = json.load(json_file)
with open('flat/old-testament-flat.json') as json_file:  
    old = json.load(json_file)
with open('flat/pearl-of-great-price-flat.json') as json_file:  
    pgp = json.load(json_file)

#bom = {"verses":[{"text":"hey kathy I","reference": "1 Nephi 1:1"},{"text":"1 2 3 hello 4 5 I","reference": "1 Nephi 1:2"}]}

output = ""

for word in wordsInInput:
    print(word)
    possibilities = []
    for verse in bom['verses']:
        wordsInVerse = verse['text'].split()
        wordsInVerse = [x.lower().translate(str.maketrans('', '', string.punctuation)) for x in wordsInVerse]
        #print(wordsInVerse)
        try:
            word = word.lower().translate(str.maketrans('', '', string.punctuation))
            index = wordsInVerse.index(word) + 1
            #print(index)
            possibilities.append(verse['reference'] + ":" + str(index))
        except:
            #print(-1)
            pass
    for verse in dnc['verses']:
        wordsInVerse = verse['text'].split()
        wordsInVerse = [x.lower().translate(str.maketrans('', '', string.punctuation)) for x in wordsInVerse]
        #print(wordsInVerse)
        try:
            word = word.lower().translate(str.maketrans('', '', string.punctuation))
            index = wordsInVerse.index(word) + 1
            #print(index)
            possibilities.append(verse['reference'] + ":" + str(index))
        except:
            #print(-1)
            pass
    for verse in pgp['verses']:
        wordsInVerse = verse['text'].split()
        wordsInVerse = [x.lower().translate(str.maketrans('', '', string.punctuation)) for x in wordsInVerse]
        #print(wordsInVerse)
        try:
            word = word.lower().translate(str.maketrans('', '', string.punctuation))
            index = wordsInVerse.index(word) + 1
            #print(index)
            possibilities.append(verse['reference'] + ":" + str(index))
        except:
            #print(-1)
            pass
    for verse in new['verses']:
        wordsInVerse = verse['text'].split()
        wordsInVerse = [x.lower().translate(str.maketrans('', '', string.punctuation)) for x in wordsInVerse]
        #print(wordsInVerse)
        try:
            word = word.lower().translate(str.maketrans('', '', string.punctuation))
            index = wordsInVerse.index(word) + 1
            #print(index)
            possibilities.append(verse['reference'] + ":" + str(index))
        except:
            #print(-1)
            pass
    for verse in old['verses']:
        wordsInVerse = verse['text'].split()
        wordsInVerse = [x.lower().translate(str.maketrans('', '', string.punctuation)) for x in wordsInVerse]
        #print(wordsInVerse)
        try:
            word = word.lower().translate(str.maketrans('', '', string.punctuation))
            index = wordsInVerse.index(word) + 1
            #print(index)
            possibilities.append(verse['reference'] + ":" + str(index))
        except:
            #print(-1)
            pass
    referenceToAppend = word
    if len(possibilities):
        referenceToAppend = random.choice(possibilities)
    output = output + "  " + referenceToAppend

print(output)
        
