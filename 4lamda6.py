square = lambda side: side * side
rectangle = lambda l, b: l * b
triangle = lambda b, h: 0.5 * b * h

s = float(input("Enter side of square: "))
l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
bt = float(input("Enter base of triangle: "))
h = float(input("Enter height of triangle: "))

print(square(s))
print(rectangle(l, b))
print(triangle(bt, h))
