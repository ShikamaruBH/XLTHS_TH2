from .env import *

import math
import json
from .findVowels import findVowels
from .getMFCCVectors import getMFCCVectors
from .createDatabase import createDatabase

DATA = createDatabase()

def distanceVectors(vector1, vector2):
  return math.sqrt(np.sum((vector1 - vector2) ** 2))

def identificateVowel(signal, Fs):
  # DATA = json.load(open('CSDL.json'))
  vowel = findVowels(signal, Fs)
  MFCCVectors = getMFCCVectors(vowel, Fs)
  averageVector = sum(MFCCVectors) / len(MFCCVectors)

  vowelResult = 'a'
  minDistance = distanceVectors(averageVector, DATA['a'][0])
  for vowel in DATA:
    for vector in DATA[vowel]:
      # print(vowel, end=' ')
      distance = distanceVectors(averageVector, vector)
      # print(distance)
      if minDistance > distance:
        vowelResult = vowel
        minDistance = distance
  # print(minDistance)
  return vowelResult