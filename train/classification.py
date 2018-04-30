import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer
from sklearn.svm import LinearSVC, SVC
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.calibration import CalibratedClassifierCV

dataset = 'shuffled-full-set-hashed.csv'
df = pd.read_csv(dataset, header=None, names=['label', 'words'])
# vectorizer = TfidfVectorizer()
# The free EC2 instance has very limited memory
# To use little memory, switch from TfidfVectorizer to HashingVectorizer
vectorizer = HashingVectorizer()
X = vectorizer.fit_transform(df.words.values.astype('U'))
y = df.label
joblib.dump(vectorizer, 'vectorizer.pkl')
svm = LinearSVC(C=1)
clf = CalibratedClassifierCV(svm)
clf.fit(X, y)
joblib.dump(clf, 'model.pkl')

# try to find the best C
# bestscore = -1
# bestcnumber = -1
# bestgnumber = -1

# for c in [0.001, 0.01, 0.1, 1, 10, 100, 1000]:
# 	clf_svc = LinearSVC(C=c)
# 	clf_svc.fit(X_train, y_train)
# 	score = clf_svc.score(X_test, y_test)
# 	if score > bestscore:
# 		bestcnumber = c
# 	print("SVM score at ", c, " is ", score)
#
# cv_error = cross_val_score(LinearSVC(C=bestcnumber), X, y, cv=5)
# print('CV accuracy: %.3f +/- %.3f' % (np.mean(cv_error), np.std(cv_error)))
