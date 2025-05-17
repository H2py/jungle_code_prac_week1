words = ['cat', 'window', 'defense']
for w in words:
    print(w, len(w))
    
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
create_users = {}
for user, status in users.item():
    if status == 'active':
        create_users[user] = status 
        
# range 사용법
list(range(5,10))
[5, 6, 7, 8, 9]
list(range(0, 10, 3))
[0, 3, 6, 9]
list(range(-10, -100, -20))
[-10, -30, -50, -70, -90]

# If you input just 1 argument then, generates 10 values

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])
    
#0 Mary
#1 had
#2 a
#3 little
#4 lamb



# pass statement : does nothing at all. It can be used when a statement is required syntatically but the program required no action.

def http_error(status):
    match status:
        case 400:
            return 'Bad request'
        case 500:
            return 'Server Error'
        case 404:
            return 'Not found'
        case _:
            return "Something's wrong with the internet"
        
match point:
    case (0, 0):
        print(f"Origin")
    case (0, y):
        print(f"Y = {y}")
    case (x,y):
        print(f"X={x} Y={y}")
        

def fib(n):
    a,b = 0,1
    while a < n:
        print(a, end=' ')
        a,b = b , a+b
    print()
    
fib(2000)


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
        
        
i = 5

def f(arg=i):
    print(arg)
    
i = 6
f()

# Q. What's the value will return when f() is executed?
# A. The answer is that i = 6 is not defined earlier then def f so, def f can't use the i = 6

# How to use pass?

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else :
    print('카드를 꺼내라')