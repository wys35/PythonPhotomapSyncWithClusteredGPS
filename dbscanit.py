import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN

rawdata = pd.read_csv('data.csv', delimiter=',')
gpsdata = rawdata.loc[:, ['lat','lon']]

kms_per_radian = 6371.0088
epsilon = 10/kms_per_radian # 100 km 
db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(gpsdata))
#db = DBSCAN(eps=0.5, min_samples=3).fit(gpsdata)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)

print(labels)

for i, row in rawdata.iterrows():
    newlabel = labels[i]
    rawdata.at[i, 'label'] = newlabel

# sort the values, in case of revisit the same location twice.
rawdata = rawdata.sort_values(['label', 'filename'], ascending=[True, True])

rawdata.to_csv("datawithlabel.csv", sep=",", encoding='utf-8')    


# plotting
#import matplotlib.pyplot as plt
#unique_labels = set(labels)
#colors = [plt.cm.Spectral(each)
#            for each in np.linspace(0, 1, len(unique_labels))]
#for k, col in zip(unique_labels, colors):
#    if k == -1:
#        col = [0, 0, 0, 1]
#
#    class_member_mask = (labels ==k)
#
#    xy = gpsdata[class_member_mask & core_samples_mask]
#    plt.plot(xy.values[:, 0], xy.values[:, 1], 'o', markerfacecolor=tuple(col),
#    markeredgecolor='k', markersize=14)
#
#    xy = gpsdata[class_member_mask & ~core_samples_mask]
#    plt.plot(xy.values[:, 0], xy.values[:, 1], 'o', markerfacecolor=tuple(col),
#             markeredgecolor='k', markersize=6)
#
#plt.title('GPS coordinates, estimated number of clusters: %d' % n_clusters_)
#plt.show()
# end plotting


