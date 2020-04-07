import os

import numpy as np
from pymongo import MongoClient

client = MongoClient()
db = client.housing_ml
houses = db.houses
houses.delete_many({})
data = np.loadtxt(os.path.join('..', 'data', 'housing.txt'), delimiter=',')
newHouses = list({'sq_feet': row[0], 'num_bedrooms': row[1], 'price': row[2]} for row in data)
houses.insert_many(newHouses)
