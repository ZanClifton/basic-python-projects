# Build a map function that takes a list as input and a function as input and returns a list of items where the function is applied to each item in the input list.

def maths_map(list, function):
    new_list = []
    for index in list:
        new_list.append(function(index))
    print(new_list)


number_list = [1, 6, 2, 17, -8, 102, 3]


def square(number):
    return number * number


def cube(number):
    return number * number * number


def multiply_by_two(number):
    return number * 2


def add_100(number):
    return number + 100


print("list of numbers:", number_list)

print("\nsquare:")
maths_map(number_list, square)
print("\ncube:")
maths_map(number_list, cube)
print("\nmultiply by 2:")
maths_map(number_list, multiply_by_two)
print("\nadd 100:")
maths_map(number_list, add_100)

# Build a filter function that takes a list as input and a function as input and returns a list of only those items which pass the condition specified in the function.


def filter_list(list, function):
    new_list = []
    for index in list:
        if function(index):
            new_list.append(function(index))
    print(new_list)


def is_even(number):
    if number % 2 == 0:
        return number


def is_odd(number):
    if number % 2 != 0:
        return number


def is_greater_than_five(number):
    if number > 5:
        return number


print("\nis even:")
filter_list(number_list, is_even)
print("\nis odd:")
filter_list(number_list, is_odd)
print("\nis greater than 5:")
filter_list(number_list, is_greater_than_five)
