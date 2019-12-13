'''
1. Lambda is a another way to create a function.
2. Lambda is a one line anonymous function it doesn't contains name.
3. Using lambda we can do only one expression.
'''

## Lambda with out arguments 
#add = lambda : 2 + 8
#r = add()
#print(r)

## Lambda with arguments 
# add = lambda a,b: a + 8
# r = add(2,3)
# print(r)

## Lambda with if and else
add = lambda a,b: b + 10 if a > 5 else a - b
print(add(4,50))
