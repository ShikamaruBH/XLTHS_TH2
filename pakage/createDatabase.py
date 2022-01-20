from .env import *

from librosa import load
from sklearn.cluster import KMeans
import json

from .findVowels import findVowels
from .getMFCCVectors import getMFCCVectors

def createDatabase():
	path = './NguyenAmHuanLuyen-16k'
	DATA = {'a': [], 'e': [], 'i': [], 'o': [], 'u': []}

	for name in TINHIEUHUANLUYEN_NAMES:
		print(f'Find vowel of {name}')
		for vowel in VOWELS:
			signal, Fs = load(f'{path}/{name}/{vowel}.wav', sr=None)
			vowel_part = findVowels(signal, Fs)
			MFCCVectors = getMFCCVectors(vowel_part, Fs)
			DATA[vowel] += (MFCCVectors)

	for vowel in DATA:
		print(f'Calculating {vowel} vectors')

		cluster_centers = KMeans(K).fit(np.array(DATA[vowel])).cluster_centers_

		DATA[vowel] = [list(center.astype(float)) for center in cluster_centers]

	json.dump(DATA, open('CSDL.json', 'w'))