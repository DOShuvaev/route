class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y


class Square(Shape):
    all_square = []

    def __init__(self, a=1, x=0, y=0):
        super().__init__(x, y)
        self.all_square.append(self)

    @classmethod
    def total_area(cls):
        area = 0
        for square in cls.all_square:
            area += cls.square_area(square.a)
        return area

    @staticmethod
    def square_area(a):
        return a ** 2


class Rectangle(Square):
    all_rectangles = []
    def __init__(self, x, y, a = 3, b = 5):
        super().__init__(x, y)
        self.a = a
        self.b = b
        self.all_rectangle.append(self)


    @classmethod
    def total_area_rec(cls):
        area = 0
        for с in cls.all_rectangles:
            area = area + с.rectangle_area(c.a, c.b)
        return area

    @staticmethod
    def rectangle_area(a, b):
        return a * b



class Circle(Shape):
    pi = 3.14159
    all_circles = []

    def __init__(self, radius=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius
        self.all_circles.append(self)

    @classmethod
    def total_area(cls):
        area = 0
        for circle in cls.all_circles:
            area += cls.circle_area(circle.radius)
        return area

    @staticmethod
    def circle_area(radius):
        return __class__.pi * radius * radius



sq = Square()
sq.total_area()