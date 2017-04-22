from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, f1_score, log_loss, precision_score, recall_score


def classification_metrics_binary(y_true, y_pred):
    """
    Returns a report with different metrics:
    Accuracy:
    Confusion matrix: C_ij where observations are known to be in group i but predicted to be in group j. In binary
    classification true negatives is C_00, false negatives is C_10, true positives is C_11 and false positives is C_01.
    Parameters:
        y_true
        y_pred
    Examples:
        >>> y_true = [0,1,0,0,1]
        >>> y_pred = [0,1,0,1,1]
        >>> classification_metrics_binary(y_true, y_pred)
        {'Recall': 1.0, 'F1': 0.80000000000000004, 'Confusion Matrix': array([[2, 1],
               [0, 2]]), 'Precision': 0.66666666666666663, 'Accuracy': 0.80000000000000004}

    """
    m_acc = accuracy_score(y_true, y_pred)
    m_f1 = f1_score(y_true, y_pred)
    m_precision = precision_score(y_true, y_pred)
    m_recall = recall_score(y_true, y_pred)
    m_conf = confusion_matrix(y_true, y_pred)
    report = {'Accuracy':m_acc, 'Precision':m_precision, 'Recall':m_recall, 'F1':m_f1, 'Confusion Matrix':m_conf}
    return report