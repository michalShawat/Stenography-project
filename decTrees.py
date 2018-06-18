# given train1_x, train2_x, train3_x, train4_x, train8_x, train_y files
# performs machine learning by decision trees with different encoding techniques
# and different trees depth

import xgboost.sklearn as xgb
import numpy as np
from sklearn.model_selection import train_test_split

# performs XGBoost machine learning
def xgb_cl(x_train, x_test, y_train, y_test, max_depth):
    xg_cl = xgb.XGBClassifier(objective='binary:logistic',n_estimators=10, seed=123,max_depth=max_depth)
    xg_cl.fit(x_train, y_train)

    # Compute the accuracy of the predictions
    preds = xg_cl.predict(x_test)
    accuracy = float(np.sum(preds == y_test))/y_test.shape[0]
    print("xgb_cl Accuracy: %.2f%%" % (accuracy * 100.0))
    return accuracy * 100.0

# performs execution on one depth
def differ_depth(train_x_file, max_depth):
    x_train = np.loadtxt(train_x_file)
    y_train = np.loadtxt("train_y")

    # mix the images
    np.random.seed(0)
    np.random.shuffle(x_train)
    np.random.seed(0)
    np.random.shuffle(y_train)

    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=123)
    acc = xgb_cl(x_train, x_test, y_train, y_test, max_depth)
    return acc

# performs execution on one encoding technique
def one_run(train_x_file, depth_sizes):
    for i in depth_sizes:
        acc = differ_depth(train_x_file, i)
        print("depth: "+str(i)+", acc: "+str(acc))


def main():
    depth_sizes = [8, 16, 32, 64, 128, 256, 512]
    print("train1")
    one_run("train1_x", depth_sizes)
    print("train2")
    one_run("train2_x", depth_sizes)
    print("train3")
    one_run("train3_x", depth_sizes)
    print("train4")
    one_run("train4_x", depth_sizes)
    print("train8")
    one_run("train8_x", depth_sizes)

main()