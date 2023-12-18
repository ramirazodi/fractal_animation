import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2])

# Custom turquoise colormap
colors = [(0, 0, 0), (0, 206/255, 209/255), (64/255, 224/255, 208/255)]
n_bins = 100  # Increase for finer color transitions
cmap = LinearSegmentedColormap.from_list("turquoise", colors, N=n_bins)

# Adjust these variables to control the zoom and pan
zoom = 0.9
left_right = 0
up_down = 0.0
x_center, y_center = -0.7 + left_right, 0.0 + up_down
x_width, y_height = 3.5 * zoom, 2.0 * zoom
xmin, xmax = x_center - x_width / 2, x_center + x_width / 2
ymin, ymax = y_center - y_height / 2, y_center + y_height / 2

width, height = 1000, 1000
max_iter = 200

mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

# Plotting with dark background and custom colormap
plt.style.use('dark_background')
plt.imshow(mandelbrot_image, extent=[xmin, xmax, ymin, ymax], cmap=cmap, origin='lower')
plt.title("Mandelbrot Set")
plt.axis('off')
plt.tight_layout()
plt.show()
