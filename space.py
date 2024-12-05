# This module checks if cones are regularly spaced or not in order to choose the best method for the path planning.


import pandas as pd
import numpy as np

df = pd.read_csv("BrandsHatchLayout.csv")

df = df.dropna(subset=["x", "y"])

left_cones = df[df["side"] == "left"].reset_index(drop=True)
right_cones = df[df["side"] == "right"].reset_index(drop=True)

### 1. Check Regularity Within Each Side ###
def check_within_side(cones):
    distances = []
    for i in range(len(cones) - 1):
        dx = cones.iloc[i + 1]["x"] - cones.iloc[i]["x"]
        dy = cones.iloc[i + 1]["y"] - cones.iloc[i]["y"]
        distance = np.sqrt(dx**2 + dy**2)
        distances.append(distance)
    avg_distance = np.mean(distances)
    std_deviation = np.std(distances)
    return distances, avg_distance, std_deviation

# Check left and right cones
left_distances, left_avg, left_std = check_within_side(left_cones)
right_distances, right_avg, right_std = check_within_side(right_cones)

### 2. Check Regularity Between Sides ###
# Ensure the same number of cones for pairing
min_length = min(len(left_cones), len(right_cones))
left_cones = left_cones.iloc[:min_length]
right_cones = right_cones.iloc[:min_length]

paired_distances = []
for i in range(len(left_cones)):
    dx = right_cones.iloc[i]["x"] - left_cones.iloc[i]["x"]
    dy = right_cones.iloc[i]["y"] - left_cones.iloc[i]["y"]
    distance = np.sqrt(dx**2 + dy**2)
    paired_distances.append(distance)
paired_avg = np.mean(paired_distances)
paired_std = np.std(paired_distances)

### Output Results ###
print("### Regularity Within Each Side ###")
print(f"Left Avg Distance: {left_avg:.2f}, Std Dev: {left_std:.2f}")
print(f"Right Avg Distance: {right_avg:.2f}, Std Dev: {right_std:.2f}")

print("\n### Regularity Between Sides ###")
print(f"Paired Avg Distance: {paired_avg:.2f}, Std Dev: {paired_std:.2f}")

# Check if cones are regularly spaced
threshold = 0.1  # 10% of the average distance
if left_std <= threshold * left_avg and right_std <= threshold * right_avg and paired_std <= threshold * paired_avg:
    print("\nCones are regularly spaced.")
else:
    print("\nCones are irregularly spaced.")
