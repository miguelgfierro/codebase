import pandas as pd
from matplotlib import pyplot as plt


def _importance_dataframe(importances, features):
    """Helper function to create a dataframe with the importance of each feature"""
    importance_frame = pd.DataFrame(
        {"Importance": list(importances), "Feature": features}
    )
    importance_frame.sort_values(by="Importance", inplace=True)
    return importance_frame


def draw_feature_importance(importances, features, output_file="output.png"):
    """Draw the feature importance as a bar chart in an output file
    
    Args:
        importances (np.array): Array with the importances.
        features (list): List of the features which corresponds to `importances` array.
        output_file (str): Filename of the output chart
    """
    importance_frame = _importance_dataframe(importances, features)
    importance_frame.plot(kind="barh", x="Feature", figsize=(8, 8), color="green")
    plt.tight_layout()
    plt.savefig(output_file)


def plot_feature_importance(importances, features):
    """Plot the feature importance as a bar chart
    
    Args:
        importances (np.array): Array with the importances.
        features (list): List of the features which corresponds to `importances` array.
    """
    importance_frame = _importance_dataframe(importances, features)
    importance_frame.plot(kind="barh", x="Feature", figsize=(8, 8), color="green")
