from .env import *

import math
import json
from .findVowels import findVowels
from .getMFCCVectors import getMFCCVectors

def distanceVectors(vector1, vector2):
  return math.sqrt(np.sum((vector1 - vector2) ** 2))

def identificateVowel(signal, Fs):
  DATA = json.load(open('CSDL.json'))
  vowel = findVowels(signal, Fs)
  MFCCVectors = getMFCCVectors(vowel, Fs, N)
  averageVector = sum(MFCCVectors) / len(MFCCVectors)
  
  vowelResult = 'a'
  minDistance = distanceVectors(averageVector, DATA['a'][0])
  for vowel in DATA:
    for vector in DATA[vowel]:
      distance = distanceVectors(averageVector, vector)
      if minDistance > distance:
        vowelResult = vowel
        minDistance = distance
  return vowelResult