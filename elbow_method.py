# -*- coding: utf-8 -*-
"""ELBOW METHOD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RmHnPdd4zB1-njOadZI8OqutCE5fKwpd
"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
xaxis = np.array([1, 4, 5, 6, 1, 4, 5, 6, 1, 2, 4, 6, 5, 5, 5, 1, 3, 4, 2, 6, 4, 5, 5])
yaxis = np.array([5, 4, 5, 6, 5, 3, 5, 4, 4, 4, 8, 1, 3, 2, 1, 5, 1, 8, 7, 6, 9, 1, 10])
X = np.array(list(zip(xaxis, yaxis))).reshape(len(xaxis), 2)
plt.plot()
plt.title('Data Visualization')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([0, 10])
plt.ylim([0, 15])
plt.scatter(xaxis, yaxis)
plt.show()

# create new plot and data
#plt.plot()
#X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
#colors = ['b', 'g', 'r']
#markers = ['o', 'v', 's']

# K-means using Euclidean distance and distortion concept
distortions = []
#total number of clusters
K = range(1,10)
#for every cluster value we calculate distortion
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    kmeanModel.fit(X)
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])

# Now that we have all the distortions we will plot the graph
plt.plot(K, distortions, 'bx-')
plt.xlabel('k-clusters')
plt.ylabel('Distortion')
plt.xlim([0, 10])
# plt.ylim([0, 3]) can set the y limit accordingly if and when needed otherwise it sets default value depending on graph
plt.title('Elbow method with Euclidean Distance')
plt.show()

# K-means using Inertia
inertias = []
#total number of clusters
K = range(1,10)
#for every cluster value we calculate inertia
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    kmeanModel.fit(X)
    inertias.append(kmeanModel.inertia_)

# Now that we have inertia we will plot the graph
plt.plot(K, inertias, 'bx-')
plt.xlabel('k-clusters')
plt.ylabel('Inertia')
plt.xlim([0, 10])
# plt.ylim([0, 3]) can set the y limit accordingly if and when needed otherwise it sets default value depending on graph
plt.title('Elbow method with Inertia')
plt.show()