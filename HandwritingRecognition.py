
import numpy as np
import matplotlib.pyplot as pplot
import pandas as panda
from sklearn.tree import DecisionTreeClassifier

data = panda.read_csv("datasets/handwritten_data_785.csv").as_matrix()
test_data = panda.read_csv("datasets/test.csv").as_matrix()
clf = DecisionTreeClassifier()

#training dataset
xtrain = data[0:,1:]
train_label = data[0:,0]
clf.fit(xtrain,train_label)

#testing dataset
xtest = test_data[0:,0:]

d = xtest[8]
print(xtest[8])
d.shape = (28,28)
pplot.imshow(255-d,cmap="gray")
print(clf.predict([xtest[8]]))
pplot.show()





