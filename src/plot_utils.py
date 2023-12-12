import seaborn as sns
import matplotlib.pyplot as plt

def set_seaborn_style():
    """
    Set a custom Seaborn style.
    """
    sns.set(style="whitegrid")

def plot_histogram_kde(data, title, x_label, y_label, color='skyblue'):
    """
    Plot a histogram with KDE.

    Parameters:
    - data: Series or array-like
        Data to be plotted.
    - title: str
        Plot title.
    - x_label: str
        Label for the x-axis.
    - y_label: str
        Label for the y-axis.
    - color: str, optional
        Color for the plot.

    Returns:
    - None
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data, kde=True, color=color, edgecolor='black')
    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def plot_boxplot(data, title, x_label, color='lightcoral'):
    """
    Plot a boxplot.

    Parameters:
    - data: Series or array-like
        Data to be plotted.
    - title: str
        Plot title.
    - x_label: str
        Label for the x-axis.
    - color: str, optional
        Color for the plot.

    Returns:
    - None
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data, color=color)
    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def plot_time_series(data, time_column, title, x_label, y_label):
    """
    Plot a time series using Matplotlib.

    Parameters:
    - data: DataFrame
        Data containing a time series.
    - time_column: str
        Column representing the time.
    - title: str
        Plot title.
    - x_label: str
        Label for the x-axis.
    - y_label: str
        Label for the y-axis.

    Returns:
    - None
    """
    data[time_column] = pd.to_datetime(data[time_column])
    df_time_series = data.set_index(time_column)
    df_time_series.resample('D').size().plot()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def plot_countplot(data, x_column, title, x_label, rotation=45):
    """
    Plot a countplot using Seaborn.

    Parameters:
    - data: DataFrame
        Data to be plotted.
    - x_column: str
        Column for the x-axis.
    - title: str
        Plot title.
    - x_label: str
        Label for the x-axis.
    - rotation: int, optional
        Rotation angle for x-axis labels.

    Returns:
    - None
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(x=data[x_column])
    plt.title(title)
    plt.xlabel(x_label)
    plt.xticks(rotation=rotation)
    plt.show()
