class Point():
    def __init__(self, x, y):
        self.points = []
        self.x = x
        self.y = y

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.x} {self.y}"
