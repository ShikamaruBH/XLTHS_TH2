import numpy as np

# Hàm tính STE
def calSTE(framesArray):
  ste = np.zeros(len(framesArray))
  
  for i in range(len(framesArray)):
    ste[i] = np.sum(framesArray[i]**2)
  ste = ste / np.max(ste)
  
  return ste