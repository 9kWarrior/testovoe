import unittest
from main import MathHelper


class TestMathHelper(unittest.TestCase):


  def setUp(self):
    self.mathHelper = MathHelper()


  def test_square_circle(self):
    self.assertAlmostEqual(self.mathHelper.square_figure_circle(4), 50)


  def test_square_rectangle(self):
    self.assertEqual(self.mathHelper.square_figure_rectangle(3, 4, 5), 6)


  def test_isRectangleRightTriangle(self):
    self.assertEqual(self.mathHelper.isRectangleRightTriangle(3, 4, 5), True)


if __name__ == "__main__":
  unittest.main()