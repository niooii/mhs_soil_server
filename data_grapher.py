import base64
import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import io
import time

from soil import SoilInfo

plot_b64_data = ""

# Initial z values
zVals = []

# Making random z data points
i = 0
step = 1
while i / step < 100:
    zVals.append(0)
    i += step

# Generalizing x and y
sideLen = int(np.sqrt(len(zVals)))
xVals = np.linspace(1, sideLen, sideLen)
yVals = np.linspace(1, sideLen, sideLen)
X, Y = np.meshgrid(xVals, yVals)


def update_plot(soil_info: SoilInfo, goodness: float):
    global plot_b64_data
    global zVals

    # Create a new figure and axis for each update
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_title(f'Soil Goodness yeah yep - {time.time()}')  # Add timestamp to ensure uniqueness
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('How good soil is')

    # Update zVals with new value
    zVals[soil_info.coord_x + soil_info.coord_y * sideLen] = goodness  # Increased range for more noticeable changes

    # Plot the updated surface
    ax.plot_surface(X, Y, np.array(zVals).reshape(sideLen, sideLen), rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')

    # Save the plot to a binary data string
    stream = io.BytesIO()
    plt.savefig(stream, format='jpg')
    stream.seek(0)
    old_plot_data = plot_b64_data
    plot_b64_data = base64.b64encode(stream.read()).decode()

    print(f"PLOT DATA: {plot_b64_data}")

    # Close the figure to avoid memory leaks
    plt.close(fig)


# returns binary data encoded in base 64 for the plot image in jpg form
def get_plot_data():
    global plot_b64_data
    return plot_b64_data
