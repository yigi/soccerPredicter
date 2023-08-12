from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
# Load the data
data = pd.read_csv('data/result/total.csv', usecols=["1st Half Home Ball Possession", "1st Half Home Goal Attempts", 
                                                     "1st Half Home Shots on Goal", "1st Half Home Shots off Goal", 
                                                     "1st Half Home Corner Kicks", "1st Half Home Attacks", "1st Half Home Dangerous Attacks", 
                                                     "1st Half Away Ball Possession", "1st Half Away Goal Attempts", 
                                                     "1st Half Away Shots on Goal", "1st Half Away Shots off Goal", 
                                                     "1st Half Away Corner Kicks","1st Half Away Attacks", "1st Half Away Dangerous Attacks", 
                                                     "1st Half Home Goals", "1st Half Away Goals", 
                                                     "2nd Half Home Goals", "2nd Half Away Goals"])
# Split the data into X and Y
X = data.iloc[:, :-2].values
Y = data.iloc[:, -2:].values
# Create a MultiOutputRegressor
model = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=0))
# Fit the model with the data
model.fit(X, Y)
# Predict the values of X and Y
new_data = [[23,4,1,3,1,41,10,77,5,3,2,1,54,22,0,2]]
predicted = model.predict(new_data)
print(predicted)
predicted_values_int = [round(val) for val in predicted[0]]
print(predicted_values_int)
