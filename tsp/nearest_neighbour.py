import numpy


def nearest_neighbour(matrix, start=0):
    """Solve the TSP with the nearest neighbour algorithm.
    The algorithm will work on the incoming matrix.

    For details take a look at
    https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm

    :param matrix: Matrix describing the TSP.
    :type matrix: numpy.ndarray
    :param start: Vertex to start with, defaults to 0
    :type start: int, optional
    :return: Ordered list of visited vertices
    :rtype: list
    """
    path = [start]
    while len(matrix) != len(path):
        matrix[:, start] = numpy.inf
        start = numpy.argmin(matrix[start])
        path.append(start)
    return path
