

from pynput.keyboard import Key, Listener

def on_press(key):
    #print('{0} pressed'.format(
        #key))
    check_key(key)

def on_release(key):
    #print('{0} release'.format(
       # key))
    if key == Key.esc:
        # Stop listener
        return False

def check_key(key):
    if key in [Key.up, Key.down, Key.left, Key.right]: 
        if(key == Key.up):
            print('UP')
        elif(key == Key.down):
            print("DOWN")
        elif(key == Key.right):
            print("RIGHT")
        elif(key == Key.left):
            print("LEFT")
        else:
            print("no arrow key")

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()