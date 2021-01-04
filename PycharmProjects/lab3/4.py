import math

width = input("The width of the rectange:")
length = input("The length of the rectangle")
width = int(width)
length = int(length)

perimeter = width*2 + length*2
diagonal = math.sqrt(width*width + length*length)
perimeter = str(perimeter)
diagonal = str(diagonal)

print("The perimeter is equal to " + perimeter)
print("The diagonal is " + diagonal)