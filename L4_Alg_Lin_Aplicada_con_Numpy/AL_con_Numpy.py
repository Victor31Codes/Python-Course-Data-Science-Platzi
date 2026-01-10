import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
suma = A + B
producto = A * B
print("Suma de Matrices:\n", suma)  # Matrix addition
print("Producto de Matrices:\n", producto)  # Element-wise matrix multiplication
dot_product = np.dot(A, B)
print("Producto Punto de Matrices:\n", dot_product)  # Matrix dot product

transpuesta = A.T
print("Transpuesta de A:\n", transpuesta)  # Transpose of matrix A

determinante = np.linalg.det(A)
print("Determinante de A:", determinante)  # Determinant of matrix A

inversa = np.linalg.inv(A)
print("Inversa de A:\n", inversa)  # Inverse of matrix A

valores_propios, vectores_propios = np.linalg.eig(A)
print("Valores propios de A:\n", valores_propios)
print("Vectores propios de A:\n", vectores_propios)  # Eigenvalues and eigenvectors of matrix A
solucion = np.linalg.solve(A, B)
print("Solución de Ax = B:\n", solucion)  # Solving the linear equation Ax = B


