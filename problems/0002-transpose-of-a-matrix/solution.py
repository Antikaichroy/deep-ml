def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    # import numpy as np 
    # a = np.array(a)
    # return a.T
    
    # transposed = []
    # for i in range(len(a[0])):
    #     to_add = []
    #     for j in range(len(a)):
    #         to_add.append(a[j][i])

    #     transposed.append(to_add)
    transposed = [list(elements) for elements in zip(*a)]

    return transposed
            