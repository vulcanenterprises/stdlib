"""
sparse_vector.py
=========================================================
The sparse_vector.py module for python stdlib
"""
import math
from typing import Dict

from stdlib.excepts.exceptions import IllegalArgumentException


class SparseVector(object):
    def __init__(self, d: int):
        self.d: int = d
        self.st: Dict = {}

    def put(self, i: int, value: float) -> None:
        if i < 0 or i >= self.d:
            raise IllegalArgumentException("Illegal index")

        if value == 0.0:
            self.st.__delitem__(i)

        else:
            self.st[i] = value

    def get(self, i: int) -> float:
        if i < 0 or i >= self.d:
            raise IllegalArgumentException("Illegal index")

        if i in self.st:
            return self.st.get(i)

        else:
            return 0.0

    def __sizeof__(self) -> int:
        return self.d

    def nnz(self) -> int:
        return len(self.st)

    def dimension(self) -> int:
        return self.d

    def dot_object(self, that) -> float:
        """

        :param that:
        :type that: SparseVector
        :return:
        :rtype:
        """
        if self.d != that.d:
            raise IllegalArgumentException("Vector lengths are different")

        summ = 0.0
        if len(self.st) <= len(that.st):
            for i in self.st.keys():
                if i in that.st:
                    summ += self.get(i) * that.get(i)

        else:
            for i in that.st.keys():
                if i in self.st:
                    summ += self.get(i) * that.get(i)

        return summ

    def dot_list(self, that: [float]) -> float:
        summ = 0.0
        for i in self.st.keys():
            summ += that[i] * self.get(i)

        return summ

    def magnitude(self) -> float:
        return math.sqrt(self.dot_object(self))

    def scale(self, alpha: float):
        """

        :param alpha:
        :type alpha:
        :return:
        :rtype: SparseVector
        """
        c = SparseVector(self.d)
        for i in self.st.keys():
            c.put(i, alpha * self.get(i))

        return c

    def plus(self, that):
        """

        :param that:
        :type that: SparseVector
        :return:
        :rtype: SparseVector
        """
        if self.d != that.d:
            raise IllegalArgumentException("vector lengths are different")

        c = SparseVector(self.d)
        for i in self.st.keys():
            c.put(i, self.get(i))

        for i in that.st.keys():
            c.put(i, that.get(i) + c.get(i))

        return c

    def __str__(self):
        s = ''
        for i in self.st.keys():
            s += "({0}, {1}) ".format(i, self.st.get(i))

        return s


def main():
    a = SparseVector(10)
    b = SparseVector(10)
    a.put(3, 0.50)
    a.put(9, 0.75)
    a.put(6, 0.11)
    a.put(6, 0.00)
    b.put(3, 0.60)
    b.put(4, 0.90)
    c = a.dot_object(b)
    print("type of c is {0}".format(type(c)))
    print("c = {0}".format(c))
    print("a = {0}".format(a.__str__()))
    print("b = {0}".format(b))
    print("a dot b = {0}".format(a.dot_object(b)))
    print("a + b   = {0}".format(a.plus(b)))


if __name__ == '__main__':
    main()
