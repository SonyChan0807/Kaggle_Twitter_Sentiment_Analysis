import numpy as np
import pickle
import csv
import xgboost as xgb

train1 = pickle.load(open("train_model1_2.txt", "rb"))
train2 = pickle.load(open("train_model2_2.txt", "rb"))
train3 = pickle.load(open("train_model3_2.txt", "rb"))
train4 = pickle.load(open("train_model4_2.txt", "rb"))

test1 = pickle.load(open("test_model1_2.txt", "rb"))
test2 = pickle.load(open("test_model2_2.txt", "rb"))
test3 = pickle.load(open("test_model3_2.txt", "rb"))
test4 = pickle.load(open("test_model4_2.txt", "rb"))


train = np.hstack((train1, train2, train3, train4))
test = np.hstack((test1, test2, test3, test4))
y = np.array(int(2500000/2) * [0] + int(2500000/2) * [1])
np.random.seed(0)
np.random.shuffle(y)


model = xgb.XGBClassifier().fit(train, y)

y_pred = model.predict(test)
y_pred = 1 - 2 * y_pred

with open('run_submission4.csv', 'w') as file:
    fieldnames = ['Id', 'Prediction']
    writer = csv.DictWriter(file, delimiter=",", fieldnames=fieldnames)
    writer.writeheader()
    for r1, r2 in zip(np.arange(1,10001), y_pred):
        writer.writerow({'Id': int(r1), 'Prediction': int(r2)})
