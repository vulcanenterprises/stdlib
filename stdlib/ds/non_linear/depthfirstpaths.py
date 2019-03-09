"""
depthfirstpaths.py
=========================================================
The depthfirstpaths.py module for python stdlib
"""
from typing import Iterable

from stdlib.ds.non_linear import Graph
from stdlib.ds.linear import Stack


class DepthFirstPaths(object):
    def __init__(self, G: Graph, s: int):
        self._marked = [False for i in range(G.V)]
        self._edge_to = [0 for i in range(G.V)]
        self._s = s
        self.__validate_vertex(s)
        self.__dfs(G, s)

    def __dfs(self, G: Graph, v: int):
        self._marked[v] = True
        for w in G.adj(v):
            if not self._marked[w]:
                self._edge_to[w] = v
                self.__dfs(G, w)

    def has_path_to(self, v: int) -> bool:
        self.__validate_vertex(v)
        return self._marked[v]

    def path_to(self, v: int) -> Iterable or None:
        self.__validate_vertex(v)
        if not self.has_path_to(v):
            return None
        path = Stack()
        x = v
        while x != self._s:
            path.push(x)
            x = self._edge_to[x]

        path.push(self._s)
        return path

    def __validate_vertex(self, v: int) -> None:
        V = len(self._marked)
        if v < 0 or v >= V:
            raise ValueError("vertex {0} is not between 0 and {1}".format(v, V - 1))


def main():
    import os
    from stdlib.utils.inn import In
    dirpath = os.getcwd()
    inn = In('{0}/tests/tinyDG.txt'.format(dirpath))
    s = 0
    g = Graph(inn=inn)
    dfs = DepthFirstPaths(g, s)
    string = ''
    for v in range(g.V):
        if dfs.has_path_to(v):
            string += '{0} to {1}: '.format(s, v)
            for x in dfs.path_to(v):
                if x == s:
                    string += x.__str__()
                else:
                    string += "-{0}".format(x)

            string += '\n'

        else:
            string += "{0} to {1}:  not connected\n".format(s, v)

    print(string)


if __name__ == '__main__':
    main()
