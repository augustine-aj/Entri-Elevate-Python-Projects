import numpy as np


class MultivariateLinearRegression:

    def __init__(self, learning_rate=.01, epoch=10000):
        self.learning_rate = learning_rate
        self.epochs = epoch
        self.theta = None

    def hypothesis(self, x):  # h(x) = theta transpose x
        return np.dot(x, self.theta)

    def compute_cost(self, x, y):
        m = len(y)
        y_predict = self.hypothesis(x)
        cost = (1 / (2 * m) * np.sum(y_predict - y) ** 2)
        return cost

    def fit(self, x, y):
        m, n = x.shape
        x = np.concatenate([np.ones((m, 1)), x], axis=1)
        self.theta = np.zeros(n + 1)
        for epoch in range(self.epochs):
            y_predict = self.hypothesis(x)
            errors = y_predict - y
            gradient = (1 / m) * np.dot(x.T, errors)
            self.theta -= self.learning_rate * gradient

            if epoch % 1000 == 0:
                cost = self.compute_cost(x, y)
                print(f'{epoch = }, {cost = }, {self.theta = }')

    def predict(self, x):
        m = x.shape[0]
        x = np.concatenate([np.ones((m, 1)), x], axis=1)
        return self.hypothesis(x)


if __name__ == '__main__':
    x = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([5, 7, 9, 11, 13])

    model = MultivariateLinearRegression()
    model.fit(x, y)

    x_new = np.array([[6, 7], [7, 8]])
    y_new = model.predict(x_new)
    print('Predicted value : ', y_new)
