import geopandas as gpd
import matplotlib.pyplot as plt

# Load the generated data
points_gdf = gpd.read_file("data/points.geojson")
polygons_gdf = gpd.read_file("data/polygons.geojson")

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
polygons_gdf.plot(ax=ax, color="lightblue", edgecolor="black", alpha=0.5)
points_gdf.plot(ax=ax, color="red", markersize=50)

# Add labels
ax.set_title("Static GIS Map")
plt.savefig("outputs/static_map.png")
plt.show()

