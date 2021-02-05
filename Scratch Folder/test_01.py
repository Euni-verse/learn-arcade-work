# Learning variables and expressions

# printing text
answer = "bananas"
print(answer)

print("The answer is", answer)

# add a period (this will have a bigger space between answer and the period)
print("The answer is", answer, ".")

# to take out that space, use operator to separate
# and a space after the word is for a space between is and the answer
print("The answer is " + answer + ".")

# printing variables & text
answer = 45
# print("The answer is " + answer + ".")
# above doesn't work because the computer doesn't know how to put text and numbers together
# to fix this use str function which converts the number to a string (text)
print("The answer is " + str(answer) + ".")

# formatted string with an f before the quote
answer = 80
print (f"The answer is {answer}.")

# Rewrite v = 2(3.14r)
r = 7
v = 2 * (3.14 * r)

x = 8
x = x + 1
print(x)

# Use increment operator
x += 1
print(x)

# Use decrement operator
x -= 3
print(x)

# printing variable with explanation text
cat = 49
dog = x + 3
print(f"The cat equals {cat}, and the dog equals {dog}.")
