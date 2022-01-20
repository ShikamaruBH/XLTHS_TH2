from .env import *
from os.path import join
from scipy.io.wavfile import read
from .identificateVowel import identificateVowel
from .confusionMatrix import confusionMatrix

def resultTable():
  countCorrect = 0
  matrix = np.zeros((5, 5))
  
  print(f'{"":8}N = {N}, K = {K}')
  print(f'{"":7}/a/ /e/ /i/ /o/ /u/')
  for i in range(len(TINHIEUKIEMTHU_NAMES)):
    print(f'{TINHIEUKIEMTHU_NAMES[i]} ', end=' ')
    for j in range(len(VOWELS)):
      frequency, signal = read(join(r'./NguyenAmKiemThu-16k', TINHIEUKIEMTHU_NAMES[i], VOWELS[j] + '.wav'))
      signal = signal / max(np.max(signal), abs(np.min(signal)))
      vowelResult = identificateVowel(signal, frequency)
      matrix[j][VOWELS.index(vowelResult)] += 1
      if vowelResult == VOWELS[j]:
        answer = 'Đ'
        countCorrect += 1
      else:
        answer = 'S'
      print(f' {answer} ', end=' ')
    print()
  print(f'{"ĐCX":12}{round((countCorrect / (len(TINHIEUKIEMTHU_NAMES) * len(VOWELS))) * 100, 3)} %')
  print(f'\n{"":6}Ma tran nham lan')
  confusionMatrix(matrix)