# If you want to get multiple input then, using *agrs
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

# It can be modified add_many(1,2,3,4,5) or add_many(1)
# And also you can specify 1 parameter with *args

def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result

def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(name='foo', age=3)

# list.pop ==> print(las_items) and pop
# list.index(x, start, end)

def foo(**kwargs):
    print(kwargs)
    
foo(a=1, b=2, c=3)
#{'a':1, 'b':2 ,'c': 3}


#lambda function

def mul5(x):
    return 5*x

a = lambda x : 5 * x
a = lambda x : 120 // x