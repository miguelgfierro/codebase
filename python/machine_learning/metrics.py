from sklearn.metrics import (confusion_matrix, accuracy_score, roc_auc_score, f1_score, log_loss, precision_score,
                             recall_score, mean_squared_error, mean_absolute_error, r2_score)
import numpy as np


def classification_metrics_binary(y_true, y_pred):
    """Returns a report with different metrics for a binary classification problem.
    - Accuracy: Number of correct predictions made as a ratio of all predictions. Useful when there are equal number
    of observations in each class and all predictions and prediction errors are equally important.
    - Confusion matrix: C_ij where observations are known to be in group i but predicted to be in group j. In binary
    classification true negatives is C_00, false negatives is C_10, true positives is C_11 and false positives is C_01.
    - Precision: Number of true positives divided by the number of true and false positives. It is the ability of the
    classifier not to label as positive a sample that is negative.
    - Recall: Number of true positives divided by the number of true positives and false negatives. It is the ability
    of the classifier to find all the positive samples.
    High Precision and low Recall will return few positive results but most of them will be correct. 
    High Recall and low Precision will return many positive results but most of them will be incorrect.
    - F1 Score: 2*((precision*recall)/(precision+recall)). It measures the balance between precision and recall.
    Args:
        y_true (list or np.array): True labels.
        y_pred (list or np.array): Predicted labels (binary).
    Returns:
        report (dict): Dictionary with metrics.
    Examples:
        >>> from collections import OrderedDict
        >>> y_true = [0,1,0,0,1]
        >>> y_pred = [0,1,0,1,1]
        >>> result = classification_metrics_binary(y_true, y_pred)
        >>> OrderedDict(sorted(result.items()))
        OrderedDict([('Accuracy', 0.8), ('Confusion Matrix', array([[2, 1],
               [0, 2]])), ('F1', 0.8), ('Precision', 0.6666666666666666), ('Recall', 1.0)])

    """
    m_acc = accuracy_score(y_true, y_pred)
    m_f1 = f1_score(y_true, y_pred)
    m_precision = precision_score(y_true, y_pred)
    m_recall = recall_score(y_true, y_pred)
    m_conf = confusion_matrix(y_true, y_pred)
    report = {'Accuracy': m_acc, 'Precision': m_precision, 'Recall': m_recall, 'F1': m_f1, 'Confusion Matrix': m_conf}
    return report


def classification_metrics_multilabel(y_true, y_pred, labels):
    """Returns a report with different metrics for a multilabel classification problem.
    - Accuracy: Number of correct predictions made as a ratio of all predictions. Useful when there are equal number
    of observations in each class and all predictions and prediction errors are equally important.
    - Confusion matrix: C_ij where observations are known to be in group i but predicted to be in group j. In multilabel
    classification true predictions are in the diagonal and false predictions outside the diagonal.
    - Precision: Number of true positives divided by the number of true and false positives. It is the ability of the
    classifier not to label as positive a sample that is negative.
    - Recall: Number of true positives divided by the number of true positives and false negatives. It is the ability
    of the classifier to find all the positive samples.
    High Precision and low Recall will return few positive results but most of them will be correct. 
    High Recall and low Precision will return many positive results but most of them will be incorrect.
    - F1 Score: 2*((precision*recall)/(precision+recall)). It measures the balance between precision and recall.
    Args:
        y_true (list or np.array): True labels.
        y_pred (list or np.array): Predicted labels.
        labels (list): Label index or name.
    Returns:
        report (dict): Dictionary with metrics.
    Examples:
        >>> from collections import OrderedDict
        >>> y_true = [0,1,2,0,1]
        >>> y_pred = [0,1,0,1,1]
        >>> result = classification_metrics_multilabel(y_true, y_pred, [0,1,2])
        >>> OrderedDict(sorted(result.items()))
        OrderedDict([('Accuracy', 0.6), ('Confusion Matrix', array([[1, 1, 0],
               [0, 2, 0],
               [1, 0, 0]])), ('F1', 0.52), ('Precision', 0.4666666666666666), ('Recall', 0.6)])

    """
    m_acc = accuracy_score(y_true, y_pred)
    m_f1 = f1_score(y_true, y_pred, labels, average='weighted')
    m_precision = precision_score(y_true, y_pred, labels, average='weighted')
    m_recall = recall_score(y_true, y_pred, labels, average='weighted')
    m_conf = confusion_matrix(y_true, y_pred, labels)
    report = {'Accuracy': m_acc, 'Precision': m_precision, 'Recall': m_recall, 'F1': m_f1, 'Confusion Matrix': m_conf}
    return report


def classification_metrics_binary_prob(y_true, y_prob):
    """Returns a report with different metrics for a binary classification problem.
    - AUC: The Area Under the Curve represents the ability to discriminate between positive and negative classes. An
    area of 1 represent perfect scoring and an area of 0.5 means random guessing.
    - Log loss: Also called logistic regression loss or cross-entropy loss. It quantifies the performance by
    penalizing false classifications. Minimizing the Log Loss is equivalent to minimizing the squared error but using
    probabilistic predictions. Log loss penalize heavily classifiers that are confident about incorrect classifications.
    Args:
        y_true (list or np.array): True labels.
        y_prob (list or np.array): Predicted labels (probability).
    Returns:
        report (dict): Dictionary with metrics.
    Examples:
        >>> from collections import OrderedDict
        >>> y_true = [0,1,0,0,1]
        >>> y_prob = [0.2,0.7,0.4,0.3,0.2]
        >>> result = classification_metrics_binary_prob(y_true, y_prob)
        >>> OrderedDict(sorted(result.items()))
        OrderedDict([('AUC', 0.5833333333333333), ('Log loss', 0.6113513950783531)])
        >>> y_prob = [0.2,0.7,0.4,0.3,0.3]
        >>> result = classification_metrics_binary_prob(y_true, y_prob)
        >>> OrderedDict(sorted(result.items()))
        OrderedDict([('AUC', 0.75), ('Log loss', 0.5302583734567203)])

    """
    m_auc = roc_auc_score(y_true, y_prob)
    m_logloss = log_loss(y_true, y_prob)
    report = {'AUC': m_auc, 'Log loss': m_logloss}
    return report


def regression_metrics(y_true, y_pred):
    """Returns a report with different metrics for a regression problem.
    - Mean Squared Error: MSE is a risk metric corresponding to the expected value of the squared (quadratic) error.
    It has the disadvantage of heavily weighting outliers.
    - Mean Absolute Error: MAE is a risk metric corresponding to the expected value of the absolute error or L1 loss.
    Not as sensitive to outliers.
    - R Square: R2 is statistical measure of how close the data are to the fitted regression line. It's best possible
    score is 1.0 and it can be negative (because the model can be arbitrarily worse). A score of 0 means that the
    variables are not linearly correlated.
    - Root Mean Squared Error: RMSE is the square root of MSE. It also gives a relatively high weight to large errors.
    Args:
        y_true (list or np.array): True values.
        y_pred (list or np.array): Predicted values.
    Returns:
        report (dict): Dictionary with metrics.
    Examples:
        >>> from collections import OrderedDict
        >>> y_true = [5,1,0,7,1]
        >>> y_pred = [6,0.7,0.4,10,20]
        >>> result = regression_metrics(y_true, y_pred)
        >>> OrderedDict(sorted(result.items()))
        OrderedDict([('MAE', 4.74), ('MSE', 74.25), ('R2', -9.088315217391303), ('RMSE', 8.616843969807043)])
        >>> y_true = [5,1,0,7,1]
        >>> y_pred = [6,0.7,0.4,10,2]
        >>> result = regression_metrics(y_true, y_pred)
        >>> OrderedDict(sorted(result.items()))
        OrderedDict([('MAE', 1.1400000000000001), ('MSE', 2.25), ('R2', 0.6942934782608696), ('RMSE', 1.5)])

    """
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    report = {'MSE': mse, 'MAE': mae, 'R2': r2, 'RMSE': np.sqrt(mse)}
    return report


def precision_at_k(y_true, y_pred, k=None):
    """Precision at K.
    Args:
        y_true (list or np.array): True values.
        y_pred (list or np.array): Predicted values.
        k (int): Limit of predicted values.
    Returns:
        result (float): precision at k (max=1, min=0)
    Examples:
        >>> y_true = [5,1,0,7,2]
        >>> y_pred = [2,5,0,1,7]
        >>> precision_at_k(y_true, y_pred, k=3)
        1.0
        >>> y_true = np.array([5,1,0,7,2])
        >>> y_pred = np.array([9,0,8,1,7])
        >>> precision_at_k(y_true, y_pred, k=3)
        0.3333333333333333

    """
    predictions = y_pred[:k]
    num_hit = len(set(predictions).intersection(set(y_true)))
    return float(num_hit) / len(predictions)


def recall_at_k(y_true, y_pred, k=None):
    """Recall at K.
    Args:
        y_true (list or np.array): True values.
        y_pred (list or np.array): Predicted values.
        k (int): Limit of predicted values.
    Returns:
        result (float): recall at k (max=1, min=0)
    Examples:
        >>> y_true = [5,1,0,7,2]
        >>> y_pred = [2,5,0,1,7]
        >>> recall_at_k(y_true, y_pred, k=3)
        0.6
        >>> y_true = np.array([5,1,0,7,2])
        >>> y_pred = np.array([9,0,8,1,7])
        >>> recall_at_k(y_true, y_pred, k=3)
        0.2

    """
    predictions = y_pred[:k]
    num_hit = len(set(predictions).intersection(set(y_true)))
    return float(num_hit) / len(y_true)


def discounted_cumulative_gain(y_true, y_pred, k=None):
    """Discounted Cumulative Gain (DCG).
    Info: https://en.wikipedia.org/wiki/Discounted_cumulative_gain
    Args:
        y_true (list or np.array): True values.
        y_pred (list or np.array): Predicted values.
        k (int): Limit of predicted values.
    Returns:
        result (float): DCG
    Examples:
        >>> y_true = [5,1,0,7,2]
        >>> y_pred = [2,5,0,1,7]
        >>> discounted_cumulative_gain(y_true, y_pred, k=3)
        5.130929753571458
        >>> y_true = np.array([5,1,0,7,2])
        >>> y_pred = np.array([9,0,8,1,7])
        >>> discounted_cumulative_gain(y_true, y_pred, k=3)
        6.0

    """
    order = np.argsort(y_pred)[::-1]
    y_true = np.take(y_true, order[:k])
    return (y_true / np.log2(np.arange(y_true.shape[0]) + 2)).sum()


def exponential_discounted_cumulative_gain(y_true, y_pred, k=None):
    """Exponential Discounted Cumulative Gain (eDCG).
    Info: https://en.wikipedia.org/wiki/Discounted_cumulative_gain
    Args:
        y_true (list or np.array): True values.
        y_pred (list or np.array): Predicted values.
        k (int): Limit of predicted values.
    Returns:
        result (float): eDCG
    Examples:
        >>> y_true = [5,1,0,7,2]
        >>> y_pred = [2,5,0,1,7]
        >>> exponential_discounted_cumulative_gain(y_true, y_pred, k=3)
        19.130929753571458
        >>> y_true = np.array([5,1,0,7,2])
        >>> y_pred = np.array([9,0,8,1,7])
        >>> exponential_discounted_cumulative_gain(y_true, y_pred, k=3)
        32.0

    """
    order = np.argsort(y_pred)[::-1]
    y_true = np.take(y_true, order[:k])
    return ((2 ** y_true - 1) / np.log2(np.arange(y_true.shape[0]) + 2)).sum()


def normalized_discounted_cumulative_gain(y_true, y_pred, k=None):
    """Normalized Discounted Cumulative Gain (nDCG).
    Info: https://en.wikipedia.org/wiki/Discounted_cumulative_gain
    Args:
        y_true (list or np.array): True values.
        y_pred (list or np.array): Predicted values.
        k (int): Limit of predicted values.
    Returns:
        result (float): nDCG (max=1, min=0)
    Examples:
        >>> y_true = [5,1,0,7,2]
        >>> y_pred = [2,5,0,1,7]
        >>> normalized_discounted_cumulative_gain(y_true, y_pred, k=3)
        0.4599812921368268
        >>> y_true = np.array([5,1,0,7,2])
        >>> y_pred = np.array([9,0,8,1,7])
        >>> normalized_discounted_cumulative_gain(y_true, y_pred, k=3)
        0.537892328558952

    """
    return discounted_cumulative_gain(y_true, y_pred, k) / discounted_cumulative_gain(y_true, y_true, k)


def normalized_exponential_discounted_cumulative_gain(y_true, y_pred, k=None):
    """Normalized Exponential Discounted Cumulative Gain (neDCG).
    Info: https://en.wikipedia.org/wiki/Discounted_cumulative_gain
    Args:
        y_true (list or np.array): True values.
        y_pred (list or np.array): Predicted values.
        k (int): Limit of predicted values.
    Returns:
        result (float): neDCG (max=1, min=0)
    Examples:
        >>> y_true = [5,1,0,7,2]
        >>> y_pred = [2,5,0,1,7]
        >>> normalized_exponential_discounted_cumulative_gain(y_true, y_pred, k=3)
        0.1292116839006246
        >>> y_true = np.array([5,1,0,7,2])
        >>> y_pred = np.array([9,0,8,1,7])
        >>> normalized_exponential_discounted_cumulative_gain(y_true, y_pred, k=3)
        0.21950735175253772

    """
    return exponential_discounted_cumulative_gain(y_true, y_pred, k)/exponential_discounted_cumulative_gain(y_true, y_true, k)


def gini(y_true, y_pred):
    """Normalized Gini Coefficient.
    It is a measure of statistical dispersion intended to represent a measurement of inequality.
    Args:
        y (np.array): True values.
        p (np.array): Predicted values.
    Returns:
        e (float): Normalized Gini coefficient.
    Examples:
        >>> actual = np.array([0.3, 0.8, 0.1, 0.5])
        >>> pred1 = np.array([0.3, 0.8, 0.1, 0.5])
        >>> pred2 = pred1[::-1]
        >>> gini(actual, pred1)
        1.0
        >>> gini(actual, pred2)
        -1.0000000000000002
    """

    n_samples = y_true.shape[0]

    # sort rows on prediction column
    # (from largest to smallest)
    arr = np.array([y_true, y_pred]).transpose()
    true_order = arr[arr[:,0].argsort()][::-1,0]
    pred_order = arr[arr[:,1].argsort()][::-1,0]

    # get Lorenz curves
    l_true = np.cumsum(true_order) / np.sum(true_order)
    l_pred = np.cumsum(pred_order) / np.sum(pred_order)
    l_ones = np.linspace(1/n_samples, 1, n_samples)

    # get Gini coefficients (area between curves)
    g_true = np.sum(l_ones - l_true)
    g_pred = np.sum(l_ones - l_pred)

    # normalize to true Gini coefficient
    return g_pred / g_true


