import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-2,2,41)
v = np.linspace(-1, 1, 21)

# Generate 2-D arrays from u and v: X, Y
X,Y = np.meshgrid(u, v)

# Compute Z based on X and Y
Z = np.sin(3*np.sqrt(X**2 + Y**2))

# Create a filled contour plot with a color map of 'viridis'
plt.subplot(2,2,1)
plt.contourf(X,Y,Z,20, cmap='viridis')
plt.colorbar()
plt.title('Viridis')

# Create a filled contour plot with a color map of 'gray'
plt.subplot(2,2,2)
plt.contourf(X,Y,Z,20, cmap='gray')
plt.colorbar()
plt.title('Gray')

# Create a filled contour plot with a color map of 'autumn'
plt.subplot(2,2,3)
plt.contourf(X,Y,Z,20, cmap='autumn')
plt.colorbar()
plt.title('Autumn')

# Create a filled contour plot with a color map of 'winter'
plt.subplot(2,2,4)
plt.contourf(X,Y,Z,20, cmap='winter')
plt.colorbar()
plt.title('Winter')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()


# rescaling intensities (grayscale image)
# Load the image into an array: image
image = plt.imread('images/Unequalized_Hawkes_Bay_NZ.jpg')
# convert to grayscale
image = image.mean(axis=2)

# Extract minimum and maximum values from the image: pmin, pmax
pmin, pmax = image.min(), image.max()
print("The smallest & largest pixel intensities are %d & %d." % (pmin, pmax))

# Rescale the pixels: rescaled_image
rescaled_image = 256*(image - pmin) / (pmax - pmin)
print("The rescaled smallest & largest pixel intensities are %.1f & %.1f." %
      (rescaled_image.min(), rescaled_image.max()))

# Display the rescaled image
plt.subplot(1,2,1)
plt.title('rescaled image')
plt.axis('off')
plt.imshow(rescaled_image, cmap='gray')

plt.subplot(1,2,2)
plt.title('original')
plt.axis('off')
plt.imshow(image, cmap='gray')
plt.show()
