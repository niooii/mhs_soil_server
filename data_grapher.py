import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
from mpl_toolkits import mplot3d

# creating the axis
ax = plt.axes(projection="3d")

# https://stackoverflow.com/questions/61791309/how-to-make-a-3d-plot-x-y-z-assigning-z-values-to-x-y-ordered-pairs
# https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
zVals = []

def update_plot():
    # making a random z data points
    i = 0;
    step = 1;
    while i / step < 100:

        if i % 3 == 0:
            zVals.append(i + 20)
        elif i % 5 == 0:
            zVals.append(2 * i)
        else:
            zVals.append(i)
        i += step

    # generalizing x and y
    sideLen = int(np.sqrt(len(zVals)))
    xVals = np.linspace(1, sideLen, sideLen)
    yVals = np.linspace(1, sideLen, sideLen)

    X, Y = np.meshgrid(xVals, yVals)
    # X and Y is the dimensions of the room, Z is height
    # X, Y and Z are 2d arrays

    ax.plot_surface(X, Y, np.array(zVals).reshape(sideLen, sideLen), rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax.set_title('Soil Goodness yeah yep');
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('How good soil is')
    plt.show()

def animate(i, xs, ys, limit=0, verbose=False):
    # grab the data
    try:
        data = get_data(DATA_FILENAME, BUFFER_LEN)
        if verbose:
            print(data)
        x, y = map(float, data.split())
        if x > xs[-1]:
            # Add x and y to lists
            xs.append(x)
            ys.append(y)
            # Limit x and y lists to 10 items
            xs = xs[-limit:]
            ys = ys[-limit:]
        else:
            print(f"W: {time.time()} :: STALE!")
    except ValueError:
        print(f"W: {time.time()} :: EXCEPTION!")
    else:
        # Draw x and y lists
        ax.clear()
        ax.set_ylim([0, 1])
        ax.plot(xs, ys)