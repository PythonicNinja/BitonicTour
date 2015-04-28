#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bitonic_tour
----------------------------------

Tests for `bitonic_tour` module.
"""

import unittest

from bitonic_tour.bitonic_tour import bitonic_tour, bitonic_tour_with_final
from bitonic_tour.bitonic_tour import Point


class TestBitonic_tour(unittest.TestCase):

    def setUp(self):
        pass

    def test_line(self):
        points = [
            Point(1, 1),
            Point(2, 2),
            Point(3, 3),
            Point(4, 4)
        ]
        results = bitonic_tour_with_final(points)
        self.assertEqual(8.48528137423857, results.final)

    def test_testcase_from_web(self):
        points = [
            Point(1, 2),
            Point(3, 4),
            Point(5, 6),
            Point(7, 8),
        ]
        results = bitonic_tour_with_final(points)
        self.assertEqual(16.97056274847714, results.final)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
