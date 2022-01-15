
def confusionMatrix(CONFUSION_MATRIX):
	vowels = 'aeiou'
	print(f'{"":5}{"/a/":^5}{"/e/":^5}{"/i/":^5}{"/o/":^5}{"/u/":^5}')
	for i in range(5):
		print('{:<5}{:^5.0f}{:^5.0f}{:^5.0f}{:^5.0f}{:^5.0f}'.format(vowels[i], *CONFUSION_MATRIX[i]))
	print()