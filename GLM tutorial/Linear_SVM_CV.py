import numpy as np
from sklearn.model_selection import KFold
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

# Generate sample data
X = #input trialized neural data (# of samples, # of features)
y = #input trial labels (# of samples,)

kf = KFold(n_splits=5)  # 5-fold cross-validation
accuracies = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Train a linear SVM
    clf = SVC(kernel='linear', C=1)  # Regularization with C parameter
    clf.fit(X_train, y_train)
    
    # Predict on the test set
    y_pred = clf.predict(X_test)
    
    # Calculate accuracy
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)

# Average accuracy across all folds
avg_accuracy = np.mean(accuracies)
print(f"Average Accuracy: {avg_accuracy:.2f}")