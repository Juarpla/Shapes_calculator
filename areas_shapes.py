#importing the module math
import math

#Square procesing
square = input("\nWhat is the length of a side of the square in centimeters? ")
square_area = float(square) ** 2
square_area_m = square_area * 1 / 10000
cube_volume = float(square) ** 3
cube_volume_m = cube_volume * 1 / 10000
print(f"The area of the square in centimeters is: {square_area:,.4f} cm^2")
print(f"The volume of a cube in centimeters will be: {cube_volume:,.4f} cm^2")
print(f"The area of the square in meters is: {square_area_m:,.4f} m^2")
print(f"The volume of a cube in meters will be: {cube_volume_m:,.4f} m^2\n")

#Rectangle procesing
l_rectangle = input("What is the length of rectangle in centimeters? ")
w_rectangle = input("What is the width of rectangle in centimeters? ")
rectangle_area = float(l_rectangle) * float(w_rectangle)
rectangle_area_m = rectangle_area * 1 / 10000
print(f"The area of the rectangle in centimeters is: {rectangle_area:,.4f}cm^2")
print(f"The area of the rectangle in meters is: {rectangle_area_m:,.4f} m^2\n")

#Circle procesing
circle = input("What is radius of the circle in centimeters? ")
circle_area = math.pi * (float(circle) ** 2)
circle_area_m = circle_area * 1 / 10000
circle_volume = math.pi * (float(circle) ** 3) * 4 / 3
circle_volume_m = circle_volume * 1 / 10000
print(f"The area of the circle in centimeters is: {circle_area:,.4f} cm^2")
print(f"The volume of a circle in centimeters will be: {circle_volume:,.4f} cm^2")
print(f"The area of the circle in meters is: {circle_area_m:,.4f} m^2")
print(f"The volume of a circle in meters will be: {circle_volume_m:,.4f} m^2")