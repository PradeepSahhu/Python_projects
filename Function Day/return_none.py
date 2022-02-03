

'''
#Return statements.
def ret_Nothing():
    return 
def ret_None():
    return None
 
def ret_0():
    return 0
 
print(ret_Nothing() == None)
#True
print(ret_Nothing() is None) # correct way to compare values with None
#True
print(ret_None() is None)
#True
print(ret_0() is None)
#False
print(ret_0() == 0)
#True
# and...
print(repr(ret_Nothing()))
#'None'


# is - used to check as they are the same object .
# ==  - is used to check the equivalent...
'''
if (2 == 2.0):
    print("Both are equivalent")
if 2 is 2.0:
    print("Both are same:")
else:
    print("Good bye tata khatam")
