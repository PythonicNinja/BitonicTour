# -*- coding: utf-8 -*-

from collections import namedtuple

import matplotlib.pyplot as plt

import sys
import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({},{})'.format(self.x, self.y)

    def distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)


class Result(object):
    def __init__(self, p1, p2, d=None):
        self.p1 = p1
        self.p2 = p2
        if not d:
            self.d = self.p1.distance(p2)
        else:
            self.d = d

    def __str__(self):
        return '({} <- {} -> {})'.format(self.p1, self.d, self.p2)

    def __repr__(self):
        return self.__str__()


def bitonic_tour(points):
    b = [None for _ in points]

    b[1] = Result(points[0], points[1])

    for j in range(2, len(points)):
        minimum = Result(None, None, sys.maxint)
        suma = 0
        for i in range(j - 2, -1, -1):
            d = Result(points[i], points[j], (b[i + 1].d + points[i].distance(points[j]) + suma))
            if d.d < minimum:
                minimum = d
            suma += points[i].distance(points[i + 1])
        b[j] = minimum

    return b


def bitonic_tour_with_final(points):
    b = bitonic_tour(points)
    final = b[-1].d + points[-1].distance(points[-2])
    return namedtuple('Result', 'b final')(b, final)


def plot(points):
    '''
    plots bitonic tour
    '''

    bitonic_path = bitonic_tour(points)

    for point in points:
        plt.plot(point.x, point.y, marker='o', linestyle='.', color='r', label='Points')

    for path in bitonic_path:
        if isinstance(path, Result):
            pair = [path.p1, path.p2]
            x_s = [(p.x, p.x) for p in pair]
            y_s = [(p.y, p.y) for p in pair]
            plt.plot(x_s, y_s, marker='o', linestyle='-', color='b', label='Path')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bitonic Path')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    points = [
        Point(0, 6),
        Point(1, 0),
        Point(2, 3),
        Point(5, 4),
        Point(6, 1),
        Point(7, 5),
        Point(8, 2)
    ]
    plot(points)