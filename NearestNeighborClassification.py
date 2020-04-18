#Please put your code for Step 2 and Step 3 in this file.

#IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import random

#FUNCTIONS
def openckdfile():
    #opens data file, extracts and stores data
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
    #normalizes data on the same scale so it can be properly graphed
    glucose_scaled = (glucose-70)/(490-70)
    hemoglobin_scaled = (hemoglobin-3.1)/(17.8-3.1)
    return glucose_scaled, hemoglobin_scaled, classification

def graphData(glucose, hemoglobin, classification):
    #graphs original data
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title('Glucose vs Hemoglobin')
    plt.legend()
    plt.show()

def createTestCase():
    #creates a random test case
    newglucose = random.uniform(0,1)
    newhemoglobin = random.uniform(0,1)
    return newglucose, newhemoglobin

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    #calculates distance array from test case to all original data points
    distance_array = np.zeros(158)
    distance_array = np.sqrt((glucose - newglucose)**2 + (hemoglobin - newhemoglobin)**2)
    return distance_array

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    #classifies test case using Nearest Neighbor Classifier method
    distance_array = calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification)
    min_index = np.argmin(distance_array)
    nearest_class = classification[min_index]
    return nearest_class

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, newclass):
    #graphs original data with test case
    #test case is opposite color of class it's in to make it stand out
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    if newclass == 1:
        plt.plot(newhemoglobin, newglucose, 'rx', markersize=20 )
    if newclass == 0:
        plt.plot(newhemoglobin, newglucose, 'kx', markersize=20)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title('Glucose vs Hemoglobin')
    plt.legend()
    plt.show()
 
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    #classifies test case using K-Nearest Neighbor Classifier method
    k_distance_array = calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification)
    sorted_indices = np.argsort(k_distance_array)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    print(k_classifications)
    k_class = round(np.mean(k_classifications))
    return k_class
    
# MAIN SCRIPT
#initializing variables    
glucose, hemoglobin, classification = openckdfile()
glucose_scaled, hemoglobin_scaled, classification = normalizeData(glucose, hemoglobin, classification)
newglucose, newhemoglobin = createTestCase()

print('Hemoglobin is', newhemoglobin)
print('Glucose is', newglucose)

#graphs original data set
graphData(glucose_scaled, hemoglobin_scaled, classification)

#classifies test case using nearest neighbor classifier
newclass = nearestNeighborClassifier(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification)

#graphs test case with original data
graphTestCase(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, newclass)

#classifies test case using k nearest neighbor classifier
k = 5 #change this based on how many surrounding points you want to compare the test case to
k_class = kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification)
