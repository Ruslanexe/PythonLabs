from Lab9.GeometricFigures import GeometricFigures


class Circle(GeometricFigures):
    def __init__(self, name: str, dimension: str, quantity: int, no_corners: bool):
        super().__init__(name, dimension, quantity)
        self.no_corners = no_corners

    def show(self):
        print(self.name, self.dimension, self.quantity, self.no_corners)


class Triangle(GeometricFigures):
    def __init__(self, name: str, dimension: str, quantity: int, corners: int):
        super().__init__(name, dimension, quantity)
        self.corners = corners

    def show(self):
        print(self.name, self.dimension, self.quantity, self.corners)


class Cylinder(GeometricFigures):
    def __init__(self, name: str, dimension: str, quantity: int, volume: float):
        super().__init__(name, dimension, quantity)
        self.volume = volume

    def show(self):
        print(self.name, self.dimension, self.quantity, self.volume)


class Cone(GeometricFigures):
    def __init__(self, name: str, dimension: str, quantity: int, looks_like_a_pyramid: bool):
        super().__init__(name, dimension, quantity)
        self.looks_like_a_pyramid = looks_like_a_pyramid

    def show(self):
        print(self.name, self.dimension, self.quantity, self.looks_like_a_pyramid)


class Sphere(GeometricFigures):
    def __init__(self, name: str, dimension: str, quantity: int, exist: bool):
        super().__init__(name, dimension, quantity)
        self.exist = exist

    def show(self):
        print(self.name, self.dimension, self.quantity, self.exist)
