from pakage import *
from os.path import join
from scipy.io.wavfile import read

if __name__ == '__main__':
  for i in range(len(TINHIEUHUANLUYEN_NAMES)):
    for j in range(len(VOWELS)):
      frequency, signal = read(join(r'.\NguyenAmHuanLuyen-16k', TINHIEUHUANLUYEN_NAMES[i], VOWELS[j] + '.wav'))
      signal = signal / max(np.max(signal), abs(np.min(signal)))
      print(identificateVowel(signal, frequency))