import pandas as pd
data = pd.read_csv('https://s3.amazonaws.com/demo-datasets/wine.csv')
numeric_data=data.drop('color',1)
#print(numeric_data)
numeric_data=(numeric_data-numeric_data.mean())/numeric_data.std()
#print(numeric_data)
import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)

#go to hw3_case_study_3.ipynb afterward