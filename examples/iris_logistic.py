import six

from sklearn import datasets
from sklearn import cross_validation
from sklearn import linear_model
from sklearn import metrics

import gas
from gas.utils.pprint import pprint

class SamplesGenerator(gas.Task):
	def run(self):
		six.print_("Loading the iris dataset...")

		# import some data to play with
		iris = datasets.load_iris()
		X = iris.data[:, :2]  # we only take the first two features.
		y = iris.target
		
		# save data to object
		self.X = X
		self.y = y
	def output(self):
		return {
			'X': self.X,
			'y': self.y,
		}

class Trainer(gas.Task):
	def requires(self):
		return SamplesGenerator()
	def run(self):
		X = self.input()['X']
		y = self.input()['y']

		X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y)

		six.print_("Training...")
		logreg = linear_model.LogisticRegression(C=1e5)
		logreg.fit(X_train, y_train)

		six.print_("Predicting on test dataset...")
		y_pred = logreg.predict(X_test)

		accuracy = metrics.accuracy_score(y_test, y_pred) * 100
		six.print_("Accuracy: {}%".format(accuracy))

def main():
	Trainer()

__name__ == "__main__" and main()
