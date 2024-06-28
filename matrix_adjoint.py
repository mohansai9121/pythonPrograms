# Program to find adjoint of matrix and also determinant
import math
print("Enter the inputs for a square matrix")
m = int(input("Enter the number of rows/columns for square matrix:"))


def display_matrix(mat):
    for a in mat:
        print(a)


def matrix_except_row_column(mat, x, y):
    new_matrix_elements = []
    for a in range(len(mat)):
        for b in range(len(mat)):
            if a == x or b == y:
                continue
            else:
                new_matrix_elements.append(mat[a][b])
    return listing(new_matrix_elements)


def transpose(mat):
    new_mat = [['-' for _ in range(m)] for _ in range(m)]
    for a in range(m):
        for b in range(m):
            new_mat[a][b] = pow(-1, a+b)*mat[b][a]
    return new_mat


def determinant(mat):
    sum1 = 0
    if len(mat) == 1:
        return mat[0]
    elif len(mat) == 2:
        return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    else:
        for a in range(len(mat)):
            sum1 += pow(-1, a)*mat[0][a]*determinant(matrix_except_row_column(mat, 0, a))
        return sum1


def listing(mat):
    n = int(math.sqrt(len(mat)))
    new_mat = []
    for a in range(0, n):
        new_mat.append(mat[a*n:a*n+n])
    return new_mat


def cofactor(mat):
    if m == 1:
        return mat
    elif m == 2:
        temp = mat[0][0]
        mat[0][0] = mat[1][1]
        mat[0][1] = -1*mat[0][1]
        mat[1][0] = -1*mat[1][0]
        mat[1][1] = temp
        return mat
    else:
        new_mat = [['-' for _ in range(m)]for _ in range(m)]
        for a in range(m):
            for b in range(m):
                trimmed_matrix = matrix_except_row_column(mat, a, b)
                new_mat[a][b] = determinant(trimmed_matrix)
    return new_mat


matrix = []
for i in range(m):
    elements = list(map(int, input(f"Enter {m} elements, Row{i+1}:").split()))
    if len(elements) != m:
        elements = list(map(int, input(f"Again enter row{i+1} with exactly {m} values:")))
    matrix.append(elements)
matrix = transpose(cofactor(matrix))
print("Adjoint matrix is:")
display_matrix(matrix)
print("Determinant of the matrix:")
print(determinant(matrix))

