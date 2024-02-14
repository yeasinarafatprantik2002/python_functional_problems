import math


def circle_stats(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return f"The area is {round(area, 2)} and the circumference is {round(circumference, 2)}"


circle_stats(5)
print(circle_stats(5))
