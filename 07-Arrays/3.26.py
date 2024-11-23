import matplotlib.pyplot as plt
import math
degrees = range(0,361)
radians = [math.radians(degree) for degree in degrees]
y = [math.sin(radian) for radian in radians]
plt.plot(radians,y)
plt.show()
