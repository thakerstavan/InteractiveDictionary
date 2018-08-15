import json

data = json.load(open("data.json"))


def lookup(word):
    word = word.lower()
    try:
        return data[word]
    except KeyError:
        return "Word doesn't exist in dictionary"


wordChoice = input("Enter a word: ")
result = lookup(wordChoice)
print(result)
