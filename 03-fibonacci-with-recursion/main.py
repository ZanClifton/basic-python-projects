def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))


n = int(input("How many terms from the Fibonacci Sequence would you like to see?\nNumbers above 30 may take a long time to run.\nTerms: "))

if n <= 0:
    print("Naughty! Enter a positive whole number, please!")
elif n == 1:
    print(f"Here is 1 term of the Fibonacci sequence:")
    for i in range(n):
        print(fib(i))
else:
    print(f"Here are {n} terms of the Fibonacci sequence:")
    for i in range(n):
        print(fib(i))
