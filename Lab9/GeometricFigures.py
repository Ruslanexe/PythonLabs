class GeometricFigures:
    def __init__(self, name: str, dimension: str, quantity: int):
        self.name = name
        self.dimension = dimension
        self.quantity = quantity

    def show(self):
        print(self.name, self.dimension, self.quantity)
