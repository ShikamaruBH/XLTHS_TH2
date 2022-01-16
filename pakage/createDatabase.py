from .env import *

from librosa import load
from sklearn.cluster import KMeans
import json

from .findVowels import findVowels
from .getMFCCVectors import getMFCCVectors

def createDatabase():
	path = './NguyenAmHuanLuyen-16k'
	VECTORS_DATA = {'a': [], 'e': [], 'i': [], 'o': [], 'u': []}
	VECTORS_RESULT = {'a': [], 'e': [], 'i': [], 'o': [], 'u': []}

	for name in TINHIEUHUANLUYEN_NAMES:
		print(f'Find vowel of {name}')
		for vowel in VOWELS:
			signal, Fs = load(f'{path}/{name}/{vowel}.wav', sr=None)
			vowel_part = findVowels(signal, Fs)
			MFCCVectors = getMFCCVectors(vowel_part, Fs, N)
			VECTORS_DATA[vowel] += (MFCCVectors)

	for vowel in VECTORS_DATA:
		print(f'Calculating {vowel} vectors')
		VECTORS_RESULT[vowel] = list(KMeans(K).fit(np.array(VECTORS_DATA[vowel])).cluster_centers_[0].astype(float))

	print(VECTORS_RESULT)

	json.dump(VECTORS_RESULT, open('CSDL.json', 'w'))