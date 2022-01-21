from .env import K, np, VOWELS
from .createDatabase import createDatabase

import matplotlib.pyplot as plt

def plotDatabase():
	DATA = createDatabase()
	plt.figure('First vectors of 5 vowels')
	for vowel in DATA:
		plt.plot(DATA[vowel][0])
	plt.legend(list(VOWELS))

	for vowel in DATA:
		print(f'ploting /{vowel}/')
		plt.figure(f'MFCC vectors of /{vowel}/')

		for i in range(K):
			plt.plot(DATA[vowel][i])

		plt.title(f'{K} vectors of {vowel}')
		plt.tight_layout()
	plt.show()
			