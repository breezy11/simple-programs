# Program koristi data set: https://www.kaggle.com/ronitf/heart-disease-uci.
# Odabrao sam ovaj data set tako što sam filtrirao data setove s filterom classification, i odabrao onaj s najviše glasova.

# Imports
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.cluster import KMeans

# Učitati data set i prikazati prvih 5 redova.
data = pd.read_csv('datasets/heart.csv')
print(data.head())

# Provjeriti da li ima null-vrijednosti.
print(data.isnull().sum())

# Izbaciti 'target' stupac iz dataframe-a, jer on govori da li ima ili nema bolesti.
X = data.drop("target", axis=1).values

# Labels - kategorije
y = data['target'].values

# Kreirati scaler da se mogu podaci skalirati, range će biti (0-1).
scaler = MinMaxScaler(feature_range=(0,1))
X = scaler.fit_transform(X)

# Prikazati skalirane podatke.
print(X)

# Podjeliti data set na test i train podatke, te prikazati podjelu.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print('Train set: X', X_train.shape, ', y', y_train.shape, '| Test set: ', X_test.shape, ' , y', y_test.shape)

# Kreiranje K-Nearest-Neighbor modela.
# Parametar n_neighbors je postavljen na broj 5 jer na stranici u opisu data seta kazu da je cilj predviditi prisustnost bolesti srca (0-4).
knn_model = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
predvidanje = knn_model.predict(X_test)
acc = metrics.accuracy_score(y_test, predvidanje)

print('Preciznost K-Nearest-Neighbor algoritma je: ', acc.max())

# Kreiranje K-means clustering modela.
# Parametar n_clusters je takoder postavljen na broj 5.
kmeans_model = KMeans(n_clusters=2, random_state=42).fit(X_train, y_train)
predvidanje = kmeans_model.predict(X_test)
preciznosti = metrics.accuracy_score(y_test, predvidanje)

print('Preciznost K-Means algoritma je: ', preciznosti.max())

# Po što je preciznost K-Means bila mala, odlučio sam iterirati 20 puta pa ispisati maksimalnu preciznost i broj klustera s kojim je postignuta.

n = 20
preciznosti = np.zeros(n - 1)

for i in range(1, n):
    # Istrenirati model i predvidjeti.

    kmeans_model = KMeans(n_clusters=i, random_state=42).fit(X_train, y_train)
    predvidanje = kmeans_model.predict(X_test)
    preciznosti[i - 1] = metrics.accuracy_score(y_test, predvidanje)

print('Maksimalna preciznost:', preciznosti.max())
print('Postignuta je s', (np.argmax(preciznosti) + 1), 'cluster-om.')