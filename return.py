import json

data = json.load(open('data.json'))


# def word_finder(data, w):

#   if w in data :
#    return data[w]

#   else:
#    return print('data not found')

# word = input("Enter word: ")

# print(word_finder(data,word))

data = json.load(open("data.json"))
  
def translate(w):
    if w in data:
        return data[w]
    else:
        return"The world doesn't exit. Please double check"


word = input("Enter word:  ")


print(translate(word))