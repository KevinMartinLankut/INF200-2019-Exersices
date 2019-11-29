# -*- coding: utf-8 -*-
__author__ = "Kevin Martin Lankut"
__email__ = "kela@nmbu.no"


import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.exceptions import NotFittedError
from sklearn.utils import check_random_state, check_X_y


def sigmoid(z):
    """
    Perform a logistic transform on the input.

    This function applies the sigmoidal function element-wise to all
    elements of z. The sigmoidal function is on the following mathematical form:

    F(z) = 1/(1+e^-z)

    Parameters:
    :param z: Logit to transform (np.ndarray)

    Returns:
    :return sigmoidal_transformed_z: Transformed input (np.ndarray)
    """
    sigmodial_transformex_z = 1 / (1 + np.exp(-z))
    return sigmodial_transformex_z


def predict_proba(coef, X):
    """
    Predict the class probabilities for each data point in X.

    Estimate which class each data point in X corresponds to. This is done
    according to the following formula:

    hat{y}_i = σ(x_i^T*w)

    where x_i is the i-th row in X and σ is the sigmoidal function.
    Alternatively, in matrix-vector form:

    hat{y}=σ(X*w)

    Parameters:
    :param coef: The weight vector w (np.ndarray(shape=(r,))
    :param X: The data matrix (np.ndarray(shape=(n, r))

    Returns:
    :return p: The predicted class probabilities (np.ndarray(shape(n,))
    """
    product = X.dot(coef)
    p = sigmoid(product)
    return p


def logistic_gradient(coef, X, y):
    """
    Returns the gradient of a logistic regression model.

    The gradient is given by:

    ∇_w*L(w;X,y) = ∑_i(x_i(hat{y}_i−y_i)

    or elementwise:

    [∇_w*L(w;X,y)]_j = ∂L/∂w_j = ∑_i(X_ij(hat{y}_i−y_i)

    where hat{y}_i is the predicted value for data point i and is given by
    σ(x_i^T*w), where σ is the sigmoidal function.

    Parameters:
    :param coef: The weight vector w (np.ndarray(shape=(r,))
    :param X: The data matrix (np.ndarray(shape=(n, r))
    :param y: The true class labels for each data point (np.ndarray(shape=(n,))

    Returns:
    :return gradient: The gradient of the cross entropy loss related to the
    linear logistic regression model(np.ndarray(shape=(r,))
    """
    hat_y = predict_proba(coef, X)
    gradient = np.transpose(X)@(hat_y-y)
    return gradient


class LogisticRegression(BaseEstimator, ClassifierMixin):
    """
    A logistic regression classifier that follows the scikit-learn API.

    Note that the __init__ method of scikit-learn estimators should not do any
    logic or input validation. This is all taken care of in the fit method.

    Parameters:
    :param max_iter: Maximum number of gradient descent iterations to run.
    default = 1000
    :type: int

    :param tol: The gradient descent iterations will converge when the gradient
    norm is less than this.
    default = 1e-5
    :type: float

    :param learning_rate: The step-size for the gradient descent updates.
    default = 0.01
    :type: float

    :param random_state: np.random.random_state, int or None(default=None)
        A numpy random state object or a seed for a numpy random state object

    Attributes:
    coef: np.ndarray(shape=(r,))
        The logistic regression weights (initialised in self.fit)
    max_iter: int(default=1000)
            Maximum number of gradient descent iterations to run.
    tol: float(default=1e-5)
        The gradient descent iterations will converge when the gradient
        norm is less than this.
    learning_rate: float(default=0.01)
        The step-size for the gradient descent updates.
    random_state: np.random.random_state, int or None(default=None)
        A numpy random state object or a seed for a numpy random state object.
    """

    def __init__(
            self, max_iter=1000, tol=1e-5, learning_rate=0.01, random_state=None):
        """
        Initialise a logistic regression instance.

        The __init__ method of scikit-learn estimators should not do any
        logic or input validation. This is all taken care of in the fit method.

        Parameters:
        :param max_iter: Maximum number of gradient descent iterations to run.
        default=1000
        :type: int

        :param tol: The gradient descent iterations will converge when the
        gradient norm is less than this.
        default=1e-5
        :type: float

        :param learning_rate: The step-size for the gradient descent updates.
        default=0.01
        :type: float

        :param random_state: np.random.random_state, int or None(default=None)
            A numpy random state object or a seed for a numpy random state
            object
        """
        self.max_iter = max_iter
        self.tol = tol
        self.learning_rate = learning_rate
        self.random_state = random_state

    def _has_converged(self, coef, X, y):
        """
        Whether the gradient descent algorithm has converged.

        Returns True if the norm of the gradient is smaller than self.tol.
        Mathematically that is:

        ||∇_w*L(w^k;X,y)||<T

        where ∇_w*L is the gradient of the loss function, ||v|| is the norm of
        the vector v, w^k is the weights at iteration k, and T is the
        convergence tolerance(self.tol).

        Parameters:
        :param coef: The weight vector w^(k) (np.ndarray(shape=(r,))
        :param X: The data matrix (np.ndarray(shape=(n, r))
        :param y: The true class labels for each data point
        (np.ndarray(shape=(n,))

        Returns:
        :return has_converged: True if the convergence criteria above is met,
        False otherwise.
        :type: bool
        """
        gradient = np.linalg.norm(logistic_gradient(coef, X, y))
        if gradient < self.tol:
            return True
        else:
            return False

    def _fit_gradient_descent(self, coef, X, y):
        """
        Fit the logisitc regression model to the data given initial weights

        Gradient descent works by iteratively applying the following update
        rule

        w^k <- w^(k-1) - η*∇*L(w^(k−1);X,y)

        where w^k is the coefficient vector at iteration k, w^(k-1) is the
        coefficient vector at iteration k-1, η is the learning rate and
        ∇*L(w^(k−1);X,y) is the gradient of the loss function at iteration k-1.

        The iterative algorithm should be performed for at most self.max_iter
        iterations, or until the convergence criteria is reached.

        Parameters:
        :param coef: The initial guess for the coefficient vector.
        May be modified inplace by the method (np.ndarray(shape=(r,))
        :param X: The data matrix(np.ndarray(shape=(n, r))
        :param y: The target vector(np.ndarray(shape=(n,))

        Returns:
        :return coef: The logistic regression weights(np.ndarray(shape=(n,))
        """
        k = 0
        converged = False

        while (not converged) and k < self.max_iter:
            converged = self._has_converged(coef, X, y)
            coef = coef - self.learning_rate*logistic_gradient(coef, X, y)
            k += 1
        return coef


    def fit(self, X, y):
        """
        Fit a logistic regression model to the data.

        Parameters:
        :param X: The data matrix(np.ndarray(shape=(n, r))
        :param y: The observed classes for each data point in X
        (np.ndarray(shape=(n,))
        """
        # This function ensures that X and y has acceptable data types
        # and flattens y to have shape (n,) if it has shape (n, 1)
        X, y = check_X_y(X, y, order="C")

        if any((y < 0) | (y > 1)):
            raise ValueError("Only y-values between 0 and 1 are accepted.")

        # A random state is a random number generator, akin to those
        # you made in earlier coursework. It has all functions of
        # np.random, but its sequence of random numbers is not affected
        # by calls to np.random.
        random_state = check_random_state(self.random_state)
        coef = random_state.standard_normal(X.shape[1])

        self.coef_ = self._fit_gradient_descent(coef, X, y)
        return self

    def predict_proba(self, X):
        """
        Estimate the class probabilities.

        This function returns the probability that each datapoint belongs to
        the positive class.

        Parameters:
        :param X: The data matrix(np.ndarray(shape=(n, r))

        Returns:
        :return p: A vector of probabilities. The i-th entry is the probability
        for the i-th data point belonging to the positive class(np.ndarray)
        """
        if not hasattr(self, "coef_"):
            raise NotFittedError("Call fit before prediction")
        return predict_proba(self.coef_, X)

    def predict_log_proba(self, X):
        """
        Estimate the class log probabilities.

        This function returns the probability that each datapoint belongs to
        the positive class.

        Parameters:
        :param X: The data matrix(np.ndarray(shape=(n, r))

        Returns:
        :return lp: A vector of log probabilities. The i-th entry is the log
        probability for the i-th data point belonging to the positive class
        (np.ndarray)
        """
        return np.log(self.predict_proba(X))

    def predict(self, X):
        """
        Predict whether each data point in X belongs to the positive class

        Parameters:
        :param X: The data matrix(np.ndarray(shape=(n, r))

        Returns:
        :return yhat: Predicted classes for the input data matrix(np.ndarray)
        len(yhat) == len(X)
        """
        return self.predict_proba(X) >= 0.5


if __name__ == "__main__":
    # Simulate a random dataset
    X = np.random.standard_normal((100, 5))
    coef = np.random.standard_normal(5)
    y = predict_proba(coef, X) > 0.5

    # Fit a logistic regression model to the X and y vector
    # Fill in your code here.
    # Create a logistic regression object and fit it to the dataset

    lr_model = LogisticRegression(max_iter=50)
    lr_model.fit(X, y)
    # Print performance information
    print(f"Accuracy: {lr_model.score(X, y)}")
    print(f"True coefficients: {coef}")
    print(f"Learned coefficients: {lr_model.coef_}")
