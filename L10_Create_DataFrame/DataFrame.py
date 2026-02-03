import numpy as np
import pandas as pd

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dt_from_array = pd.DataFrame(data, columns=['A', 'B', 'C'])
print("DataFrame from NumPy array:\n", dt_from_array)