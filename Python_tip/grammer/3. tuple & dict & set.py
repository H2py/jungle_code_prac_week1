t1 = (1, 2, 3)
del t1[0] #Error
# Tuple cannot be modified

# Dict means that hash or associative array
# Dict is consist of key-value pair

a = {1: 'hi', 'a': [1,2,3]}

del a[key]

# If you input overlapping data, it just shows you first data

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.keys()
a.values()
a.items()
a.clear()
# output : dict_keys(['name', 'phone', 'birth'])

for k in a.keys():
    print(k)
    
# output : name / phone / birth

for v in a.values():
    print(v)

'name' in a
# output: true

'email' in a

#output : False


s1 = set([1,2,3])
s1
# {1,2,3}


# Set's key feature
# 1 : Duplication is not allowed
# 2 : Unordered(순서 x)

# When you create a union or a different set then, set is super useful

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

s1 & s2 or s1.intersection(s2)
# output : {4, 5, 6}

s1 | s2 or s1.union(s2)
#output : {1,2,3,4,5,6,7,8,9}

s1 - s2 or s1.difference(s2)
s2 - s1 or s2.difference(s1)

s1.add(4)
# one value add

s1 = set([1,2,3])
s1.update([4,5,6])
# multiple value add

