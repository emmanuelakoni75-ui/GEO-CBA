# Creating tornado path map from coordinate pairs

import matplotlib.pyplot as plt
import os

# Use a clean plotting style
plt.style.use('seaborn-v0_8-whitegrid')

# Coordinate data: start_lat, start_lon, end_lat, end_lon
coordinates = [
    (36.059, -98.644, 36.064, -98.634),
    (36.064, -98.634, 36.165, -98.578),
    (35.35, -98.441, 35.413, -98.311),
    (36.165, -98.578, 36.235, -98.583),
    (36.236, -98.507, 36.244, -98.5),
    (35.444, -98.287, 35.725, -97.697),
    (35.622, -97.856, 35.618, -97.837),
    (35.725, -97.697, 35.747, -97.674),
    (35.747, -97.674, 35.921, -97.356),
    (35.008, -97.961, 35.189, -97.67),
    (34.88, -97.732, 34.939, -97.67),
    (34.939, -97.67, 35.141, -97.491),
    (35.189, -97.67, 35.305, -97.589),
    (35.242, -97.628, 35.243, -97.619),
    (36.034, -97.163, 36.108, -97.013),
    (35.305, -97.589, 35.311, -97.571),
    (35.109, -97.451, 35.116, -97.447),
    (35.373, -97.131, 35.387, -97.108),
    (36.4103, -96.5812, 36.4429, -96.551),
    (36.465, -96.576, 36.6759, -96.4231),
    (34.252, -96.76, 34.274, -96.67),
    (35.7631, -95.7423, 35.8377, -95.6423),
    (35.8377, -95.6423, 35.8554, -95.6023),
    (35.942, -95.3754, 35.9533, -95.2978),
    (36.2264, -94.9542, 36.2693, -94.8406),
    (35.0021, -95.2106, 35.0238, -95.1758),
    (36.2757, -94.7575, 36.3294, -94.6728),
    (34.6942, -95.0378, 34.7041, -95.0144),
    (34.8256, -94.7248, 34.9673, -94.6047),
    (35.44, -94.4595, 35.4493, -94.441),
    (36.9806, -101.0535, 36.9759, -101.0159),
    (36.77, -100.82, 36.7695, -100.8183),
    (36.3568, -99.88, 36.3568, -99.88),
    (36.9614, -96.5458, 36.9614, -96.5458),
    (36.9231, -96.2885, 36.9231, -96.2885)
]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 8))
for start_lat, start_lon, end_lat, end_lon in coordinates:
    ax.plot([start_lon, end_lon], [start_lat, end_lat], marker='o', linewidth=2)

ax.set_title("Tornado Paths (Start to End Coordinates)", fontsize=14)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.grid(True)
ax.set_aspect('equal', adjustable='box')

# Save the plot
output_path = "/mnt/data/tornado_paths_map.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print("Generated tornado path map and saved as tornado_paths_map.png")