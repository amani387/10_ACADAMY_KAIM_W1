import matplotlib.pyplot as plt

def plot_stock_data(data, column, label):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data[column], label=label)
    plt.title(label)
    plt.xlabel("Date")
    plt.ylabel(label)
    plt.legend()
    plt.show()

def plot_correlation_scatter(data, x_col, y_col):
    data.plot.scatter(x=x_col, y=y_col, title=f"Correlation: {x_col} vs {y_col}")
    plt.show()
