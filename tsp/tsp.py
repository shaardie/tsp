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

    def get_weight(self, path):
        """Get the weight of the given path.

        :param path: Path to calculate weight for
        :type path: list
        :return: weight of the tour
        :rtype: float
        """
        path_length = len(path)
        weigth = 0
        for i in range(path_length):
            weigth += self.matrix[i, (i+1) % path_length]
        return weigth
