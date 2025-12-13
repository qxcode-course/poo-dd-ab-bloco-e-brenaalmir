from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getPerimeter(self):
        pass

    @abstractmethod
    def getName(self):
        pass


class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"


class Circle(Shape):
    def __init__(self, center: Point2D, radius: float):
        self.name = "Circ"
        self.center = center
        self.radius = radius

    def getName(self):
        return self.name

    def getArea(self):
        return math.pi * self.radius ** 2

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circ: C={self.center}, R={self.radius:.2f}"


class Rectangle(Shape):
    def __init__(self, p1: Point2D, p2: Point2D):
        self.name = "Rect"
        self.p1 = p1
        self.p2 = p2

    def getName(self):
        return self.name

    def getArea(self):
        largura = abs(self.p1.x - self.p2.x)
        altura = abs(self.p1.y - self.p2.y)
        return largura * altura

    def getPerimeter(self):
        largura = abs(self.p1.x - self.p2.x)
        altura = abs(self.p1.y - self.p2.y)
        return 2 * (largura + altura)

    def __str__(self):
        return f"Rect: P1={self.p1} P2={self.p2}"

def main():
    shapes = []
    while True:
        line = input().strip()
        args = line.split()
        print("$" + " ".join(args))

        if args[0] == "circle":
            x, y, r = map(float, args[1:])
            shapes.append(Circle(Point2D(x, y), r))

        elif args[0] == "rect":
            x1, y1, x2, y2 = map(float, args[1:])
            shapes.append(Rectangle(Point2D(x1, y1), Point2D(x2, y2)))

        elif args[0] == "show":
            for s in shapes:
                print(s)

        elif args[0] == "info":
            for s in shapes:
                print(f"{s.getName()}: A={s.getArea():.2f} P={s.getPerimeter():.2f}")

        elif args[0] == "end":
            break


main()