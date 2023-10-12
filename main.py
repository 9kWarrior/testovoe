import math


class MathHelper:
    def __init__(self):
        pass


    def square_figure_rectangle(self, x, y, z) -> float:
        p = x + y + z
        p = p / 2
        square = math.sqrt(p*(p-x)*(p-y)*(p-z))
        return (square)


    def square_figure_circle(self, r) -> float:
        square = 3.14 * r * r
        return (square)


    def isRectangleRightTriangle(self, x, y, z) -> bool:
        hypo = max([x, y, z])
        katets = [x, y, z]
        katets.remove(hypo)
        if hypo**2 == katets[0]**2 + katets[1]**2:
            return True
        else:
            return False

mathHelper = MathHelper()
print(mathHelper.square_figure_rectangle(3, 4, 5))
print(mathHelper.square_figure_circle(4))
print(mathHelper.isRectangleRightTriangle(3, 4, 5))