import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

df = pd.read_excel("./Book1.xlsx")

print(df)
# Convert categorical variables to numerical labels
le = LabelEncoder()
df['outlook'] = le.fit_transform(df['outlook'])
df['temp'] = le.fit_transform(df['temp'])
df['humidty'] = le.fit_transform(df['humidty'])
df['windy'] = le.fit_transform(df['windy'])
df['play'] = le.fit_transform(df['play'])

# Features and target variable
x = df[['outlook', 'temp', 'humidty', 'windy']]
y = df['play']

clf = DecisionTreeClassifier(criterion="entropy", random_state=42)
clf.fit(x, y)

plt.figure(figsize=(10, 6))

plot_tree(clf,filled=True,feature_names=['outlook','temp','humidty','windy'],class_names=['No','Yes'])

plt.title("Decision tree for play tennis")
plt.show()