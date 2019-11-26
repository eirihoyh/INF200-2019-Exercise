# -*- coding: utf-8 -*-
__author__ = "Eirik Høyheim"
__email__ = "eirihoyh@nmbu.no"

import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.exceptions import NotFittedError
from sklearn.utils import check_random_state, check_X_y


def sigmoid(z):
    """\frac{1}{1 + exp(-\mathbf{z})}"""
    # Your code here
    return 1/(1 + np.exp(-z))


def predict_proba(coef, X):
    # Your code here
    pass


def logistic_gradient(coef, X, y):
    # Your code here
    pass


class LogisticRegression(BaseEstimator, ClassifierMixin):

    def __init__(
            self, max_iter=1000, tol=1e-5, learning_rate=0.01,
            random_state=None
    ):
        self.max_iter = max_iter
        self.tol = tol
        self.learning_rate = learning_rate
        self.random_state = random_state

    def _has_converged(self, coef, X, y):

        # Your code here
        pass

    def _fit_gradient_descent(self, coef, X, y):

        # Your code here
        pass

    def fit(self, X, y):

        # This function ensures that X and y has acceptable data types
        # and flattens y to have shape (n,) if it has shape (n, 1)
        X, y = check_X_y(X, y, order="C")
        if any((y < 0) | (y > 1)):
            raise ValueError("Only y-values between 0 and 1 are accepted.")
        # A random state is a random number generator, akin to those
        # you made in earlier coursework. It has all functions of
        # np.ranom, but its sequence of random numbers is not affected
        # by calls to np.random.
        random_state = check_random_state(self.random_state)
        coef = random_state.standard_normal(X.shape[1])
        self.coef_ = self._fit_gradient_descent(coef, X, y)
        return self

    def predict_proba(self, X):

        if not hasattr(self, "coef_"):
            raise NotFittedError("Call fit before prediction")
        return predict_proba(self.coef_, X)

    def predict_log_proba(self, X):

        return np.log(self.predict_proba(X))

    def predict(self, X):

        return self.predict_proba(X) >= 0.5


if __name__ == "__main__":
    # Simulate a random dataset
    X = np.random.standard_normal((100, 5))
    coef = np.random.standard_normal(5)
    y = predict_proba(coef, X) > 0.5
    # Fit a logistic regression model to the X and y vector
    # Fill in your code here.
    # Create a logistic regression object and fit it to the dataset
    # Print performance information
    print(f"Accuracy: {lr_model.score(X, y)}")
    print(f"True coefficients: {coef}")
    print(f"Learned coefficients: {lr_model.coef_}")
