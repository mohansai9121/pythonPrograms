# program for adding two matrices
m = int(input("Enter number of rows of matrix:"))
n = int(input("Enter number of columns of matrix:"))


def display_matrix(mat):
    for a in range(m):
        print(mat[a])


def subtraction(mat1, mat2):
    new_matrix = [['_' for a in range(n)]for b in range(m)]
    for a in range(m):
        for b in range(n):
            new_matrix[a][b] = mat1[a][b]-mat2[a][b]
    return new_matrix


# Enter 1st matrix
print(f"Enter {m} rows with {n} elements in each row for matrix1")
matrix1 = []
for i in range(m):
    row = list(map(int, input(f'Enter {n} elements(space separated) row {i+1}:').split()))
    while len(row) != n:
        row = list(map(int, input(f'Enter row {i + 1} again with {n} elements:').split()))
    matrix1.append(row)

# Enter 2nd matrix
print(f"Enter {m} rows with {n} elements in each row for matrix2")
matrix2 = []
for i in range(m):
    row = list(map(int, input(f'Enter {n} elements(space separated) row {i+1}:').split()))
    while len(row) != n:
        row = list(map(int, input(f'Enter row {i + 1} again with {n} elements:').split()))
    matrix2.append(row)

# printing both the matrices
print("Displaying 1st matrix:")
display_matrix(matrix1)
print("Displaying 2nd matrix:")
display_matrix(matrix2)

# Subtracting Matrix2 from Matrix1
print("Displaying the matrix after addition:")
display_matrix(subtraction(matrix1, matrix2))
