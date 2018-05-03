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
from sklearn.metrics import accuracy_score

dataset = 'shuffled-full-set-hashed.csv'
df = pd.read_csv(dataset, header=None, names=['label', 'words'])
# vectorizer = TfidfVectorizer()
# print(df.groupby('label').count())

vectorizer = HashingVectorizer()
# X = vectorizer.fit_transform(df.words.values.astype('U'))
# y = df.label
# joblib.dump(vectorizer, 'vectorizer-all.pkl')
# svm = LinearSVC(C=1)
# clf = CalibratedClassifierCV(svm)
# clf.fit(X, y)
# joblib.dump(clf, 'model-all.pkl')

df_aws = df.sample(n=9000)
df_train, df_test = train_test_split(df_aws, test_size=0.2)
X_aws = vectorizer.fit_transform(df_train.words.values.astype('U'))
y_aws = df_train.label
df_test.to_csv('test_aws.csv', header=False, index=False)
joblib.dump(vectorizer, 'vectorizer-aws.pkl')
svm = LinearSVC(C=1, class_weight='balanced')
clf = CalibratedClassifierCV(svm)
clf.fit(X_aws, y_aws)
joblib.dump(clf, 'model-aws.pkl')

# df_train, df_test = train_test_split(df, test_size=0.2)
# X_local = vectorizer.fit_transform(df_train.words.values.astype('U'))
# y_local = df_train.label
# df_test.to_csv('test_local.csv', header=False, index=False)
# joblib.dump(vectorizer, 'vectorizer-local.pkl')
# svm = LinearSVC(C=1, class_weight='balanced')
# clf = CalibratedClassifierCV(svm)
# clf.fit(X_local, y_local)
# joblib.dump(clf, 'model-local.pkl')


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
cv_error = cross_val_score(LinearSVC(C=1), vectorizer.fit_transform(df_aws.words.values.astype('U')), df_aws.label, cv=5)
print('CV accuracy: %.3f +/- %.3f' % (np.mean(cv_error), np.std(cv_error)))
