#Please place your FUNCTION code for step 4 here.

#IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import random


def openckdfile():
    #opens data file, extracts and stores data
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalize_data(glucose, hemoglobin, classification):
    #normalizes data on the same scale so it can be properly graphed
    gluc = (glucose-70)/(490-70)
    hemo = (hemoglobin-3.1)/(17.8-3.1)
    return gluc, hemo, classification

def random_centroids(k):
    #SELECT part of algorithm
    #selects random initial starting points for k centroids
    centroids_array = np.zeros((k,2))
    for i in range(k):
        centroids_array[i,0] = random.uniform(0,1)
        centroids_array[i,1] = random.uniform(0,1)        
    return centroids_array
    
def calculate_dist(centroids_array, gluc, hemo, classification, k):
    #calculates the distance of each point to each centroid
    distance_array = np.zeros((len(gluc),k))
    for i in range(k):
        centroid_gluc = centroids_array[i,0]
        centroid_hemo = centroids_array[i,1]
        distance_array[:,i] = np.sqrt((centroid_gluc - gluc)**2 + (centroid_hemo - hemo)**2)    
    return distance_array

def assign(centroids_array, gluc, hemo, classification, k):
    #ASSIGN part of algorithm
    #assigns a class to every point based on which centroid it's nearest to
    distance = calculate_dist(centroids_array, gluc, hemo, classification, k)
    point_dist = np.zeros(k)
    assignment = np.zeros(len(gluc))
    for row in range(len(gluc)):
        for col in range(k):
            point_dist[col] = distance[row,col]
        cluster_label = np.argmin(point_dist)
        assignment[row] = cluster_label
    return assignment

def update(gluc, hemo, assignment, k):
    #UPDATE part of algorithm
    #averages the locations of all points in a cluster to calculate new location of centroids
    new_centroid_array = np.zeros((k,2))
    for i in range(k):
        new_centroid_gluc = np.mean(gluc[assignment == i])
        new_centroid_hemo = np.mean(hemo[assignment == i])
        
        new_centroid_array[i,0] = new_centroid_gluc
        new_centroid_array[i,1] = new_centroid_hemo
    return new_centroid_array     
          
    
def graphingKMeans(glucose, hemoglobin, assignment, centroids):
    #graphs clusters and centroids, separating them by color
    plt.figure()
    for i in range(int(assignment.max())+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 1], centroids[i, 0], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
#NOTE: ITERATE part of algorithm is included in main code in driver