import numpy as np

def matrix_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    This function return the result of two multiplied matrixes 
    
    Args:
        a (np.ndarray): A numpy array
        b (np.ndarray): A numpy array
    Returns:
        np.ndarray: The result of a multipliud by b
    """
    if len(a[0]) == len(b):
        return a @ b
    return []

print(matrix_multiply.__doc__)

a = np.array(10)
# a = np.arange(6).reshape(3, 2)
b = np.arange(12).reshape(3, 4)
