import matplotlib.pyplot as plt
import numpy as np
x = np.array([0, 1, 2, 3])
y = np.array([3, 2, 1, 0])

print(plt.style.available)  # so many styles!
y_max = y.max()
x_max = x[y.argmax()]  # argmax returns the index of the max!
print("xmax {}, ymax {}".format(x_max, y_max))

plt.style.use('dark_background')
plt.annotate(text='maximum of line x + y = 3 for x in [0,3]',
             color='red',
             xy = (x_max, y_max),
             xytext=(x_max+0.2,y_max),
             arrowprops=dict(facecolor="white", width=1, headwidth=8, headlength=5))
plt.plot(x, y)
plt.show()

