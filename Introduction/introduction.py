##################### Variables and assignments #################################
x = 2
y = x

# Both x and y are pointing to the value 2

z = x + y + 1

# Will calculate and allocate the number 5 to z

print(z)

# Intro to data types
from decimal import Decimal

x = 5
f = 0.1
# Decimal is not part of standard library. Is like the float type but will round to the closest decimal point
d = Decimal('0.1')
b = False
n = None

print(type(x))
print(type(f))
print(type(d))
print(type(b))
print(type(n))

# Display difference between Decimal and float.
print(f * 3)
print(d * 3)


# Reading Tests
# Need to be proficient with test-driven environment
def add(xy, zy):
    return xy + zy

# Long version of checking if answer matches
if add(2, 3) != 5:
    print("Broken Add")

if add(2, 5) != 7:
    print("Broken Add")

if add(8, 5) != 13:
    print("Broken Add")

# assert [condition]
assert add(2, 3) == 5, "2 + 3 not working"
assert add(2, 5) == 7
assert add(8, 5) == 13


# print(add(2, 3))  # 5
# print(add(2, 5))  # 7
# print(add(8, 5))  # 13
