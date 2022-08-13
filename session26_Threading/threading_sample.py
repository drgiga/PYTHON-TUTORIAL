import threading

def func_A():
  print("func_A")

def printit():
  threading.Timer(5.0, printit).start()
  threading.Timer(1, func_A).start()
  print("Hello, World!")

printit()


