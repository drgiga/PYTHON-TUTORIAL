def myfunc():
  x = 300
  print(x)
  def myinnerfunc():
    print(x)
  myinnerfunc()
  

myfunc()