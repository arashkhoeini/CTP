import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from operator import itemgetter
import sqlite3
import pickle
#using sqlite as database
with sqlite3.connect('data.db') as con:

    data = con.execute("select * from features").fetchall()
    data = np.array(data, float)

    df = pd.DataFrame(data)
    df = df.interpolate()
    df = df.fillna(0)

    cols = list(range(1,14))
    cols.remove(5)

    X = df.values[:,cols]

    #scalling columns
    min_max_scaler = preprocessing.MinMaxScaler()
    X = min_max_scaler.fit_transform(X)

    model = pickle.load(open('model', 'rb'))
    Y = model.predict(X)

    #Writing to database
    pd.Series(Y).to_sql('targets' , con , if_exists='replace')
