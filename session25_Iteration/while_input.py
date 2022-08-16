text = ""
while True:
    line = input('for exit write : exit \n> ')
    if line == 'exit':
        break
    text += line
    print(line)
print('Exit Done!')
print(text)
