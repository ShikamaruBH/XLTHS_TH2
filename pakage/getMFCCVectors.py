from .env import *
from librosa.feature import mfcc

def getMFCCVectors(vowel_part, Fs, N):
	vowel_part = vowel_part[int(vowel_part.size / 3):int(vowel_part.size * 2 / 3)]
	l = []
	for i in range(0, int(vowel_part.size * Fs), int(FRAME_SHIFT_IN_SECOND * Fs)):
		if vowel_part[i:i + int(FRAME_LENGHT_IN_SECOND * Fs)].size == int(FRAME_LENGHT_IN_SECOND * Fs):
			temp = mfcc(vowel_part[i:i + int(FRAME_LENGHT_IN_SECOND * Fs)], Fs, n_mfcc=N, n_fft=int(FRAME_LENGHT_IN_SECOND * Fs))
			l.append(temp.T[0])
	return l
