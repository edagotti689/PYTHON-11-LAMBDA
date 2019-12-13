'''
1. zip() is used to map the similar index of multiple containers and returns an zip object.
2. Using zip we can make combination of multiple listes
'''

l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e','f']

# zo = zip(l1, l2, ['X','Y','Z'])
zo1 = zip(l1, l2)

#print(' zip values are :', list(zo))

## Create a dictionary based on zip return value
print(' zip values are :', dict(zo1))







