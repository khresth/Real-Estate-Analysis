data = pd.read_csv('housing.csv')
X = data.drop(['median_house_value'], axis=1)
y = data['median_house_value']
data.dropna(inplace=True) 

x_train, x_test, y_train, y_test = train_test_split(x ,y,test_size=0.2)

train_data = x_train.join(y_train)
train_data.hist(figsize=(15,10))
#these are distribution of various features, we will use sns heatmap to visualize correlation with target variable

plt.figure(figsize =(15,10))
sns.heatmap(train_data.corr(numeric_only=True),annot=True, cmap="YlGnBu")
#histogram is skewed, not a gaussian bell curve, lets take log of those features

train_data['total_rooms'] = np.log(train_data['total_rooms']+1)
train_data['total_bedrooms'] = np.log(train_data['total_bedrooms']+1)
train_data['population'] = np.log(train_data['population']+1)
train_data['households'] = np.log(train_data['households']+1)
train_data.hist(figsize=(15,10))

#we want to use the ocean proximity feature as well, we convert categorical feature to binary
train_data=train_data.join(pd.get_dummies(train_data.ocean_proximity)).drop(["ocean_proximity"], axis=1) 
plt.figure(figsize =(15,10))
sns.heatmap(train_data.corr(numeric_only=True),annot=True, cmap="YlGnBu")
plt.figure(figsize=(15,10))  
sns.scatterplot(x="latitude", y="longitude",data=train_data, hue="median_house_value", palette="coolwarm")