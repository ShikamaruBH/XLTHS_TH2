def getFramesArray(signal, frameLength):
  step = frameLength // 3
  frames = []
  index = 0
  for i in range(0, len(signal) // step + 1):
    temp = signal[index : index + frameLength]
    frames.append(temp)
    index += step
  return frames