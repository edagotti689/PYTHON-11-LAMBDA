'''
1. using iterators we can get sequence of values based on demand using next() function.
'''

l = [1,2,3,4,5]

for i in l:
   print(i)

# iter_obj = iter(l)
# print(next(iter_obj))

# print(next(iter_obj))

# for i in iter_obj:
    # print(' For loop ', i)


'''
StopIteration
'''

'''

# Comparison Between Python Generator vs Iterator
'''
'''
Let’s see the difference between Iterators and Generators in python.

In creating a python generator, we use a function. But in creating an iterator in python, we use the iter() and next() functions.
A generator in python makes use of the ‘yield’ keyword. A python iterator doesn’t.
Python generator saves the states of the local variables every time ‘yield’ pauses the loop in python. An iterator does not make use of local variables, all it needs is iterable to iterate on.
A generator may have any number of ‘yield’ statements.
You can implement your own iterator using a python class; a generator does not need a class in python.
To write a python generator, you can either use a Python function or a comprehension. But for an iterator, you must use the iter() and next() functions.
Generator in python let us write fast and compact code. This is an advantage over Python iterators. They are also simpler to code than do custom iterator.
Python iterator is more memory-efficient. Lest see this with example below:
'''
