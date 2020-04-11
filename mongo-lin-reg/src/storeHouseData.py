import os

import numpy as np
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def storeHouseData():
    try:
        data = np.loadtxt(os.path.join('..', 'data', 'housing.txt'), delimiter=',')
        client = MongoClient(host=os.environ['MONGO_HOST'], port=27017)
        db = client.housing_ml
        houses = db.houses
        houses.delete_many({})
        newHouses = list({'sq_feet': row[0], 'num_bedrooms': row[1], 'price': row[2]} for row in data)
        houses.insert_many(newHouses)
    except ConnectionFailure as e:
        print(e)
