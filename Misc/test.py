
import numpy as np

arr = np.arange(10).reshape(2, 5)

arr[0][1] = 100

print(arr)