# Stenography

In this project we trained a decision forest with encoded and unencoded images.
1. Extract images from the CIFAR-10 data set.
2. Insert a malicious code into half of the images.
3. Perform a decision forest with 80:20 train-test ratio.

## Getting Started

1. Clone the project to your computer.
2. Download CIFAR-10 python version data set from [here](https://www.cs.toronto.edu/~kriz/cifar.html) to this directory.
3. Download XGBoost. You can use this [installation guide](https://xgboost.readthedocs.io/en/latest/build.html)

## Deployment

1. Create empty batchX, encodedX directories (batch1, batch2,...encoded1, encoded2,...) for your desired batches from CIFAR-10.
2. Run run.py.

## Results
You can see our results table [here](https://github.com/michalShawat/Stenography/blob/master/results%20table.PNG)
and the graph [here](https://github.com/michalShawat/Stenography/blob/master/graphUpdated.PNG).
With depth trees of 256 we managed to acheive around 85% detection on the test sets, regardless to the encoding technique.

## Authors

* **Galit Vaknin** - [Galit1321](https://github.com/Galit1321)

* **Ifat Neumann** - [neumani1](https://github.com/neumani1)

* **Michal Shawat** - [michalShawat](https://github.com/michalShawat)

## Acknowledgments

* The BIU Center for Research in Applied Cryptography and Cyber Security in Bar-Ilan University
