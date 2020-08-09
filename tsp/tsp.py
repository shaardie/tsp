import numpy


class TSP:
    def __init__(self, matrix):
        self.matrix = matrix

    @staticmethod
    def load(filename):
        """Load a TSP from a file.

        :param filename: Name of the file
        :type filename: str
        :return: Traveling Salesman Problem
        :rtype: TSP
        """
        return TSP(numpy.loadtxt(filename, delimiter=","))

    def save(self, filename):
        """Save the TSP to a file.

        :param filename: Name of the file.
        :type filename: str
        """
        numpy.savetxt(filename, self.matrix, delimiter=",")

    def nearest_neighbor(self, start=0):
        """Solve the TSP with the nearest neighbour algorithm.

        For details take a look at
        https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm

        :param start: Vertex to start with, defaults to 0
        :type start: int, optional
        :return: Ordered list of visited vertices
        :rtype: list
        """
        path = []
        while len(self.matrix) != len(path):
            path.append(start)
            self.matrix[:, start] = numpy.inf
            start = numpy.argmin(self.matrix[start])

        return path
