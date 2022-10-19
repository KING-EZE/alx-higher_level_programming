#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices
    Args:
    m_a (list of lists of int/float): matrix to be multipled
    m_b (list of lists of int/float): matrix to be multplied
    Raises:
    TypeError: if m_a or m_b is not a list
    TypeError: if m_a or m_b is not a list of lists
    TypeError: if row of m_a or m_b are not the same size
    TypeError: if one element of list of lists is not int/float
    ValueError: if m_a or m_b is empty
    ValueError: if m_a or m_b cannot be multiplied
    Returns:
    A new list which is the outcome of the mulitplication
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a cannot be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b cannot be empty")

    if not all(isinstance(element, int) or isinstance(element, float))
    for element in [number for row in m_a for number in row]:
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(element, int) or isinstance(element, float))
    for element in [number for row in m_b for number in row]:
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b cannot be multiplied")

    matrix2 = []
    for row in m_a:
        my_row = []
        for column in matrix1:
            product = 0
            for m in range(len(matrix1[0])):
                product += row[m] * column[m]
                my_row.append(product)
                matrix2.append(my_row)

                return matrix2
