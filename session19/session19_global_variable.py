x = 200
def myfunc():
  global x
  x = 300
  def myfunc2():
    global x
    x = 400
  print(x)

myfunc()

print(x)