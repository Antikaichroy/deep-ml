import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    current_shape = np.array(a).shape
    import math 
    prod_current = math.prod(current_shape)
    prod_new = math.prod(new_shape)
    if prod_current != prod_new:
        return []
    reshaped_matrix = np.reshape(np.array(a), new_shape)
    return reshaped_matrix