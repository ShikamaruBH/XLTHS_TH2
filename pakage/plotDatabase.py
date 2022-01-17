import matplotlib.pyplot as plt
from librosa.display import specshow
import json

from .env import K, np

def plotDatabase():
	DATA = json.load(open('CSDL.json'))

	for vowel in DATA:
		print(f'ploting /{vowel}/')
		plt.figure(f'MFCC vectors of /{vowel}/')

		for i in range(K):
			plt.subplot(int(f'1{K}{i + 1}'))
			specshow(np.array(DATA[vowel]))
			plt.colorbar()
			plt.title(f'MFCC vector {i + 1}')

	plt.show()
			