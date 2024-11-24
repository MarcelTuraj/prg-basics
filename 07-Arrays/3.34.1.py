def identity_matrix(n):
    # Initialize an empty list for the matrix
    matrix_row_struct = []
    
    for i in range(n):
        # Create a new row initialized to all zeros
        subarray = [0] * n  # or you can use: subarray = [0] * n
        subarray[i] = 1  # Set the diagonal element to 1
        matrix_row_struct.append(subarray)  # Append the new row to the matrix
    
    return matrix_row_struct

# Example usage:
n = 4
result = identity_matrix(n)
for row in result:
    print(row)
