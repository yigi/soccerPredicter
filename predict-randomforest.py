import pandas as pd
from sklearn.ensemble import RandomForestRegressor
# load the csv data into a pandas dataframe
data = pd.read_csv('data/result/total.csv', usecols=["1st Half Home Ball Possession", "1st Half Home Goal Attempts", 
                                                     "1st Half Home Shots on Goal", "1st Half Home Shots off Goal", 
                                                     "1st Half Home Corner Kicks", "1st Half Home Attacks", "1st Half Home Dangerous Attacks", 
                                                     "1st Half Away Ball Possession", "1st Half Away Goal Attempts", 
                                                     "1st Half Away Shots on Goal", "1st Half Away Shots off Goal", 
                                                     "1st Half Away Corner Kicks","1st Half Away Attacks", "1st Half Away Dangerous Attacks", 
                                                     "1st Half Home Goals", "1st Half Away Goals", 
                                                     "2nd Half Home Goals", "2nd Half Away Goals"])
# separate the input features and target variable
X = data.iloc[:,:-2]
y = data.iloc[:,-2:]
# create an instance of the RandomForestRegressor
rf = RandomForestRegressor()
# fit the model on the input data and target variable
rf.fit(X, y)
# use the trained model to predict the values of X and Y for the new data
new_data = [[23,4,1,3,1,41,10,77,5,3,2,1,54,22,0,2]]
prediction = rf.predict(new_data)
# print the predicted values of X and Y
print(prediction)