import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev

# Preface: 
# The cones are regularly spaced - the standard deviation of the distances between cones is less than 10%.(both between sides and within sides)
# Therefore I will use - Waypoints + Interpolation + Least squares to plan a path.
# Unfortunately I won't get to work with the Graph-Based Approach and Dijkstra algorithm :(
# But at least I will get to implement Lagrange Interpolation and Least squares - gogo algebra 2
# Intead of Lagrange we'll use the cubic spline method 


# Load the CSV file
df = pd.read_csv('BrandsHatchLayout.csv')

# Create middle points between the cones - waypoints
right_cones = df[df['side'] == 'right']
left_cones = df[df['side'] == 'left']
waypoints = pd.DataFrame({
    'x': (left_cones['x'].values + right_cones['x'].values) / 2,
    'y': (left_cones['y'].values + right_cones['y'].values) / 2
})
# the first value is None
x = waypoints['x'][1:] #dropna
y = waypoints['y'][1:]

# Compute the coefficients of the spline
tck, u = splprep([x,y], s=0)

# Make u a function of x,y to prevent cases where x has multiple y values
# u_new contains 500 points in the range [0,1]
# The idea is to make evenly spaced intervals along the spline instead of using the intervals given to us by u, 
# and ensuring there are no "gaps" in the points. The higher the number of samples the more 'smooth' the curve is.
u_new = np.linspace(0, 1, 1000)

# Use splev to compute interpolated values
x_new, y_new = splev(u_new, tck)

# Plot the cones and the interpolated path
plt.scatter(df['x'], df['y'], color='blue', label='Cones')
plt.plot(x_new, y_new, '-', label='Spline Interpolation', color="orange")
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Path Plan')
plt.legend()
plt.grid(True)
plt.show()

