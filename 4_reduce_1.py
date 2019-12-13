'''
1. reduce is used to do operation on each iterable value and return all operations result sum.
2. reduce takes two parameters one is function another one is iterable object

'''

from functools import reduce

#(1+2)+3)+4)+5)
rv = reduce(lambda a,b: a * b,[1,2,3,4,5])
# rv1 = reduce(lambda a,b: a + b,[1,2,3,4,5])
# print(rv1)
print(rv)




'''
Error:

    print(list(f))
TypeError: 'int' object is not iterable

'''


