class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.y < other.y or (self.y == other.y and self.x < other.x)

    def __gt__(self, other):
        return other < self

    def __str__(self):
        return f"{self.x};{self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
