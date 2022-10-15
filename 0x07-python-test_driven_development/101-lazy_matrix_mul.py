#!/usr/bin/python3
""" This module contains a function that mulitplies two matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
    m_a (list of list of int/floats): The first matrix
    m_b (list of list of ints/floats): The second matrix
    """
    return (np.matmul(m_a, m_b))
