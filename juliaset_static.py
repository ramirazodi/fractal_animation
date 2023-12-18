import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def julia(c, z, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def julia_set(c, xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return np.array([[julia(c, complex(r, i), max_iter) for r in r1] for i in r2])

# Color map
n_bins = 100
colors = [(0, 0, 0),  # Pure black
          (0, 206/255 + 0.2, 209/255 + 0.2),  # Brighter turquoise
          (64/255 + 0.2, 224/255 + 0.2, 208/255 + 0.2)]  # Very light turquoise
cmap = LinearSegmentedColormap.from_list("turquoise_very_bright", colors, N=n_bins)

# Adjust these variables to control the zoom and pan
zoom = 0.9
left_right = 0
up_down = 0.0

# Julia set parameter - try different values to explore different patterns
c = complex(-0.4, 0.6)

# Adjusted parameters for zoom and pan
x_center, y_center = left_right, up_down
x_width, y_height = 3.5 * zoom, 2.0 * zoom
xmin, xmax = x_center - x_width / 2, x_center + x_width / 2
ymin, ymax = y_center - y_height / 2, y_center + y_height / 2

width, height = 1200, 1200
max_iter = 200

julia_image = julia_set(c, xmin, xmax, ymin, ymax, width, height, max_iter)

# Plotting with dark background and custom colormap
plt.style.use('dark_background')
plt.imshow(julia_image, extent=[xmin, xmax, ymin, ymax], cmap=cmap, origin='lower')
plt.title("Julia Set", pad=20)
plt.axis('off')
plt.tight_layout()
plt.show()
