#!/usr/bin/python3

class Square():
    
    side = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Calculate the area of the square """
        return self.side ** 2

    def perimeter_of_my_square(self):
        """ Calculate the perimeter of the square """
        return 4 * self.side

    def __str__(self):
        return "{}x{}".format(self.side, self.side)

if __name__ == "__main__":
    s = Square(side=12)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
