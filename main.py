MAX_ITERATION = 200
PRECISION = complex(0.0001, 0.0001)

def f(z):
    return z**3 - 1

def df(z):
    return 3*(z**2)

def newtons_method(f, df, x=0.1, y=0.1):
    x = complex(x, y)
    guess = f(x)
    while abs(guess.real) > PRECISION.real or abs(guess.imag) > PRECISION.imag:
        if df(x) == 0:
            return False
        x -= f(x)/df(x)
        guess = f(x)
    return x

def plot_test():
    import numpy as np
    import matplotlib.pyplot as plt

    plt.imshow(np.random.random((500, 500)))
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    print(newtons_method(f, df))
    plot_test()