"""
Bucket class to conduct frequency analysis on polyalphabetic cipher
with a fixed key length(vigeneres)

"""
import string
class Bucket:
	#initialize the bucket with a frequency map for each letter occurrence in the bucket
	def __init__(self, value):
		self.value = value;
		alphabet = list(string.ascii_uppercase)
		initKeys = [0] * 26
		self.frequencyMap = dict(zip(alphabet,initKeys))
		self.letCount = 0
	#return the bucket value i.e. its position in the fixed length key
	def getValue(self):
		return self.value
	#return the bucket's frequency map 
	def printMap(self):
		
		print( "Bucket ", str(self.value), " frequency analysis: ")

		for key in self.frequencyMap:
			print(key, self.frequencyMap[key], "\tP: ", round(self.frequencyMap[key] / self.letCount, 4))

	#increment a letter occurrence in the bucket
	def incMap(self, letter):
		self.frequencyMap[letter] = self.frequencyMap.get(letter) + 1
		self.letCount += 1


