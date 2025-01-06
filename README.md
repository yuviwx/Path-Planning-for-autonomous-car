# Formula 1 home assignment - Path Planning

This repository contains code and solutions for **path planning task**.
For path planning I needed to express the route of the car in a continuous curve.
There are a lot of ways to plan a path. First of all I needed to check if the cones are regularly spaced - the standard deviation of the distances between cones is less than 10%.(both between sides and within sides)
If the above isn't satisfied - a Graph-Based Approach and Dijkstra algorithm is needed.
Unfortunately, the above is satisfied and i didn't get the chance to make a graph of the map and implement Dijkstra algorithm :(
My solution was very simple due to the convenience data given to me, and due to the arrangement of the cones.
The solution was to determine rigth Waypoints for the car and make a curve using cubic spline.(There is also a file containing my lagrange interpolation from my first attempt for a curve)

---

## Tasks
- Design a smooth path for a car to navigate between the cones.
- Optimize the path for minimal curvature while ensuring feasibility for vehicle navigation.
- Visualize your solution using 2D graphics.

---

## Tasks Overview

### cubic splines:
Cubic spline is a split continuous function where in each interval cubic polynomial function.
I chose this method since it's easy to implement and since creating such function there are requirments on the second derivative which represents curveture - 'path smoothness'.
So using this method I achived the first requirement for designing a smooth path for a car to navigate between the cones.

Next, to optimize the path for minimal curvature, Instead of interpolating 𝑦 as a function of 𝑥, the curve is described as (x = f(u), y = g(u)).
This approach allows us to control the curvature by uniformly creating u-values between 0 and 1 and it creates large amount of short distance tangent lines, that follow the curvature of the function.
Using try and error method I chose to split u into a 1000 points uniformaly, thus achieving minimal curvature and small deviation from the waypoints.

To Visualize my solution I used matplotlib library.

### For more strict path planning:
We can add least-squares method to achieve the following:
1. Minimize Deviation:
  Ensure the generated path stays close to the waypoints.

2. Enforce Smoothness:
  Minimize the second derivative (curvature) along the path.

3. Handle Constraints:
  Incorporate physical constraints, such as turning radius or trajectory feasibility.

In our case, we achieve (1) + (2) using 'u' alone.
Since there aren't any given constraints, (3) is not a required achievment.

