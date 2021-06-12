# Elbow-Method
Elbow Method implemented in python to determine k clusters in K-means algorithm.
The two methods to determine optimal clusters include distortion and inertia, the first of which uses Euclidean distance to calculate the average of the squared distances between the cluster centers of the respective clusters, while the latter is the sum of the squared distance of sample cluster points from their closest centroid. 
Now, there are two ways to implement the Elbow method using either distortions or inertia. Both are include in the code.
# Execution
Open this file in Google colab and run the file for the demo of Elbow-Method.
It produces a graph like this:

As is evident from the graph, as k increases the value of the y-axis decreases because the distance from the cluster centroid decreases. 
As the improvement declines rapidly, it forms an elbow shape.
Both graphs show that k = 4 is optimal where k is the number of clusters. We will always choose the value of k at the elbow.'

# Article
Read my article at the following link to understand the algorithm: https://www.educative.io/edpresso/what-is-the-elbow-method-in-python
