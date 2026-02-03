import numpy as np
#for entering the array
def get_matrix_input(name):
    print(f"\n--- Input Matrix {name} ---")
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    matrix=[]
    print(f"Enter the elements row-wise (separated by space):")
    for i in range(rows*cols):
        elements = int(input())
        matrix.append(elements)

    matrix = np.array(matrix).reshape(rows, cols)
    print(matrix)
    return matrix

#for displaying the menu for showing the operation
def display_menu():
    print("\n" + "="*30)
    print(" MATRIX OPERATIONS TOOL")
    print("="*30)
    print("1. Addition (A + B)")
    print("2. Subtraction (A - B)")
    print("3. Multiplication (A * B)")
    print("4. Transpose (Aᵀ)")
    print("5. Determinant (det(A))")
    print("6. Exit")
    print("="*30)

def main():
    while True:
        display_menu()
        choice = input("Choose an operation (1-6): ")

        if choice == '6':
            print("Shutting down. Happy calculating!")
            break
       #undergoing Operation
        try:
            if choice == '1':
                matrix_a = get_matrix_input("A")
                matrix_b = get_matrix_input("B")
                result = np.add(matrix_a, matrix_b)
                print("\nResult (A + B):\n", result)
            elif choice == '2':
                matrix_a = get_matrix_input("A")
                matrix_b = get_matrix_input("B")
                result = np.subtract(matrix_a, matrix_b)
                print("\nResult (A - B):\n", result)
            elif choice == '3':
                matrix_a = get_matrix_input("A")
                matrix_b = get_matrix_input("B")
                result = np.matmul(matrix_a, matrix_b)
                print("\nResult (A * B):\n", result)
            elif choice == '4':
                matrix_a = get_matrix_input("A")
                print("\nTranspose of A:\n", matrix_a.T)
            elif choice == '5':
                matrix_a = get_matrix_input("A")
                if matrix_a.shape[0] != matrix_a.shape[1]:
                    print("Error: Determinant is only defined for square matrices.")
                else:
                    det = np.linalg.det(matrix_a)
                    print(f"\nDeterminant of A: {det:.2f}")
            else:
                print("Invalid choice, try again.")
        #Error handling 
        except ValueError as e:
            print(f"\nError: {e}. Ensure dimensions and element counts match.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
