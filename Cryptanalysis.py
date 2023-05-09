
"""
Script for analyzing ciphertext files in krypton4
takes files in the working directory as arguments
and does a frequency analysis
"""
import sys
import string
from Bucket import Bucket
class Cryptanalysis:

	def __init__(self, fileList):
		#set the file list provided from command line
		self.fileList = fileList
		#get a list of the alphabet and the default key values 0
		alphabet = list(string.ascii_uppercase)
		initKeys = [0] * 26

		#initialize the frequency map for counting freq
		self.frequencyMap = dict(zip(alphabet, initKeys))
		#total letter count of all the files to compute a p-value for each letter
		self.letCount = 0
		#create the bucket hashmaps for each index in the key 
		keyBuckets = [0, 1, 2, 3, 4, 5]
		self.bucketList = []

		for i in keyBuckets:
			self.bucketList.append(Bucket(keyBuckets[i]))
		
	#split each line into six letter increments and merge the found files
	def splitNMerge(self):
		vigeData = open("vigeData", "w")

		for f in self.fileList:
			for line in open(f):
				line = line.replace(" ", "")
				n = 6
				for i in range(0, len(line), n):
					vigeData.write(line[i:i+n] +"\n")

		vigeData.close()

	#examine the processed file given the key length and update the corresponding bucket map
	def proccFileAnalysis(self):
		#update the frequency map given the bucket index in the six letter line and the letter in the
		#corresponding line
		for line in open("vigeData"):
			for i in range(0, len(line)):
				if line[i] == "\n":
					continue

				self.bucketList[i].incMap(line[i])

		#print the bucket frequency maps
		for bucket in self.bucketList:
			bucket.printMap()

	#run the generic frequency analysis on the file list
	def freqAnalysis(self):
		for f in self.fileList:
			for line in open(f):
				line = line.replace(" ", "")
				for c in range(0, len(line)):
					self.frequencyMap[line[c]] = self.frequencyMap.get(line[c]) + 1
					self.letCount += 1

	#print the frequency map for all the files 
	def printFreqMap(self):
		
		print("Frequencies: ")
		
		for key in self.frequencyMap:
			print(key, self.frequencyMap[key])
		
		print("Probabilities: ")
		
		for key in self.frequencyMap:
			print(key, round(self.frequencyMap[key] / self.letCount, 4))

#main
if __name__ == "__main__":
	analysis = Cryptanalysis(sys.argv[1:])
	#analysis.freqAnalysis()
	#analysis.printFreqMap()
	#analysis.splitNMerge()
	analysis.proccFileAnalysis()