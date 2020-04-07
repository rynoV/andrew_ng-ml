# Linear Regression on Housing Prices w/ MongoDB

This is an application which stores house data in a local MongoDB database, retrieves it, and performs linear
 regression on it to predict house prices.
 
src/storeHouseData.py takes the data from data/housing.txt and stores it in a MongoDB database called `housing_ml` in
 a collection called `houses`.

src/main.py retrieves all the documents from the `houses` collection, performs linear regression on the data, and
 predicts the price of a house. The normal equation method is used if there are fewer than 10,000 training examples (as
  recommended by Andrew Ng), and gradient descent is used otherwise.