import itertools
import numpy as np
import matplotlib.pyplot as plt


def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    """Plots a confusion matrix.
    Args:
        cm (numpy array): The confusion matrix array.
        classes (list): List wit the classes names.
        normalize (bool): Flag to normalize data.
        title (str): Title of the plot.
        cmap (matplotlib.cm): Matplotlib colormap https://matplotlib.org/api/cm_api.html
    Examples:
        >>> import numpy as np
        >>> a = np.array([[10, 3, 0],[1, 2, 3],[1, 5, 9]])
        >>> classes = ['cl1', 'cl2', 'cl3']
        >>> plot_confusion_matrix(a, classes, normalize=False)
        >>> plot_confusion_matrix(a, classes, normalize=True)

    """
    cm_max = cm.max()
    cm_min = cm.min()
    if cm_min > 0: cm_min = 0
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        cm_max = 1
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    thresh = cm_max / 2.
    plt.clim(cm_min, cm_max)

    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i,
                 round(cm[i, j], 3),  # round to 3 decimals if they are float
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
