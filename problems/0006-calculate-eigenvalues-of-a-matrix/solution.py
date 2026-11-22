def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    # eigen values are calculated using the characteristic equation
    import numpy as np
    matrix = np.array(matrix)
    trace = np.trace(matrix)
    det_matrix = np.linalg.det(matrix)

    sol1 = (trace + np.sqrt(trace**2-4*det_matrix))/2
    sol2 = (trace - np.sqrt(trace**2-4*det_matrix))/2
    return [sol1, sol2]