from sklearn.utils import shuffle

from exercices.dataset import Datasets
from exercices.visualize import show_samples, show_history, show_samples_with_label
import pandas


def test_show_images():
    sample_provider = Datasets.fashion_mnist()

    samples = [_ for _ in sample_provider()]
    samples = shuffle(samples, n_samples=25)

    show_samples(samples, 5, 5)
    # a figure should pop (showing a grid of digits)


# def test_show_images_with_label():
#     sample_provider = Datasets.mnist()
#
#     samples = [_ for _ in sample_provider()]
#     samples = shuffle(samples, n_samples=25)
#
#     show_samples_with_label(samples, 5, 5)
#     # a figure should pop (showing a grid of digits)


def test_show_history():
    history = pandas.read_csv('../resources/training_logs.csv')
    show_history(history)

    # a figure should pop (showing two curves)
