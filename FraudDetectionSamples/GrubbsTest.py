#install pip outlier_utils 
import numpy as np
from OUTLIERS import smirnov_grubbs as grubbs

#Some Array
data = np.array([1,2,3,4,5,6,4,3,2,3,4,2,3,4,0,2,48,4,5,6,5,4,3,3,4,5,6,7,6,5,4,3,2,3,4,3,2,3,2,3,2,32,3,2,3,4,5,4,1,2,3,7,9,100])

output = grubbs.test(data, alpha=.05)

print("Origional Data Shape: ", data.size)
print("After Grubbs Test: ", output.size)
print("Grubbs Test Removed: ", data.size - output.size, " elements")