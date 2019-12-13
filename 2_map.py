'''
1. map is used to do operation on each iterable value and it will return all operations result in map object format.

2. Map takes two parameters one is function another one is iterable object

'''

## Map with def fucntion
def add(a,b):
    return  a + b

mo = map(add,(1,2,3,4,5,6),[9,8,7,6,5])
print(list(mo))

# Map with lambda function
# mo1= map(lambda a,b: 'ok',[1,2,3,4,5] , [10,20,30,40,50])
# print(tuple(mo1))

## Map with lambda if else
# s=[1,2,6,4]
# s1=[3,6,3,4]
# mo2 = map(lambda a,b: a+b if a > b else a - b,s,s1)
# print(list(mo2))