import matplotlib.pyplot as plt

def visualize(results):
    """Visualizes the negotiation outcomes using matplotlib."""
    for _, m in enumerate(results.mechanisms):
        plot_result(m)

def plot_result(m):
    """Plots the results of the negotiation."""
    m.plot(save_fig=False)
    plt.show()
    plt.close()
