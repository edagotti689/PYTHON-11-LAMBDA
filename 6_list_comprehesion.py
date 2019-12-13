'''
List comprehensions are used for creating new list from another iterables.

As list comprehension returns list, they consists of brackets containing the expression which needs to be executed for each element along with the for loop to iterate over each element.
'''

l = [1, 2, 3, 4]
## Basic list comprehension
r = [n+10 for n in l]

## list comprehension with if condition
#r = [n+2 for n in l if n > 2]

## list comprehension with if and else condition
# r = [n*2 if n > 2 else n + 10 for n in l]
print(r)

