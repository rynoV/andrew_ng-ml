import numpy as np
from pymongo import MongoClient


def loadData():
    client = MongoClient()
    db = client.housing_ml
    housesCol = db.houses
    houses = housesCol.find()
    data = np.array(list([house['sq_feet'], house['num_bedrooms'], house['price']] for house in houses))
    X = data[:, :2]
    y = data[:, 2]
    return X, y
