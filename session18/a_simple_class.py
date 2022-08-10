class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

print(type(MyClass()))
print(type(MyClass().i))
print(type(MyClass().f))

print(MyClass())
print(MyClass().i)
print(MyClass().f)

newInstance = MyClass()
print(newInstance.__doc__)