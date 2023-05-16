#!/usr/bin/python3

class Square():
    def __init__(self, side):
        self.side = side

    def area(self):
        """Area of the square"""
        return self.side * self.side

    def perimeter(self):
        """Perimeter of the square"""
        return 4 * self.side

    def __str__(self):
        return "{}/{}".format(self.side, self.side)

if __name__ == "__main__":
    s = Square(side=12)
    print(s)
    print(s.area())
    print(s.perimeter())
