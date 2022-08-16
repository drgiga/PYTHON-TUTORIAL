print("Strings are immutable ------")
sentence = 'My Name ****.'
# sentence[0] = 'J' # TypeError: 'str' object does not support item assignment
"""
The reason for the error is that strings are immutable, which means you can’t
change an existing string.
"""

"""
# Solution
The best you can do is create a new string that is a
variation on the original
"""

sentence = 'My Name ****.' # index [0:12] length:13
modified_sentence = "My Name Is Davoud." # index[0:17] length:18
new_sentence = sentence[13:] + modified_sentence

print(new_sentence)
print("lenght of new sentence",len(new_sentence))

print(f"id of sentence with value:{sentence}:",id(sentence))
print(f"id of modified_sentence with value:{modified_sentence}:",id(modified_sentence))
print(f"id of new_sentence with value:{new_sentence}:",id(new_sentence))
