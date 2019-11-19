#global
data="Hello world"
def demo():
    #data="Hello"
    print(data)
    print(type(data))

demo()
print(data)

test=demo
print(type(test))
test()

def caller(a):
    print(type(a))
    print('inside')
    a()

caller(demo)
