from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))
print("Rectangle Coordinate: ", rectangle.point1.x, ",", rectangle.point1.y,
      "and", rectangle.point2.x, ",", rectangle.point2.y)

user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)
