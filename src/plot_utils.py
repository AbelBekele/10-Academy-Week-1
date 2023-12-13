import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

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

def plot_time_series(data, time_column, title, x_label, y_label, color='skyblue'):
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
    - color: str, optional
        Color for the plot.

    Returns:
    - None
    """
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data.resample('D').size(), color=color, marker='o')
    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def plot_countplot(data, x_column, title, x_label, rotation=45, color='skyblue'):
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
    - color: str, optional
        Color for the plot.

    Returns:
    - None
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(x=data[x_column], color=color)
    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=14)
    plt.xticks(rotation=rotation, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def create_table(table_data):
    """
    Create a table using Plotly.

    Parameters:
    - table_data: DataFrame
        Data for the table.

    Returns:
    - None
    """
    table = go.Figure(data=[go.Table(
        header=dict(values=list(table_data.columns),
                    fill_color='lightblue',
                    align='center',
                    font=dict(color='black', size=14)),
        cells=dict(values=[table_data['Handset Manufacturer'], table_data['Handset Type'], table_data['count']],
                   fill=dict(color=['white', 'lightcyan', 'lightcyan']),
                   align='center',
                   font=dict(color='black', size=12)))
    ])

    table.update_layout(width=800, height=400, margin=dict(l=0, r=0, t=0, b=0))

    table.show()