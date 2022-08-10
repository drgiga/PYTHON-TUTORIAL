g = print(globals())
g

x = 'foo'
y = 29
g
print("------------------------------")
my_list = ['foo', 'bar', 'baz'] # global
def f():
    my_list = ['qux', 'quux'] # local

f()
print(my_list)
print("------------------------------")
name = "global" # global
def f():
    name = "local" # local

f()
print(name)
