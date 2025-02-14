#combining features to make one interesting feature
train_data['bedroom_ratio'] = train_data['total_bedrooms']/train_data['total_rooms']
train_data['household_rooms'] = train_data['total_rooms']/train_data['households']
plt.figure(figsize =(15,10))
sns.heatmap(train_data.corr(numeric_only=True),annot=True, cmap="YlGnBu")