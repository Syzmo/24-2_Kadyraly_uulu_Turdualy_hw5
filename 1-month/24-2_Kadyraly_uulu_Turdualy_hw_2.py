class Figure:
    unit = 'cm'

    def __init__(self, _perimeter=0):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass
class Circle(Figure):

    def __init__(self, _radius):
        self.radius = _radius


    def calculate_area(self):
        area = (3.14 * self.radius) ** 2
        return area


    def info(self):
        area = (3.14 * self.radius) ** 2
        print(f'Cirkle radius: {self.radius} {self.unit}\n'
              f'{area} {self.unit}')


class RightTriangle(Figure):
    def __init__(self, _side_a, _side_b):
        self.side_a = _side_a
        self.side_b = _side_b

    def calculate_area(self):
        area = (self.side_a * self.side_b)/2
        return area

    def info(self):
        area = (self.side_a * self.side_b)/2
        print(f'Side a: {self.side_a}\n'
            f'Side b: {self.side_b}\n'
            f'area : {area}')

c1 = Circle(2)
c2 = Circle(4)

t1 = RightTriangle(3, 4)
t2 = RightTriangle(5, 2)
t3 = RightTriangle(9, 7)
figures = [c1, c2, t1, t2, t3]

for i in figures:
    i.info()