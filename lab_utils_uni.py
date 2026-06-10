# lab_utils_uni.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from mpl_toolkits.mplot3d import Axes3D


def plt_intuition():
    """
    Visualize a simple cost function.
    """
    x = np.linspace(-10, 10, 200)
    y = (x - 3) ** 2

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, linewidth=2)
    plt.scatter([3], [0], s=100)
    plt.title("Cost Function Intuition")
    plt.xlabel("Parameter")
    plt.ylabel("Cost")
    plt.grid(True)
    plt.show()


def plt_stationary():
    """
    Demonstrate stationary points.
    """
    x = np.linspace(-4, 4, 500)
    y = x**4 - 4*x**2

    plt.figure(figsize=(8, 5))
    plt.plot(x, y)

    stationary_x = [0, np.sqrt(2), -np.sqrt(2)]
    stationary_y = [sx**4 - 4*sx**2 for sx in stationary_x]

    plt.scatter(stationary_x, stationary_y, s=100)

    plt.title("Stationary Points")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()


def plt_update_onclick():
    """
    Interactive plot that updates on mouse click.
    """

    fig, ax = plt.subplots(figsize=(8, 5))

    x = np.linspace(-10, 10, 200)
    y = (x - 2) ** 2

    ax.plot(x, y)
    point, = ax.plot([], [], "ro", markersize=10)

    ax.set_title("Click Anywhere")
    ax.grid(True)

    def onclick(event):
        if event.xdata is None:
            return

        px = event.xdata
        py = (px - 2) ** 2

        point.set_data([px], [py])
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("button_press_event", onclick)

    plt.show()


def soup_bowl():
    """
    3D bowl-shaped surface used in gradient descent intuition.
    """

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)

    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2

    ax.plot_surface(X, Y, Z)

    ax.set_title("Gradient Descent Cost Surface")
    ax.set_xlabel("w")
    ax.set_ylabel("b")
    ax.set_zlabel("Cost")

    plt.show()
