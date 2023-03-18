Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.

#### Algorithm

One possible algorithm to rotate an n x n 2D matrix 90 degrees clockwise in-place is:

    Transpose the matrix by swapping each element at position (i,j) with the element at position (j,i). This step reflects the matrix along its diagonal.
    Reverse each row of the transposed matrix. This step flips each row horizontally.