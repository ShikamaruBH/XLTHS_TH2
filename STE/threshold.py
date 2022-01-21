from os.path import join
from scipy.io.wavfile import read
import numpy as np
import frame
import ste
import ma

FILE_PATH_THHL = 'D:\Documents\XLTHS\Thi TH\TinHieuHuanLuyen-44k'
FILE_WAV_THHL = ['01MDA.wav', '02FVA.wav', '03MAB.wav', '06FTB.wav', '30FTN.wav', '42FQT.wav', '44MTT.wav', '45MDV.wav']
FILE_LAB_THHL = ['01MDA.lab', '02FVA.lab', '03MAB.lab', '06FTB.lab', '30FTN.lab', '42FQT.lab', '44MTT.lab', '45MDV.lab']

INDEX = 0
TIME_FRAME = 0.03

# Đọc dữ liệu
def readFileInput(fileName):
    inputFile = []
    with open(join(FILE_PATH_THHL, fileName)) as file:
        for line in file:
            inputFile.append(line.split())
    for i in range(0, len(inputFile) - 2):
        inputFile[i][0] = int(float(inputFile[i][0]) * frequency / 1323 * 3)
        inputFile[i][1] = int(float(inputFile[i][1]) * frequency / 1323 * 3)
    
    inputFile = inputFile[:-2]
    return inputFile

# Tìm ngưỡng
def calThreshold(fileLab, STEArray):
  f = []
  g = []
  index = 0
  # Chia STE của từng đoạn tiếng nói và khoảng lặng
  for j in range(len(STEArray)):
    if j >= fileLab[index][0] and j < fileLab[index][1]:
      if fileLab[index][2] == 'sil':
        g.append(STEArray[j])
      else:
        f.append(STEArray[j])
    else:
      index += 1
      
  Tmin = min(f)
  Tmax = max(g)
  T = (Tmin + Tmax) / 2
  tempF = tempG = -1
  countF = countG = 0
    
  for value in f:
    countF += 1 if value > T else 0
  for value in g:
    countG += 1 if value < T else 0

  while tempF != countF or tempG != countG:
    avgF = 0
    avgG = 0
    
    for value in f:
      avgF += max(value - T, 0)
    avgF /= len(f)
    for value in g:
      avgG += max(T - value, 0)
    avgG /= len(g)
    
    if (avgF - avgG) > 0:
      Tmin = T
    else:
      Tmax = T
      
    T = (Tmin + Tmax) / 2
    tempF = countF
    tempG = countG
    countF = countG = 0
    
    for value in f:
      countF += 1 if value > T else 0
    for value in g:
      countG += 1 if value < T else 0
      
  return T

# Main
thresholdsSTEArray = np.array([])
thresholdsMAArray = np.array([])

for i in range(0, len(FILE_WAV_THHL)):
  # Đọc dữ liệu của file huấn luyện
  frequency, signal = read(join(FILE_PATH_THHL, FILE_WAV_THHL[i]))  
  signal = signal / max(np.max(signal), abs(np.min(signal)))
  frameLength = int(TIME_FRAME * frequency) # Độ dài của 1 frame (đơn vị mẫu)
  framesArray = frame.getFramesArray(signal, frameLength)
  STEArray = ste.calSTE(framesArray) # Mảng giá trị STE
  MAArray = ma.calMA(framesArray)    # Mảng giá trị MA
  fileLab = readFileInput(FILE_LAB_THHL[i])
  steT = calThreshold(fileLab, STEArray)
  maT = calThreshold(fileLab, MAArray)
  thresholdsSTEArray = np.append(thresholdsSTEArray, steT)
  thresholdsMAArray = np.append(thresholdsMAArray, maT)
  
print(thresholdsSTEArray)
print(thresholdsMAArray)
print(f"Threshold = {np.average(thresholdsSTEArray)}")
print(f"Threshold = {np.average(thresholdsMAArray)}")