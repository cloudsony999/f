#its a function
def test(name):
    print("my name is ",name)


class Person:
    #now its a method
    def test(self,name):
        print("my name is ",name)


test('amitava')

p=Person()
p.test('sayan')

