'''
1. Using string format we can create a new string
'''
sname = input("Please enter surname  :")
fname = input("Please enter first name :")
lname = input("Please enter last name  :")

print(' \n Full anme is : ',sname, ' ', fname, ' ',lname)

#print(' \n Full anme is : ' + sname + ' ' + fname + ' ' + lname)

## Old format
#print('\n Full anme is :  %s  %s  %s'%(sname, fname, lname))

## New Format
# print('\n Full name is : {0} {1} {2}'.format(sname, fname, lname))
