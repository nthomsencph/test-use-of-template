""" This module contains the main function. """

from typing import List

def transpose(matrix : List = None) -> List:
    """ Transpose a matrix.

    Args:
        matrix (List, optional): _description_. Defaults to None.

    Returns:
        List: _description_
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]