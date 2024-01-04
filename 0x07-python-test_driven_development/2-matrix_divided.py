def matrix_divided(matrix, div):
    """matrix_divided -  divides all elements of a matrix

    Args:
        matrix: a list of lists of integers or floats
        div: number (integer or float)

    Return:
        a new matrix with elements divided by div and rounded to 2 decimal places
    """

    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

        for each_int in matrix[i]:
            if not isinstance(each_int, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

        if i < len(matrix) - 1 and len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = round(element / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix

