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
        print("\nTraining neural network")
        sleep(1)
        return "model trained on " + dataset

    def _compute_acc(self, model, dataset):
        return 0.42


@pytest.fixture()
def nn5():
    return NeuralNetwork(n_layers=5)


@pytest.fixture(scope="function")
def train_scope_function():
    nn = NeuralNetwork(2)
    nn.train("dataset1")
    return nn


@pytest.fixture(scope="module")
def train_scope_module():
    nn = NeuralNetwork(2)
    nn.train("dataset1")
    return nn


@pytest.fixture(scope="module")
def load_dataset():
    filename = "share/traj.txt"
    with open(filename, "r") as f:
        data = [line.rstrip() for line in f.readlines()]
    yield data
    print("Tear down the fixture, with data: {}".format(data))

