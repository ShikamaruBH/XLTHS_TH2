import numpy as np

def calMA(framesArray):
  ma = np.zeros(len(framesArray))
  
  for i in range(len(framesArray)):
    ma[i] = np.sum(abs(framesArray[i]))
  ma = ma / np.max(ma)
  
  return ma