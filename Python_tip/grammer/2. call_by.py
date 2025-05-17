#Call by reference vs Call by value

#Call by Value:
#Copying the value using stack
#thus, even if you change the copying value, original value doesn't change their own

#Call by reference:
#Copying reference to indicate locate of value

#But, Python is not both call by reference and call by value
#Python introduces call by assignment(call by object-reference)

#If assignment is Immutable object then, using the call by value
#or assignment is mutable object, then using the call by reference

#Immutable: tuple, str, int
#Mutable: list, set, dictionary

#Conclusion:
#Python's the way of calling the function is differed by object's data structure


#*Tip
#There's a concept of Equality and identity
#if you want to just compare with two value
#use '==' or if you want to compare precisely two value(that's gonna be check whether 식별번호) use 'is'

a = [1,2,3]
id(a)
# 4380442688

b = a
id(b)
# 4380442688
# Indicating same reference

# If you want to create different reference copy, then use [:] or copy
a = [1,2,3]
b = a[:]

from copy import copy
a = [1,2,3]
b = copy(a)
b is a
# False

