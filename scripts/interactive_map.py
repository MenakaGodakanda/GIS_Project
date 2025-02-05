import geopandas as gpd
import folium

# Load data
points_gdf = gpd.read_file("data/points.geojson")
polygons_gdf = gpd.read_file("data/polygons.geojson")

# Initialize the map centered at an arbitrary location
m = folium.Map(location=[0, 0], zoom_start=2)

# Add polygons
for _, row in polygons_gdf.iterrows():
    folium.GeoJson(row["geometry"], style_function=lambda x: {"color": "blue"}).add_to(m)

# Add points
for _, row in points_gdf.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=f"Point: ({row.geometry.x}, {row.geometry.y})",
        icon=folium.Icon(color="red")
    ).add_to(m)

# Save map to HTML
m.save("outputs/interactive_map.html")
print("Interactive map saved successfully!")

