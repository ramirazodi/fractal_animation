import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap


def julia(c, z, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


def julia_set(c, xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return np.array([[julia(c, complex(r, i), max_iter) for r in r1] for i in r2])


def update(frame_number, radius, theta_delta, max_iter, width, height):
    theta = frame_number * theta_delta
    c = radius * np.exp(2 * np.pi * 1j * theta)
    julia_image = julia_set(c, xmin, xmax, ymin, ymax, width, height, max_iter)
    ax.clear()
    ax.imshow(julia_image, extent=[xmin, xmax, ymin, ymax], cmap=cmap, origin='lower')
    ax.axis('off')
    # Display the c value with padding and custom font size
    ax.set_title(f"Complex Number = {c.real:.2f} + {c.imag:.2f}i", pad=15, fontsize=12,
                 color='white')
    return ax,

# Color map
n_bins = 100
colors = [(0, 0, 0),  # Pure black
          (0, 206/255 + 0.2, 209/255 + 0.2),  # Brighter turquoise
          (64/255 + 0.2, 224/255 + 0.2, 208/255 + 0.2)]  # Very light turquoise
cmap = LinearSegmentedColormap.from_list("turquoise_very_bright", colors, N=n_bins)

# Image parameters
zoom = 1.3
width, height = 1000, 1000
max_iter = 200
frames = 500  # Number of frames in the animation
radius = 0.8    # Radius for 'c' in the complex plane #0.7885
theta_delta = 0.0037  # Change in theta per frame (controls rotation speed)
x_center, y_center = 0.0, 0.0
x_width, y_height = 3.5 * zoom, 2.0 * zoom
xmin, xmax = x_center - x_width / 2, x_center + x_width / 2
ymin, ymax = y_center - y_height / 2, y_center + y_height / 2

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 12))
fig.patch.set_facecolor('#000000')
ax.set_facecolor('#000000')
plt.tight_layout()

# Animate plot
ani = animation.FuncAnimation(fig, update, frames=frames, fargs=(radius, theta_delta, max_iter, width, height), repeat=False)

# Save the animation as a GIF
dpi = 120
ani.save('julia_rotation.gif', writer='imagemagick', fps=35, dpi=dpi)

plt.close(fig)
