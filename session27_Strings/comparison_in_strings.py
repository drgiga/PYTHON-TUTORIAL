print("String comparison -------")
sentence = 'My favorite fruit is banana'
#sentence = 'banana is My favorite fruit'
#sentence = 'banana'
word = "banana"

if sentence < word:
    print(f'Sentence:"{sentence}", "{word}": is at the end of the sentence .')
elif sentence > word:
    print(f'Sentence:"{sentence}", "{word}": is at the beginning of the sentence .')
else:
    print(f'Sentence:"{sentence}", is same "{word}".')
