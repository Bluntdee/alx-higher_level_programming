#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = [[0 for _ in row] for row in matrix]
    # Iterate through each element in the input matrix, compute the square, and update the new matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix
