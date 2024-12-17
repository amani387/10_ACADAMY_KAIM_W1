import matplotlib.pyplot as plt

def plot_correlation_scatter(data, x_col, y_col, title):
    """Plot scatterplot of sentiment vs. stock returns."""
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_col], data[y_col], alpha=0.7)
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid()
    plt.show()
