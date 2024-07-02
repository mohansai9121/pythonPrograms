# Program to print the transpose of a matrix
print("Provide the inputs of matrix, that you want to transpose")
m = int(input("Enter number of rows in the matrix:"))
n = int(input("Enter number of columns in the matrix:"))


def display_matrix(mat):
    for a in range(len(mat)):
        print(mat[a])


def transpose(mat):
    new_matrix = [['-' for a in range(len(mat))] for b in range(len(mat[0]))]
    for a in range(len(new_matrix)):
        for b in range(len(new_matrix[0])):
            new_matrix[a][b] = mat[b][a]
    return new_matrix


try:
    matrix = []
    for i in range(m):
        elements = list(map(int, input(f"Enter {n} elements, Row{i + 1}:").split()))
        while len(elements) != n:
            elements = list(map(int, input(f"Again enter row{i} with exactly {n} space separated values:")))
        matrix.append(elements)
    print("Printing the matrix:")
    display_matrix(matrix)
    print("Transpose of the matrix is:")
    display_matrix(transpose(matrix))
except:
    print("Something went wrong, Provide valid inputs...")
