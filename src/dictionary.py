import json
import difflib

data = json.load(open("data.json"))


def lookup(word):
    word = word.lower()
    try:
        return data[word]
    except KeyError:
        closestResults = difflib.get_close_matches(word, data)
        ans = input("Did you mean: " + closestResults[0] + "? (Y/N)\n")
        if ans == "Y":
            return data[closestResults[0]]
        else:
            return "Word doesn't exist in dictionary"


wordChoice = input("Enter a word: ")
result = lookup(wordChoice)
print(result)
