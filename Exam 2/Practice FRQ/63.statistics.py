import numpy as np

nums = np.linspace(0, 20)

print(np.mean(nums))
print(np.var(nums, ddof=1))
