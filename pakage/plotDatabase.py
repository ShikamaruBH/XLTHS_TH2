import matplotlib.pyplot as plt
import json

from .env import K, np

def plotDatabase():
	DATA = json.load(open('CSDL.json'))

	for vowel in DATA:
		print(f'ploting /{vowel}/')
		plt.figure(f'MFCC vectors of /{vowel}/')

		for i in range(K):
			plt.subplot(int(f'{K}1{i + 1}'))
			plt.plot(DATA[vowel][i])
			plt.tight_layout()
			plt.title(f'Center vector {i + 1}')

	plt.show()
			