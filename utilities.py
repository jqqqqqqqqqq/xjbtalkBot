
def test(number):
    return lambda x:x+number

f= test(10)
print f(3)