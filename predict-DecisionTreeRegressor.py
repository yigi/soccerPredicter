from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('data/result/total.csv', usecols=["1st Half Home Ball Possession", "1st Half Home Goal Attempts", 
                                                     "1st Half Home Shots on Goal", "1st Half Home Shots off Goal", 
                                                     "1st Half Home Corner Kicks", "1st Half Home Attacks", "1st Half Home Dangerous Attacks", 
                                                     "1st Half Away Ball Possession", "1st Half Away Goal Attempts", 
                                                     "1st Half Away Shots on Goal", "1st Half Away Shots off Goal", 
                                                     "1st Half Away Corner Kicks","1st Half Away Attacks", "1st Half Away Dangerous Attacks", 
                                                     "1st Half Home Goals", "1st Half Away Goals", 
                                                     "2nd Half Home Goals", "2nd Half Away Goals"])
X = data.drop(['2nd Half Home Goals', '2nd Half Away Goals'], axis=1)
y = data[['2nd Half Home Goals', '2nd Half Away Goals']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor(max_depth=5, random_state=42)
dt.fit(X_train, y_train)

y_pred = dt.predict(X_test)

new_data = [[23,4,1,3,1,41,10,77,5,3,2,1,54,22,0,2]]
new_pred = dt.predict(new_data)
print(new_pred)