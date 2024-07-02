# Multiplication of two matrices

try:
    def display_matrix(mat):
        for a in range(len(mat)):
            print(mat[a])


    def multiplication(mat1, mat2):
        new_matrix = [['_' for _ in range(len(mat1))]for _ in range(len(mat2[0]))]
        for a in range(len(mat1)):
            for b in range(len(mat2[0])):
                sum_of_products = 0
                for c in range(len(mat2)):
                    sum_of_products += mat1[a][c]*mat2[c][b]
                new_matrix[a][b] = sum_of_products
        return new_matrix


# Provide inputs for 1st matrix
    print("Inputs for the 1st matrix-")
    m = int(input("Enter the number of rows for 1st matrix:"))
    n = int(input("Enter the number of columns of 1st matrix:"))
    print(f"Enter {m} rows with each row of {n} elements")
    matrix1 = []
    for i in range(m):
        elements = list(map(int, input(f"Enter {n} elements,row{i + 1}:").split()))
        while len(elements) != n:
            elements = list(map(int, input(f"Again enter row{i+1} with exactly {n} numbers:")))
        matrix1.append(elements)

# Provide inputs for 2nd matrix
    print("Inputs for the 2nd matrix-")
    x = int(input("Enter the number of rows for 2nd matrix:"))
    y = int(input("Enter the number of columns of 2nd matrix:"))
    print(f"Enter {x} rows with each row of {y} elements")
    matrix2 = []
    for i in range(x):
        elements = list(map(int, input(f"Enter {y} elements,row{i + 1}:").split()))
        while len(elements) != y:
            elements = list(map(int, input(f"Again enter row{i+1} with exactly {y} numbers:")))
        matrix2.append(elements)

# Displaying both the matrices entered
    print("Displaying the 1st matrix:")
    display_matrix(matrix1)
    print("Displaying the 2nd matrix:")
    display_matrix(matrix2)

# Checking whether the multiplication is possible or not
    if n == x:
        multiplied_matrix = multiplication(matrix1, matrix2)
        print("Displaying the matrix after multiplication of above 2 matrices:")
        display_matrix(multiplied_matrix)
    else:
        print("Multiplication not possible for the above matrices...")
except:
    print("Something went wrong, please reRun and provide the valid inputs...")