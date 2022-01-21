import numpy as np

# Phân biệt đoạn tiếng nói và đoạn khoảng lặng
def distinguishVowersAndSilences(inputArray, threshold = 0.11918):
  markSpeech = np.zeros(len(inputArray))
  # Đánh dấu đoạn tiếng nói
  for i in range(len(inputArray)):
    if inputArray[i] >= threshold:
      markSpeech[i] = 1
  
  # Kiểm tra khoảng lặng > 300ms
  countZero = 1
  firstPosition = 0
  for i in range(1, len(markSpeech)):
    if markSpeech[i] == 0 and markSpeech[i - 1] == 0:
      countZero += 1
    elif markSpeech[i] == 1 and markSpeech[i - 1] == 0:
      if countZero < 15:
        for j in range(firstPosition, i):
          markSpeech[j] = 1
      countZero = 1
    elif markSpeech[i] == 0 and markSpeech[i - 1] == 1:
      firstPosition = i
  
  return markSpeech