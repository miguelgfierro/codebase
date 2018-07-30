import pytest
from time import sleep


class NeuralNetwork:
    def __init__(self, n_layers):
        self.name = "NN"
        self.n_layers = n_layers
        self.model = None

    def train(self, dataset):
        self.model = self._train_model(dataset)

    def compute_accuracy(self, dataset):
        return self._compute_acc(self.model, dataset)

    def _train_model(self, dataset):
        # code to train a model given a dataset
        sleep(1)
        return 'model trained on ' + dataset

    def _compute_acc(self, model, dataset):
        return 0.42


@pytest.fixture()
def nn5():
    return NeuralNetwork(n_layers=5)

