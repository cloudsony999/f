def test(x=100):
    print('x is ',x)


test(22)

def abc():
    print('I am abc')

def abc():
    print('I am abc again')

def abc():
    print('I am abc again again......')

abc()
# Method Overloading is not required in Python it is implicitly overloaded

def call(x):
    print('i am 1 arg ',type(x))



call('aaa')

call(11.34)

call(123)

call(True)




def demo(x,y):
    print(type(x),type(y))


demo(1,2)

demo(1.2,7)

demo('aa',True)

#Variable Arguments in a python function

def demotest(*x):
    print(x)



demotest(12)
demotest()
demotest(1,2,3,4,5,6,7,8,6,5,4,3,2,1)
demotest(12,34)
demotest(12,'aa',True,12.34)















