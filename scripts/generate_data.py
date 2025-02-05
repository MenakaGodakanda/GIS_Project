import geopandas as gpd
import random
from shapely.geometry import Point, Polygon

def generate_points(num_points=10, x_range=(-180, 180), y_range=(-90, 90)):
    """Generate random point geometries."""
    points = [Point(random.uniform(*x_range), random.uniform(*y_range)) for _ in range(num_points)]
    return gpd.GeoDataFrame(geometry=points, crs="EPSG:4326")

def generate_polygons(num_polygons=5):
    """Generate random polygons."""
    polygons = []
    for _ in range(num_polygons):
        center_x, center_y = random.uniform(-180, 180), random.uniform(-90, 90)
        offset = random.uniform(1, 5)
        polygon = Polygon([
            (center_x - offset, center_y - offset),
            (center_x + offset, center_y - offset),
            (center_x + offset, center_y + offset),
            (center_x - offset, center_y + offset),
            (center_x - offset, center_y - offset),
        ])
        polygons.append(polygon)

    return gpd.GeoDataFrame(geometry=polygons, crs="EPSG:4326")

if __name__ == "__main__":
    points_gdf = generate_points()
    polygons_gdf = generate_polygons()
    
    points_gdf.to_file("data/points.geojson", driver="GeoJSON")
    polygons_gdf.to_file("data/polygons.geojson", driver="GeoJSON")

    print("Simulated geospatial data generated successfully!")

