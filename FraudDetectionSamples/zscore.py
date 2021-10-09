import pandas
import numpy as np
import scipy.stats as stats

data = np.array([1,2,3,4,5,6,4,3,2,3,4,2,3,4,0,2,48,4,5,6,5,4,3,3,4,5,6,7,6,5,4,3,2,3,4,3,2,3,2,3,2,32,3,2,3,4,5,4,1,2,3,7,9,100])

print(stats.zscore(data))
