import matplotlib.pyplot as plt
import numpy as np

# Question 1: Generate histogram of pdf of pixel intensity

# Load the image into an array: image
image = plt.imread('images/Unequalized_Hawkes_Bay_NZ.jpg')

# convert to grayscale for compatibility
image = image.mean(axis=2)

# Display image in top subplot using color map 'gray'
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image, cmap='gray')
# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Display a histogram of the pixels in the bottom subplot
plt.subplot(2,1,2)
plt.xlim((0,255))
plt.title('Normalized histogram')
plt.hist(pixels, bins=64, range=(0, 256), alpha=0.4, color='red', density=True)

# Display the plot
plt.show()

# Question 2: plot CDF against PDF of pixel intensities

# Load the image into an array: image
plt.figure()
# Display image in top subplot using color map 'gray'
plt.subplot(2, 1, 1)
plt.imshow(image, cmap='gray')
plt.title('Original image')
plt.axis('off')

# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Display a histogram of the pixels in the bottom subplot
plt.subplot(2, 1, 2)
pdf = plt.hist(pixels, bins=64, range=(0, 256), density=False,
               color='red', alpha=0.4)
plt.grid('off')

# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()

# Display a cumulative histogram of the pixels
cdf = plt.hist(pixels, bins=64, range=(0, 256),
               cumulative=True, density=True,
               color='blue', alpha=0.4)

# Specify x-axis range, hide axes, add title and display plot
plt.xlim((0, 256))
plt.grid('off')
plt.title('PDF & CDF (original image)')
plt.show()

# Question 3: EQUALIZE THE IMAGE USING LINEAR INTERPOLATION
plt.figure()
plt.subplot(2, 1, 1)

# Generate a cumulative histogram
cdf, bins, patches = plt.hist(pixels, bins=256, range=(0,256), density=True, cumulative=True)
new_pixels = np.interp(pixels, bins[:-1], cdf*255)  # use linear interpolation to map image pixels CDF to almost uniform CDF

# Reshape new_pixels as a 2-D array: new_image
new_image = new_pixels.reshape(image.shape)

# Display the new image with 'gray' color map
plt.title('Equalized image')
plt.axis('off')
plt.imshow(new_image, cmap='gray')

# Question 4: Generate histogram of equalized pixels pdf and cdf

# Generate a histogram of the new pixels

plt.subplot(2,1,2)
pdf = plt.hist(new_pixels, bins=64, range=(0,256), density=False,
               color='red', alpha=0.4)
plt.grid('off')

# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()
plt.xlim((0,256))
plt.grid('off')

# Add title
plt.title('PDF & CDF (equalized image)')

# Generate a cumulative histogram of the new pixels
cdf = plt.hist(new_pixels, bins=64, range=(0,256),
               cumulative=True, density=True,
               color='blue', alpha=0.4)
plt.show()

