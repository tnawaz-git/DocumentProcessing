import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import pickle
from collections import OrderedDict
import matplotlib.pyplot as plt
from PIL import Image
import itertools

# #############################################################################
# Load data

with open('res_0.bin', 'rb') as f:
    data = pickle.load(f)

rects=[]
rects_pos=[]

for z in data:
    rects.append(z[0])

for x in rects:
    rects_pos.append([x[0]+x[2]/2,x[1]+x[3]/2])

X=rects_pos

#X, labels_true = make_blobs(n_samples=len(X), centers=rects_pos, cluster_std=0.4, random_state=0)

scaler=StandardScaler()
scaler.fit(X)
X=scaler.transform(X)
Y= scaler.inverse_transform(X)

# #############################################################################
# Compute DBSCAN
db = DBSCAN(eps=0.2, min_samples=4).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

clusters= OrderedDict()

for i in range (0,len(Y)):
    clusters[(Y[i, 0],Y[i, 1])]= labels[i]

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Estimated number of clusters: %d' % n_clusters_)
print("Number of total datapoints: ", len(X))
print('Estimated number of noise points: %d' % n_noise_)
print(clusters)
print(set(labels))

# #############################################################################

# Plotting K-distance Graph

""" neigh = NearestNeighbors(n_neighbors=2)
nbrs = neigh.fit(X)
distances, indices = nbrs.kneighbors(X)

distances = np.sort(distances, axis=0)
distances = distances[:,1]
plt.figure(figsize=(7,7))
plt.plot(distances)

plt.title('K-distance Graph',fontsize=20)
plt.xlabel('Data Points sorted by distance',fontsize=14)
plt.ylabel('Epsilon',fontsize=14)

plt.show() """

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()

# Display the image
imgg=Image.open('img_res_0.png')
plt.imshow(imgg)
colors=itertools.cycle(['b','g','r','c','m','y','k','w'])

clr= dict()
for a in set(labels):
    clr[a]=next(colors)

for z in clusters:
    if clusters[z] != -1:

        plt.scatter(z[0], z[1], s=10, c=clr[clusters[z]], marker='o')
    
    else:
        
        plt.scatter(z[0], z[1], s=20, c=clr[clusters[z]], marker='x')

plt.show()

