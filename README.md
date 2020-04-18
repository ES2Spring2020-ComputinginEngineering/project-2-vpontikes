This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).
This dataset is stored in the csv file labelled ckd.

AUTHOR
Victoria Pontikes

OVERVIEW OF CLASSIFICATION METHODS
This project analyzes the dataset mentioned above using three different methods of data analysis:
	1. Nearest Neighbor Classifier (NNC)
		This method uses pre-classified values from a dataset to classsify a random test point.
		The random point is classified based on the class of whichever data point it is closest to.
	2. K-Nearest Neighbor Classifer (KNNC)
		This method is exactly the same as the Nearest Neighbor Classifier, except the random test 
		point is classified bcased on the class of the k data points it is closest to.
		K can be chosen randomly.
	3. K Means Clustering (KMC)
		This method uses four steps to (1) select a random location for k centroids, (2) assign all
		data points to a certain cluster, (3) update the location of the centroids based on the locations
		of all points in the cluster, and (4) iterate, repeating assign and update steps until the
		centroid locations no longer change.
		This is different from the other 2 methods because it doesn't rely on pre-classified data.

NEAREST NEIGHBOR CLASSIFICATION FILE
The NearestNeighborClassification file has code for analyzing the dataset using both the Nearest Neighbor and
K-Nearest Neighbor classifiers. For each classifer, you must first open the ckd file and extract the data, which is
done in the openckdfile() function. Then, in order to graph the data, you must normalize it which is done in the
normalizeData function. The other functions are either used in the classifiers or used to graph the data and the 
test point. If you run the code exactly as I have it written, it should display one graph of the original dataset,
one graph of the dataset with the test point, and an array of 5 classifications based on the K-Nearest Neighbor
classifier. 

NOTE: Sometimes, the classes from the two different classifiers can be different. To see the class assigned to 
the test point by each method, you can either use a print statement or use the variable explorer and search for 
newclass (the class from NNC) or k_class (the class from KNNC).

K MEANS CLUSTERING FUNCTIONS FILE
The KMeansClustering_functions file has all the necessary functions for analyzing a the dataset using the K Means
Clustering classifier. Again, like with the above classifiers, you must open the ckd file and normalize the data.
Both of these are achieved using the same functions used above. Each method of the KMC algorithm is performed in a
function, with the exception of iterate which is done in the driver. This file doesn't do anything, it simply 
contains the functions which are to be called by the driver.
 	
	FUNCTIONS
	1. openckdfile
		This function takes no arguments.
		It opens the ckd file and stores the glucose, hemoglobin, and classification values as individual arrays.
		It returns the glucose, hemoglobin, and classification arrays.
	2. normalize_data
		This function takes the glucose, hemoglobin, and classification arrays as arguments.
		It modifies the glucose and hemoglobin values to be on the same scale so they can be properly graphed.
		It returns the scaled glucose and hemoglobin arrays, which I call gluc and hemo, and the untouched classification array.
	3. random_centroids
		This function takes k as an argument.
		It creates k random centroids with random initial locations. This is the Select part of the algorithm.
		It returns a k x 2 array of centroids, with glucose values in the 1st column and hemoglobin values in the 2nd.
	4. calculate_dist
		This function takes a centroid array, gluc, hemo, classification, and k as arguments.
		This function calculates the distance of each point to each centroid and stores the distance in an array with k columns,
		and each row correlates to a different data point.
		It returns the distance array of all points to all centroids.
	5. assign
		This function takes a centroid array, gluc, hemo, classification, and k as arguments.
		It assigns a class to every point based on which centroid the point it nearest to. It does this using the distance array 
		calculated by calculate_dist, which is called inside assign. This is the Assign part of the algorithm.
		It returns an assignment array which contains the class of each point.
	6. update
		This function takes gluc, hemo, assignment, and k as arguments.
		It updates the location of each centroid based on the average location of all point in that centroid's cluster. This is 
		the Update part of the algorithm.
		It returns the newly calculated centroid locations in a k x 2 centroid array, with glucose values in the 1st column and
		hemoglobin values in the 2nd.

K MEANS CLUSTERING DRIVER FILE
The KMeansClustering_driver file calls all the functions from the functions file and uses them. Remember, both the
KMC driver and the NNC file MUST run the openckdfile function and store them in variables so they can be used in 
later code. The KMC driver is where you should run the code to classify data using the KMC method. Do not forget to
import the functions from the KMC functions file or else the code won't run. The final step of the KMC classification
method, iteration, is in the driver file. In the while loop, the iterate step is performed by assigning, updating, and looping.
This iteration continues until the loop count (x) reaches 1000 or the last 100 centroids equal each other, whichever
occurs first. These numbers can be changed, just make sure the amount of iterations is well over 10. Finally, the driver
prints the final locations of the centroids and graphs each cluster and centroid, coded by color. You know you have done 
this correctly if your centroids are in the middle of your clusters. Again, k is an arbitrary variable and can be changed 
to any integer. However, because the dataset we use only has 2 distinct classes, any k value above 2 begins to output centroids
that shift, so the final centroids will not be guaranteed to be the same after multiple runs if k>2.  



