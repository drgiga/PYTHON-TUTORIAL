hello = "Hello, World!"
# Slicing in ranges
print(hello[2:5]) # Get the characters from position 2 to position 5 (not included)
# Slice From the Start
print(hello[:5]) # Get the characters from the start to position 5 (not included)
# Slice To the End
print(hello[5:]) # Get the characters from position 5, and all the way to the end
# Negative Indexing
print(hello[-5:-2])
print(hello[-len(hello):]) # Get the characters from from the end
print(hello[-13:]) # Get the characters from the end