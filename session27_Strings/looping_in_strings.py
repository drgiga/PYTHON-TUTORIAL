print("----------------------------")
print("Looping and counting -------")
sentence = "My Name Is Davoud. I'm 35 Years Old. I Life in Tehran,Iran."
# Looping and counting
count = 0
search_char = 'a'
for letter in sentence:
    if letter == search_char:
        count = count + 1
print(f"Count of Character {search_char} :",count)