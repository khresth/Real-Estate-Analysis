X_train, X_test, y_train, y_test = train_test_split(train_data.drop(['median_house_value'], axis=1), train_data['median_house_value'], test_size=0.2, random_state=42)

#Initializing and training the Decision Tree Regressor
dt_regressor = DecisionTreeRegressor(random_state=42)
dt_regressor.fit(X_train, y_train)

y_pred_train = dt_regressor.predict(X_train)
y_pred_test = dt_regressor.predict(X_test)
mse_train = mean_squared_error(y_train, y_pred_train)
mse_test = mean_squared_error(y_test, y_pred_test)
print(f'Training Mean Squared Error: {mse_train}')
print(f'Testing Mean Squared Error: {mse_test}')

#Evaluating the model using mean squared error

def predict_house_price():
    bedroom_ratio = float(input("Enter the bedroom ratio (total_bedrooms / total_rooms): "))
    population = input("Enter the population level (high/low): ").strip().lower()
    if population == 'high':
        population = train_data['population'].quantile(0.75)
    else:
        population = train_data['population'].quantile(0.25)
    
    income_level = float(input("Enter the income level (median_income): "))
    new_data = pd.DataFrame({
        'bedroom_ratio': [bedroom_ratio],
        'population': [population],
        'median_income': [income_level],
        'total_rooms': [train_data['total_rooms'].mean()],
        'total_bedrooms': [train_data['total_bedrooms'].mean()],
        'households': [train_data['households'].mean()],
        'longitude': [train_data['longitude'].mean()],
        'latitude': [train_data['latitude'].mean()],
    })

#making predictions

for column in X_train.columns:
        if column not in new_data.columns:
            new_data[column] = 0
    new_data = new_data[X_train.columns]
    prediction = dt_regressor.predict(new_data)
    print(f"Predicted House Price: ${prediction[0]:,.2f}")
predict_house_price()

  