# Elbow-Method
Elbow Method is implemented in python to determine k clusters in K-means algorithm.

The two methods to determine k clusters include distortion and inertia, the first of which uses Euclidean distance to calculate the average of the squared distances between the cluster centers of the respective clusters, while the latter is the sum of the squared distance of sample cluster points from their closest centroid. 
Both the methods are include in the code.
# Execution
Open this file in Google colab and run the file for the demo of Elbow-Method.
It produces a graph like this:

![image](https://user-images.githubusercontent.com/68595241/121759701-7cf97200-cb40-11eb-8eb3-0c4902c57c54.png)

![image](https://user-images.githubusercontent.com/68595241/121759712-8c78bb00-cb40-11eb-8aca-27858042f3ae.png)


As the improvement declines rapidly, an elbow shape is formed.
We will always choose the value of k at the elbow i.e. k = 4

# Article
Read my article at the following link to understand the algorithm:
https://www.educative.io/edpresso/what-is-the-elbow-method-in-python
