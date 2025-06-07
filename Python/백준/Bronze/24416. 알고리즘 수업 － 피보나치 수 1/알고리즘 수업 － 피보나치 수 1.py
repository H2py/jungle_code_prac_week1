def fib_counter(n):
    memo = [0] * (n + 1)

    def fib(x):
        if x == 1 or x == 2:
            return 1
        if memo[x]:
            return memo[x]
        memo[x] = fib(x - 1) + fib(x - 2)
        return memo[x]

    count_code1 = fib(n)  
    count_code2 = n - 2   
    return count_code1, count_code2

n = int(input())
a, b = fib_counter(n)
print(a, b)
