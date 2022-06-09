print("Welcome to FizzBuzz!")
number = input("Which number would you like to run FizzBuzz to? ")
end = int(number) + 1

for i in range(1, end):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
