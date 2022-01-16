from .env import *
from .frame import frame
from .ma import ma

# inputArray: mảng chứa năng lượng
def findVowels(signal, frequency, threshold):
  frameLength = int(FRAME_LENGHT_IN_SECOND * frequency)
  framesArray = frame.getFramesArray(signal, frameLength)
  MAArray = ma.calMA(framesArray)
  markSpeech = np.zeros(len(MAArray))
  
  # Đánh dấu đoạn tiếng nói
  for i in range(len(MAArray)):
    if MAArray[i] >= threshold:
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
  
  for index in range(0, len(markSpeech)):
    if markSpeech[index] == 1 and index == 0 or markSpeech[index] == 1 and markSpeech[index - 1] == 0:
      firstTime = 2 * FRAME_LENGHT_IN_SECOND * index / 3
      break
  for index in range(0, len(markSpeech)):
    if markSpeech[index] == 0 and markSpeech[index - 1] == 1 or markSpeech[index] == 1 and index == (len(markSpeech) - 1):
      lastTime = 2 * FRAME_LENGHT_IN_SECOND * index / 3
      break
    
  signal = signal[int(firstTime * frequency):int(lastTime * frequency)]
  
  return signal