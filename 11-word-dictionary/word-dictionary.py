from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Write your word: ")
    
    if word == "":
        break
    
    print(dictionary.meaning(word))