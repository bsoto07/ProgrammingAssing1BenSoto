import unittest
import hw1
import data
import math


class TestCases(unittest.TestCase):
    def test_vowel_count_1(self):
        self.assertEqual(hw1.vowel_count(input("try using 6 vowels: ")), 6)


    def test_vowel_count_2(self):
        self.assertEqual(hw1.vowel_count(input("try using 3 vowels: ")), 3)


    def test_short_list_1(self):
        lis = [[4, 2], [2], [5, 3]]
        self.assertEqual(hw1.short_lists(lis), [[4, 2], [5, 3]])


    def test_short_list_2(self):
        lis = [[4, 2], [2], [5, 3]]
        self.assertNotEqual(hw1.short_lists(lis), [[4, 2], [2], [5, 3]])


    def test_ascending_pairs_1(self):
        lis = [[2, 55], [2, 0], [22], [20, 30, 2]]
        self.assertEqual(hw1.ascending_pairs(lis), [[2, 55], [0, 2], [22], [20, 30, 2]])


    def test_ascending_pairs_2(self):
        lis = [[2, 55], [2, 0], [22], [20, 30, 2]]
        self.assertNotEqual(hw1.ascending_pairs(lis), [[2, 55], [2, 0], [22], [20, 30, 2]])


    def test_add_prices_1(self):
        pri1 = data.Price(2, 2)
        pri2 = data.Price(4, 6)
        self.assertEqual(hw1.add_prices(pri1, pri2), 6.08)
        self.assertNotEqual(hw1.add_prices(pri1, pri2), 10)


    def test_add_prices_2(self):
        pri1 = data.Price(2, 2)
        pri2 = data.Price(4, 6)
        self.assertNotEqual(hw1.add_prices(pri1, pri2), 10)


    def test_rectangle_area_1(self):
        pt1 = data.Point(0, 0)
        pt2 = data.Point(2, 2)
        rect = data.Rectangle(pt1, pt2)
        self.assertEqual(hw1.rectangle_area(rect), int(input("what is the area of a rect w sides 2x2?: ")))


    def test_rectangle_area_2(self):
        pt1 = data.Point(0, 0)
        pt2 = data.Point(2, 2)
        rect = data.Rectangle(pt1, pt2)
        self.assertNotEqual(hw1.rectangle_area(rect), int(input("what is NOT the area of a rect w sided 2x2?: ")))


    def test_books_by_author_1(self):
        blist = hw1.booklist
        self.assertEqual(hw1.books_by_author('Ben', blist), [hw1.the_dragon])


    def test_books_by_author_2(self):
        blist = hw1.booklist
        self.assertEqual(hw1.books_by_author('Sydney', blist), [hw1.the_fairy])


    def test_circle_bound_1(self):
        pt1 = data.Point(0, 0)
        pt2 = data.Point(2, 2)
        rect = data.Rectangle(pt1, pt2)
        self.assertEqual(hw1.circle_bound(rect), data.Circle(data.Point(1, 1), math.sqrt(2)))


    def test_circle_bound_2(self):
        pt2 = data.Point(2, 2)
        pt3 = data.Point(6, 6)
        rect2 = data.Rectangle(pt2, pt3)
        self.assertEqual(hw1.circle_bound(rect2), data.Circle(data.Point(4, 4), math.sqrt(8)))


    def test_below_pay_average_1(self):
        self.assertEqual(hw1.below_pay_average(hw1.emplis1), ['Jack', 'Sydney', 'Papi'])


    def test_below_pay_average_2(self):
        self.assertNotEqual(hw1.below_pay_average(hw1.emplis1), ['Jack'])

