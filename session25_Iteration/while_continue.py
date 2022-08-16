while True:
    line = input('Help\n1->for exit write -> exit\n2->for empty print write -> #\n> ')
    if line[0] == '#':
        continue
    if line == 'exit':
        break
    print(line)
print('Exit Done Successfully!')

def myPrompt(object = ...):
    return str(object)

