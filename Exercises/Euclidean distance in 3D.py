def coordinates (counter, text):
    array = []
    for c in range (counter):
        coordinate = int (input(f"Pls provide the first {text}'s coordinate № {c+1}: "))
        array.append (coordinate)
    return array

dimensions = 3

first_point = coordinates (dimensions, "first point")
second_point = coordinates (dimensions, "second_point")

import math
distance = math.sqrt(((first_point[0]-second_point[0])**2+(first_point[1]-second_point[1])**2+(first_point[2]-second_point[2])**2))
print (f"The distance is {distance:.2f} l.u.")
