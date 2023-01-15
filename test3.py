import getpass as g
#its a function
def test(a,b):
    return a+b


x=test(int(input('enter 1st ')),int(input('enter 2nd ')))
if x>50:
    print(x , 'is > 50')


def pwd(p):
    return p

print('the password is ',pwd(g.getpass('enter password ')))