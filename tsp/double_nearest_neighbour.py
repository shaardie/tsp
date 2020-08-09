import numpy


def double_nearest_neighbour(matrix, start=0):
    """Solve the TSP with the double nearest neighbour algorithm.
    The algorithm will work on the incoming matrix.

    :param matrix: Matrix describing the TSP.
    :type matrix: numpy.ndarray
    :param start: Vertex to start with, defaults to 0
    :type start: int, optional
    :return: Ordered list of visited vertices
    :rtype: list
    """
    # Init
    path = [start]
    matrix[:, start] = numpy.inf

    while len(matrix) != len(path):
        # First next element can simply be appended.
        if len(path) == 1:
            start = numpy.argmin(matrix[start])
            matrix[:, start] = numpy.inf
            path.append(start)
            continue

        # Find minimum at the end and the beginning of the path.
        c1 = numpy.argmin(matrix[path[0]])
        c2 = numpy.argmin(matrix[path[-1]])

        # Get values of the new part.
        v1 = matrix[path[0], c1]
        v2 = matrix[path[-1], c2]

        # Compare values of the new parts and
        # insert the smaller one at the end or the beginning.
        if v1 < v2:
            path.insert(0, c1)
            matrix[:, c1] = numpy.inf
            continue
        path.append(c2)
        matrix[:, c2] = numpy.inf
        start = c2

    return path
