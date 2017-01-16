# Import required packages
from tensorflow.contrib import learn
from tensorflow.contrib import layers
from sklearn import model_selection
import tensorflow as tf
import pandas as pd
import numpy as np
import os

# Set logging level to info to see detailed log output
tf.logging.set_verbosity(tf.logging.INFO)

os.chdir("/home/algo")

# Read the train data
sample = pd.read_csv("train1.csv")
sample.shape
sample.info()

X = learn.extract_pandas_data(sample[['x1','x2']])
y = learn.extract_pandas_labels(sample[['label']])

# Divide the input data into train and validation
X_train,X_validation,y_train,y_validation = model_selection.train_test_split(X,y, test_size=0.2, random_state=100)
type(X_train)

#feature engineering
feature_cols = [layers.real_valued_column("", dimension=2)]

#build the model configuration              
classifier = learn.LinearClassifier(feature_columns=feature_cols,
                                            n_classes=2,
                                            model_dir="/home/algo/m3")              

#build the model
classifier.fit(x=X_train, y=y_train, steps=1000)
classifier.weights_
classifier.bias_

#evaluate the model using validation set
results = classifier.evaluate(x=X_validation, y=y_validation, steps=1)
type(results)
for key in sorted(results):
    print "%s:%s" % (key, results[key])
    
# Predict the outcome of test data using model
X_test = np.array([[100.4,21.5],[200.1,26.1]])
predictions = classifier.predict(X_test)
predictions
