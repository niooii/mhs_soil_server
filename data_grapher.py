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

index: int = 0

# Making random z data points
for i in range(0, 25):
    zVals.append(0)

# Generalizing x and y
sideLen = int(np.sqrt(len(zVals)))
xVals = np.linspace(1, sideLen, sideLen)
yVals = np.linspace(1, sideLen, sideLen)
X, Y = np.meshgrid(xVals, yVals)


def update_plot(goodness: float, init: bool):
    global plot_b64_data
    global index;
    global zVals

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim(0,1)

    ax.set_title(f'Farmland Potential (coord {(index)%5+1}, {int(index/5)+1})') 
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # ax.set_zlabel('Soil Healthy')

    zVals[index] = goodness  # Increased range for more noticeable changes
    if not init:
        index += 1
    if index >= sideLen * sideLen:
        index = 0
    # for i in range(0, 16):
    #         zVals[i] = random.randint(0, 20)

    ax.plot_surface(X, Y, np.array(zVals).reshape(sideLen, sideLen), rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    stream = io.BytesIO()
    plt.savefig(stream, format='jpg')
    stream.seek(0)
    old_plot_data = plot_b64_data
    plot_b64_data = base64.b64encode(stream.read()).decode()

    plt.close(fig)


    #def save_plot_image():
    #with open("plot.jpg", "a") as x:
    #    pass

    #with open("plot.jpg", "wb") as file:
    #    file.write(base64.decodebytes(plot_b64_data.encode()))

    #print("saved plot image")

# returns binary data encoded in base 64 for the plot image in jpg form
def get_plot_data():
    global plot_b64_data
    return plot_b64_data
