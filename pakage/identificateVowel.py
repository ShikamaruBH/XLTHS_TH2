from .env import *

import math
import json
from .findVowels import findVowels
from .getMFCCVectors import getMFCCVectors
import matplotlib.pyplot as plt

def distanceVectors(vector1, vector2):
  return math.sqrt(np.sum((vector1 - vector2) ** 2))

def identificateVowel(signal, Fs):
  DATA = json.load(open('CSDL.json'))
  vowel = findVowels(signal, Fs)

  # plt.subplot(2, 1, 1)
  # plt.plot(signal)
  # plt.subplot(2, 1, 2)
  # plt.plot(vowel)
  # plt.show()

  MFCCVectors = getMFCCVectors(vowel, Fs)
  averageVector = sum(MFCCVectors) / len(MFCCVectors)
  
  vowelResult = ''
  minDistance = 1e18
  for vowel in DATA:
    for vector in DATA[vowel]:
      distance = distanceVectors(averageVector, vector)
      if minDistance > distance:
        vowelResult = vowel
        minDistance = distance
  return vowelResult