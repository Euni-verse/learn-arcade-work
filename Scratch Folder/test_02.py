# Learning Functions

# define your Function
def print_hello():
# then write a small summary of what the function does
    """This is a comment that describes the function. """
print("Hello!")

# definining multiple functions before calling
def print_hello():
    print("Hello!")

def print_goodbye():
    print("Bye Bye!")

# This is the main code call
print_hello()
print_goodbye()

# Using a main function

def print_rawr():
    print("RAWRRR!")

def print_ouch():
    print("FOUCH!")

def main():
    """ This is my main program function """
    print_rawr()
    print_ouch()

# Call (run) the main function
main()


# Parameters

def print_number(my_number):
    print(my_number)

print_number(55)
print_number(25)
print_number(8)

def add_numbers(a, b):
    print(a + b)

add_numbers(11, 7)

# Returning Values

# add two numbers and return the results
def sum_two_numbers(a, b):
    result = a + b
    return result

# This doesn't do much because nothing prints to screen
sum_two_numbers(22, 15)

# We need to caputre the returned result
# Capture the function's result into a variable
my_result = sum_two_numbers(22, 15) # This line captures the result

#After capturing, I can print it
print(my_result)


# MY OWN TEST

def sum_4_numbers(a, b, c, d):
    result = a + b - c * d
    return result
my_result = sum_4_numbers(22, 55, 10, 2)
print(my_result)


# Difference between printing a value and returning one

# This function will print the result
def sum_print(z, x):
    result = z + x
    print(result)

sum_print(4, 4)

# TESTS FOR RESULT

def triangle(x, y, z):
    result = (x + y) * z
    return result
udi = triangle(5, 9, 10) # capturing means making the result of these values into a variable
print(udi)

def phrases():
    print("Cherry Bomb")
phrases()

def numbers(x, y, v):
    result = x * y / v
    return result
chi = numbers(4, 5, 6)
print(chi)

def number_one(r, a, t, s):
    result = (r / a) * (t - s)
    return result
number_one(300, 10, 349, 45)

# TEST RETURN

def equation(e, t, a):
    result = (e / t) * a
    return result

lala = equation(9033, 495, 32)
print(lala)
print(equation(9033, 495, 32))

print(number_one(lala, udi, chi, 4))

def number(w, r, o, t, e):
    result = (w * r) + (o * t) / e
    return result

umby = number(4, 9, 10, 1000, 2)
print(umby)

print(number_one(umby, lala, udi, chi))


def calculate_average(a, b):
    result = (a + b) / 2
    return result

x = 45
y = 56

rudder = calculate_average(x, y)
print(rudder)

# EXAMPLE 1

def a():
    print("Example 1")
    print("A")

def b():
    print("B")

def c():
    print("C")

a()


# EXAMPLE 2

def a():
    print("Example 2")
    b()
    print("A")

def b():
    c()
    print("B")

def c():
    print("C")

a()

# EXAMPLE 3

def a():
    print("Example 3")
    print("A")
    b()

def b():
    print ("B")
    c()

def c():
    print("C")

a()

# EXAMPLE 4

def a():
    print("Example 4")
    print("A start")
    b()
    print("A end")


def b():
    print("B start")
    c()
    print("B end")


def c():
    print("C start and end")

a()

# EXAMPLE 5

def a(x):
    print("Example 5")
    print("A start, x =", x)
    b(x + 1)
    print("A end, x =", x)


def b(x):
    print("B start, x =", x)
    c(x + 1)
    print("B end, x =", x)


def c(x):
    print("C start and end, x =", x)


a(5)

# EXAMPLE 6

def a(x):
    print("Example 6")
    x = x + 1

x = 3
a(x)

print(x)

# EXAMPLE 8

def a(x):
    print("Example 8")
    x = x + 1
    return x


x = 3
x = a(x)

print(x)

# EXAMPLE 9

def a(x, y):
    print("Example 9")
    x = x + 1
    y = y + 1
    print(x, y)


x = 10
y = 20
a(y, x)

# EXAMPLE 11 return two values by using a comma and listing them

def a(x, y):
    print("Example 11")
    x = x + 1
    y = y + 1
    return x, y


x = 10
y = 20
z = a(x, y)

print(z)

# EXAMPLE 12 if you return two values you can capture it this way

def a(x, y):
    print("Example 12")
    x = x + 1
    y = y + 1
    return x, y


x = 10
y = 20
x2, y2 = a(x, y) # Most computer languages don't support this

print(x2, y2)
print(y2)

# EXAMPLE 13

def a(my_data):
    print("function a, my_data =  ", my_data)
    my_data = 20
    print("function a, my_data =  ", my_data)


my_data = 10

print("Example 13")
print("global scope, my_data =", my_data)
a(my_data)
print("global scope, my_data =", my_data)

# EXAMPLE 14

def a(my_list):
    print("function a, list =  ", my_list)
    my_list = [10, 20, 30]
    print("function a, list =  ", my_list)

my_list = [5, 2, 4]

print("Example 14")
print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)


# EXAMPLE 15

def a(my_list):
    print("function a, list =  ", my_list)
    my_list[0] = 1000
    print("function a, list =  ", my_list)


my_list = [5, 2, 4]

print("Example 15")
print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)
