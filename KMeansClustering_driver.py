#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions
import numpy as np

#initializing variables
glucose, hemoglobin, classification = kmc.openckdfile()
gluc, hemo, classification = kmc.normalize_data(glucose, hemoglobin, classification)
k = 3 #change this based on numbers of clusters you want

#selects random centroids
centroids = kmc.random_centroids(k)

count = 0
x = 0
#ITERATE part of algorithm
#constantly changes centroid/cluster location until x = 1000 or the last 100 centroids have been the same, whichever comes first
while x<1000:
    assignment = kmc.assign(centroids, gluc, hemo, classification, k)
    if np.array_equal(centroids, kmc.update(gluc, hemo, assignment,k)):
        count += 1
        if count == 100:
            print(centroids)
            break
    centroids = kmc.update(gluc, hemo, assignment, k)
    x+=1 

kmc.graphingKMeans(gluc, hemo, assignment, centroids) 