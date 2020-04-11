import os

import numpy as np
from pymongo import MongoClient

from storeHouseData import storeHouseData


def loadData():
    client = MongoClient(host=os.environ['MONGO_HOST'], port=27017)
    db = client.housing_ml
    housesCol = db.houses
    if housesCol.count_documents({}) == 0:
        storeHouseData()
    houses = housesCol.find()
    data = np.array(list([house['sq_feet'], house['num_bedrooms'], house['price']] for house in houses))
    X = data[:, :2]
    y = data[:, 2]
    return X, y
