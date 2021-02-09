def factorial(n):
    # if n < 0:
    #     return None
    # if n==1 or n==0:
    #     return 1
    # return n * factorial(n-1)
    factorial = 1
    while n > 0:
        factorial = factorial * n
        n -= 1
    return factorial

def fibonacci(n):
    # if n == 0 or n == 1:
    #     return n
    # return fibonacci(n-1) + fibonacci(n-2)
    # fibonacci = 0
    fib_prev = 1
    fib_second_prev = 0
    i = 0
    while i <= n :
        if n == 0 or n == 1:
            fibonacci = 0
            print(fibonacci)
            continue
        fibonacci = fib_prev + fib_second_prev
        print(fibonacci)
        fib_second_prev = fib_prev
        fib_prev = fibonacci
        i+=1
    return fibonacci

print(fibonacci(5))