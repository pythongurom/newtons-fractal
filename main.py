import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt


MAX_ITERATION = 1200
PRECISION = complex(1.e-9, 1.e-9)
TOLERANCE = complex(1.e-3, 1.e-3)
RESOLUTION = (2000, 2000)
SIZE = (1, 1)


# some test function
def f(z: complex) -> complex:
    return z**3 - 1

# and it's derivative
def df(z: complex) -> complex:
    return 3*(z**2)

def newtons_method(f, df, start_z: complex) -> complex:
    z = start_z
    for i in range(MAX_ITERATION): # limit iteration to speed up everything
        guess = f(z)/df(z)
        if abs(guess.real) < PRECISION.real and abs(guess.imag) < PRECISION.imag:
            return z
        z -= guess
    return False

# func that index all of the roots
def index_of_root(roots: list, root: complex):
    if len(roots) == 0:
        roots.append(root)
        return len(roots) - 1
    for i, r in enumerate(roots):
        if abs(root.real - r.real) < TOLERANCE.real and abs(root.imag - r.imag) < TOLERANCE.imag:
            return i
    roots.append(root)
    return len(roots) - 1

def map_nums():
    roots, matrix = [], np.zeros((SIZE[0] * RESOLUTION[0], SIZE[1] * RESOLUTION[1]))
    for i, x in enumerate(np.linspace(-SIZE[0]/2, SIZE[0]/2, RESOLUTION[0])): # numpy solves everything <3
        for j, y in enumerate(np.linspace(-SIZE[1]/2, SIZE[1]/2, RESOLUTION[1])):
            matrix[j][i] = index_of_root(roots, newtons_method(f, df, complex(x, y)))
    return matrix

def plot_test(matrix: np.ndarray, colors):
    plt.imshow(matrix, cmap=matplotlib.colors.ListedColormap(colors))
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    m = map_nums()
    print(m, m.max())
    plot_test(m, ["#228da7", "#4da551", "#3b5188"])
