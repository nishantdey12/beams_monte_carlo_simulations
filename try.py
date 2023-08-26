import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(n):
    """
    This function implements a Monte Carlo simulation for the n balls and n bins problem.

    Args:
      n: The number of balls.

    Returns:
      The ratio of n/n0, where n0 is the number of bins that don't contain any balls.
    """

    bins = [False] * n

    for i in range(n):
        bin = random.randrange(n)
        bins[bin] = True

    n0 = sum(bins)

    return n / n0


def main():

    n_values = [10, 100, 1000, 10000]
    ratios = []

    for n in n_values:
        ratio = monte_carlo_simulation(n)
        ratios.append(ratio)

    plt.plot(n_values, ratios)
    plt.xlabel("n")
    plt.ylabel("n/n0")
    plt.title("Ratio of n/n0 as a function of n")
    plt.show()


if __name__ == "__main__":
    main()
