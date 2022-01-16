from os.path import join
from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
import frame
import ste
import ma
import distinguishVowersAndSilences as findVowels

FILE_PATH_THHL = 'D:\Documents\XLTHS\Thi TH\TinHieuHuanLuyen-44k'
FILE_WAV_THHL = ['01MDA.wav', '02FVA.wav', '03MAB.wav', '06FTB.wav', '30FTN.wav', '42FQT.wav', '44MTT.wav', '45MDV.wav']
FILE_LAB_THHL = ['01MDA.lab', '02FVA.lab', '03MAB.lab', '06FTB.lab', '30FTN.lab', '42FQT.lab', '44MTT.lab', '45MDV.lab']

LINE = [[0.45, 0.81, 1.53, 1.85, 2.69, 2.80, 3.78, 4.15, 4.84, 5.14], 
        [0.83, 1.37, 2.09, 2.60, 3.57, 4.00, 4.76, 5.33, 6.18, 6.68], 
        [1.03, 1.42, 2.46, 2.80, 4.21, 4.52, 6.81, 7.14, 8.22, 8.50], 
        [1.52, 1.92, 3.91, 4.35, 6.18, 6.60, 8.67, 9.14, 10.94, 11.33],
        [0.59, 0.97, 1.76, 2.11, 3.44, 3.77, 4.70, 5.13, 5.96, 6.28],
        [0.46, 0.99, 1.56, 2.13, 2.51, 2.93, 3.79, 4.38, 4.77, 5.22],
        [0.93, 1.42, 2.59, 3.00, 4.71, 5.11, 6.26, 6.66, 8.04, 8.39],
        [0.88, 1.34, 2.35, 2.82, 3.76, 4.13, 5.04, 5.50, 6.41, 6.79]]

INDEX = 0
TIME_FRAME = 0.03

# Main
for i in range(0, len(FILE_WAV_THHL)):
  # Đọc dữ liệu đầu vào
  frequency, signal = read(join(FILE_PATH_THHL, FILE_WAV_THHL[i]))
  signal = signal / max(np.max(signal), abs(np.min(signal)))
  frameLength = int(TIME_FRAME * frequency) # Độ dài của 1 frame (đơn vị mẫu)
  framesArray = frame.getFramesArray(signal, frameLength)
  STEArray = ste.calSTE(framesArray)
  MAArray = ma.calMA(framesArray)
  markPointSTE = findVowels.distinguishVowersAndSilences(STEArray, 0.06827)
  markPointMA = findVowels.distinguishVowersAndSilences(MAArray, 0.11918)
  
  # Tín hiệu trên miền thời gian
  timeSample = np.zeros(len(signal))
  for index in range(len(signal)):
    timeSample[index] = index / frequency
  
  timeSampleSTE = np.zeros(len(STEArray))
  for index in range(len(STEArray)):
    timeSampleSTE[index] = 2 * TIME_FRAME * index / 3
  
  # Show
  findLineSTE = np.array([])
  findLineMA = np.array([])
  
  plt.figure(i + 1)
  plt.subplot(2, 1, 1)
  plt.title(f"Signal: {FILE_WAV_THHL[i]}")
  print(f"STE: {FILE_WAV_THHL[i]}")
  plt.plot(timeSample, signal)
  plt.plot(timeSampleSTE, STEArray, 'r')
  plt.axhline(y=0.04772, color='orange', linestyle='-')
  
  for line in LINE[i]:
    plt.axvline(line, color = 'g')
  for index in range(1, len(markPointSTE)):
    if markPointSTE[index] == 1 and markPointSTE[index - 1] == 0 or markPointSTE[index] == 0 and markPointSTE[index - 1] == 1:
      plt.axvline(x = 2 * TIME_FRAME * index / 3, color = 'b', linestyle = 'dashed')
      findLineSTE = np.append(findLineSTE, 2 * TIME_FRAME * index / 3)
  print(findLineSTE)
  
  plt.legend(['Signal', 'STE', 'Threshold'])
  plt.xlabel('Time(s)')
  plt.ylabel('Signal Amplitude')
  
  plt.subplot(2, 1, 2)
  plt.title(f"Signal: {FILE_WAV_THHL[i]}")
  print(f"MA: {FILE_WAV_THHL[i]}")
  plt.plot(timeSample, signal)
  plt.plot(timeSampleSTE, MAArray, 'r')
  plt.axhline(y=0.04772, color='orange', linestyle='-')
  
  for line in LINE[i]:
    plt.axvline(line, color = 'g')
  for index in range(1, len(markPointMA)):
    if markPointMA[index] == 1 and markPointMA[index - 1] == 0 or markPointMA[index] == 0 and markPointMA[index - 1] == 1:
      plt.axvline(x = 2 * TIME_FRAME * index / 3, color = 'b', linestyle = 'dashed')
      findLineMA = np.append(findLineMA, 2 * TIME_FRAME * index / 3)
  print(findLineMA)
  print(LINE[i])
  
  plt.legend(['Signal', 'STE', 'Threshold'])
  plt.xlabel('Time(s)')
  plt.ylabel('Signal Amplitude')
  plt.tight_layout()
plt.show()