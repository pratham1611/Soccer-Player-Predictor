import csv
import random
import math
import operator
import os
import time

def LoadFromCSV(filename,trainingSet=[]):
	with open(filename, 'rt') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(6):
	            dataset[x][y] = int(dataset[x][y])
	        #if random.random() < split:
	        trainingSet.append(dataset[x])
	        #else:
	            #testSet.append(dataset[x])
				
def getNeighbors(trainingSet, testInstance, k):
	print("Inside getNeighbors method")
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x],length)
		distances.append((trainingSet[x], dist)) # Distances list will have individual training set instance and euclidian distance calculated  by comparing test instance to training set for e.g([[67,78,90,87,85,86,LB],16.53],[[80,76,87,56,81,67],18.5,RM] etc
	distances.sort(key=operator.itemgetter(1)) # sorting distances list based on euclidian distance i.e 2nd item of the list
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0]) #neighbors list will only have attributes list as individual list items for e.g [[67,78,90,87,85,86,LB],[80,76,87,56,81,67,RM],etc]
	return neighbors

def getResponse(neighbors):
	print("Inside getResponse method")
	classVotes = {} #dictionary
	for x in range(len(neighbors)):
		response = neighbors[x][-1] #gets the last element of the list i.e LB, RB
		print(neighbors[x][-1])
		if response in classVotes:
			classVotes[response] += 1 
		else:
			classVotes[response] = 1
	#classVotes dictionary would have dict_items([('RB', 1), ('LB', 4), ('RM', 1)])
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True) #operator.itemgetter works on index 1 to sort in reverse order
	print(sortedVotes)
	return sortedVotes[0][0] #returns first element of the 

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

dict_Description={
'ST':'Striker',
'CB':'Centre Back',
'LB':'Left Back',
'CM':'Centre Midfield',
'CDM':'Centre Defensive Midfield',
'LM':'Left Midfield',
'RM':'Right Midfield',
'RB':'Right Back',
'CAM':'Centre Attacking Midfield'
}	
def main():
	trainingSet=[]
	testSet=[]
	predictions=[]
	k=6
	dirpath=os.path.dirname(os.path.realpath(__file__))
	LoadFromCSV(dirpath+'\irisdata.csv',trainingSet)
	print('What if I could predict the type of player you were thinking?')
	time.sleep(5)
	print('Enter Pace,Shot,Passing,Dribbling,Defending,Physique Attributes (space seperated-out of 100): ')
	testSet = [int(x) for x in input().split()]
	#for x in range(len(testSet)):
	neighbors = getNeighbors(trainingSet, testSet, k)
	result = getResponse(neighbors)
	predictions.append(result)
	print('Were you thinking of a '+dict_Description[result]+'?')
	time.sleep(5)
main()