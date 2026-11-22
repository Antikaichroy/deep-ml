def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    import numpy as np
    dim_a = np.array(a).shape
    dim_b = np.array(b).shape
    if dim_a[-1]==dim_b[0]:
        return np.dot(np.array(a),np.array(b))
    return -1