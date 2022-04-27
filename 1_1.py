
"""

area of the cylinder

"""
pi: float = 3.14159

r = float(input("enter the radius of the cylinder: "))

h = float(input("enter the height of the cylinder: "))

#cylinder volume

v : float = h * r**2 * pi
print("cylinder volume is ",v)

#cylinder area

a : float = 2 * pi * r * h + 2 * (pi * r**2)
print("cylinder area is ",a)

m = 14