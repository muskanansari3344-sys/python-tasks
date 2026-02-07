import numpy as np

print("=== MATRIX OPERATIONS TOOL ===")

# -------- Matrix A --------
rowsA = int(input("Matrix A - number of rows: "))
colsA = int(input("Matrix A - number of columns: "))

print("Enter elements of Matrix A row-wise:")
A = []
for i in range(rowsA):
 A.append(list(map(int, input().split())))

A = np.array(A)

# -------- Matrix B --------
rowsB = int(input("Matrix B - numbers of rows: "))
colsB = int(input("Matrix B - number of columns: "))

print("Enter elements of Matrix B row-wise:")
B = []
for i in range(rowsB):
    B.append(list(map(int, input().split())))

B = np.array(B)

print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)

# -------- Menu --------
print("""
Choose Operation:
1. Addition
2. Subtraction
3. Multiplication
4. Transpose of Matrix A
5. Determinant of Matrix A
""")

choice = int(input("Enter your choice (1-5): "))

# -------- Operations --------
if choice == 1:
    print("Result (A + B):\n", A + B)

elif choice == 2:
    print("Result (A - B):\n", A - B)

elif choice == 3:
    print("Result (A x B):\n", np.dot(A, B))

elif choice == 4:
    print("Transpose of Matrix A:\n", A.T)

elif choice == 5:
    print("Determinant of Matrix A:\n", np.linalg.det(A))

else:
    print("Invalid choice")




