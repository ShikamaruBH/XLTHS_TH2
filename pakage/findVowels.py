from .env import *
from . import frame
from . import ste
import matplotlib.pyplot as plt

# inputArray: mảng chứa năng lượng
def findVowels(signal, frequency):
  signal = signal / max(np.max(signal), abs(np.min(signal)))
  frameLength = int(FRAME_LENGHT_IN_SECOND * frequency)
  framesArray = frame.getFramesArray(signal, frameLength)
  STEArray = ste.calSTE(framesArray)
  markSpeech = np.zeros(len(STEArray))
  
  # Đánh dấu đoạn tiếng nói
  for i in range(len(STEArray)):
    if STEArray[i] >= THRESHOLD:
      markSpeech[i] = 1
  
  # Kiểm tra khoảng lặng > 300ms
  countZero = 1
  firstPosition = 0
  maxZero = 0.3 // FRAME_SHIFT_IN_SECOND
  for i in range(1, len(markSpeech)):
    if markSpeech[i] == 0 and markSpeech[i - 1] == 0:
      countZero += 1
    elif markSpeech[i] == 1 and markSpeech[i - 1] == 0:
      if countZero < maxZero and firstPosition != 0:
        for j in range(firstPosition, i):
          markSpeech[j] = 1
      countZero = 1
    elif markSpeech[i] == 0 and markSpeech[i - 1] == 1:
      firstPosition = i
  
  firstTime = 0
  lastTime = len(signal) / frequency
  lengthOfVowel = 0
  firstTemp = 0
  lastTemp = len(signal) / frequency
  countOne = 0
  
  for index in range(len(markSpeech)):
    if markSpeech[index] == 1:
      countOne += 1
      if markSpeech[index - 1] == 0:
        firstTemp = FRAME_LENGHT_IN_SECOND * index / 3
    else:
      if markSpeech[index - 1] == 1:
        lastTemp = FRAME_LENGHT_IN_SECOND * index / 3
        if countOne > lengthOfVowel:
          lengthOfVowel = countOne
          firstTime = firstTemp
          lastTime = lastTemp
  
  # # Tín hiệu trên miền thời gian
  # timeSample = np.zeros(len(signal))
  # for index in range(len(signal)):
  #   timeSample[index] = index / frequency
  
  # timeSampleSTE = np.zeros(len(STEArray))
  # for index in range(len(STEArray)):
  #   timeSampleSTE[index] = FRAME_LENGHT_IN_SECOND * index / 3
  # plt.plot(timeSample, signal)
  # plt.plot(timeSampleSTE, STEArray, 'r')
  # plt.axvline(x = firstTime, color = 'g')
  # plt.axvline(x = lastTime, color = 'g')
  # plt.show()

  signal = signal[int(firstTime * frequency):int(lastTime * frequency)]
  
  return signal