'''
1. Using generator we can execute a block of code based on demand using next() function.
2. using yield keyword we can create a generator.
'''

def gen_fun(n):
    for i in range(n):
        print('Before return')
        yield i
        print('After return')
        yield i

gen_obj = gen_fun(10)
print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))

## Iterate based on for loop
#for i in gen_obj:
#    print(' For Loop ', i)


# def gen_fun(n):
        # print('Before return')
        # yield 9
        # print('After return')
        # yield 5
