# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
data = pd.read_csv('marketing_campaign.csv', sep='\t')

# Display first 10 rows of the data
data.head(10)

# Display total rows and columns of the dataset
data.shape

# Find missing values
data.isnull().sum()

# Find whether the missing values in Income are random
data[data['Income'].isna()]

# Find if there are any outliers
plt.figure(figsize=(40, 30))
sns.boxplot(data=data)
plt.show()

# Since the missing values are at random and there are outliers, perform median imputation
data['Income'] = data['Income'].fillna(data['Income'].median())

# Find the missing values
data.isnull().sum()

# Drop the Dt_Customer column
data.drop(columns=['Dt_Customer'], inplace=True)

# Display first few rows of the data to see the result
data.head()

# Perform Categorical Encoding for certain columns
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

categorical_columns = ['Education', 'Marital_Status']
for col in categorical_columns:
    data[col] = le.fit_transform(data[col])

# Perform Robust Scaling since there are outliers in the data
from sklearn.preprocessing import RobustScaler

rob_scaler = RobustScaler()
scaled_data = rob_scaler.fit_transform(data)

# Perform K-means clustering
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics import silhouette_score

WCSS = []
k_range = range(2, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, init='k-means++')
    kmeans.fit(scaled_data)
    WCSS.append(kmeans.inertia_)
print(WCSS)

plt.figure(figsize=(8, 4))
plt.plot(k_range, WCSS, marker='o')
plt.title("Elbow Method for KMeans")
plt.xlabel("Number of clusters (k)")
plt.ylabel("WCSS")
plt.show()

kmeans_silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(scaled_data)
    score = silhouette_score(scaled_data, cluster_labels)
    kmeans_silhouette_scores.append(score)

plt.figure(figsize=(8, 6))
plt.plot(range(2, 11), kmeans_silhouette_scores, marker='o', linestyle='dashed')
plt.title('Silhouette Scores for KMeans')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()

!pip install scikit-learn-extra

from sklearn_extra.cluster import KMedoids
kmedoids_wcss = []
for k in k_range[1:]:
    kmedoids = KMedoids(n_clusters=k, random_state=42)
    kmedoids.fit(scaled_data)
    kmedoids_wcss.append(kmedoids.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(k_range[1:], kmedoids_wcss, marker='o', linestyle='--', color='g')
plt.title('Elbow Method for KMedoids')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS (KMedoids)')
plt.show()

kmedoids_silhouette_scores = []
for k in range(2, 11):
    kmedoids = KMedoids(n_clusters=k, random_state=42)
    cluster_labels = kmedoids.fit_predict(scaled_data)
    score = silhouette_score(scaled_data, cluster_labels)
    kmedoids_silhouette_scores.append(score)

plt.figure(figsize=(8, 6))
plt.plot(range(2, 11), kmedoids_silhouette_scores, marker='o', linestyle='--', color='g')
plt.title('Silhouette Scores for KMedoids')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()

# Find the cluster counts
cluster_counts = pd.Series(kmedoids.labels_).value_counts()
print(cluster_counts)

cluster_sizes = pd.Series(kmedoids.labels_).value_counts()
valid_clusters = cluster_sizes[cluster_sizes > 1].index

# Filter data to include only valid clusters
filtered_data = data_scaled[np.isin(kmedoids.labels_, valid_clusters)]
filtered_labels = kmedoids.labels_[np.isin(kmedoids.labels_, valid_clusters)]

# Compute silhouette score only for valid clusters
if len(np.unique(filtered_labels)) > 1:
    score = silhouette_score(filtered_data, filtered_labels)
    print("Silhouette Score:", score)
else:
    print("Not enough clusters to compute silhouette score.")

from sklearn.cluster import DBSCAN

# Try 5 different combinations of eps and min_samples
dbscan_params = [
    {'eps': 0.6, 'min_samples': 5},
    {'eps': 1.2, 'min_samples': 10},
    {'eps': 1.5, 'min_samples': 15},
    {'eps': 0.8, 'min_samples': 20},
    {'eps': 1.0, 'min_samples': 25}
]

for params in dbscan_params:
    dbscan = DBSCAN(eps=params['eps'], min_samples=params['min_samples'])
    dbscan_labels = dbscan.fit_predict(scaled_data)
    if len(set(dbscan_labels)) > 1:
        silhouette = silhouette_score(scaled_data, dbscan_labels)
        print(f"DBSCAN (eps={params['eps']}, min_samples={params['min_samples']}) Silhouette Score: {silhouette:.3f}")
    else:
        print(f"DBSCAN (eps={params['eps']}, min_samples={params['min_samples']}) resulted in a single cluster.")

"""- **Better Parameters**: The combination eps=1.5, min_samples=15 showed the best result in terms of silhouette score (positive score), suggesting that DBSCAN works best with these settings for the given dataset.
- **Worse Parameters**: The eps=1.0, min_samples=25 combination resulted in a negative silhouette score, which suggests that DBSCAN had a hard time identifying well-formed clusters, and many points may have been misclassified.
"""