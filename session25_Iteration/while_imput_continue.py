while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'exit':
        break
    print(line)
print('Exit Done Successfully!')

def myPrompt(object = ...):
    return str(object)