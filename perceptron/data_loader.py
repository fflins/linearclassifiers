import pandas as pd
import numpy as np

def join_classes(classe1, classe2):
    data = pd.read_csv("../data.csv", decimal=",")
    data = data[data["Species"].isin([classe1, classe2])]
    values = data.drop(columns=["Species"]).values  
    classes = np.array([1 if label == classe1 else -1 for label in data["Species"]]) 
    values = np.hstack([values, np.ones((values.shape[0], 1))])
    
    return values, classes  