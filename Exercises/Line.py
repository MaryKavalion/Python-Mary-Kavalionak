x_a = int(input("Insert the A-point's x coordinat: "))
y_a = int(input("Insert the A-point's y coordinat: "))
x_b = int(input("Insert the A-point's x coordinat: "))
y_b = int(input("Insert the A-point's y coordinat: "))
k = ((y_b - y_a)/(x_b - x_a))
m = y_a - k*x_a
print (f"The slope is k={k}, the intersection with y-axis is (0, {m})")
print (f"The equation formula is y = {k}x + {m}")