# GIS Project - Simulated Geospatial Data Visualization

This project demonstrates the use of **open-source GIS tools** to generate, visualize, and interact with simulated geospatial data. It creates random **points** and **polygons**, visualizes them as a **static map (Matplotlib)** and an **interactive web-based map (Folium)**.

## Features

- Generates Random GIS Data (Points & Polygons)
- Static Map Visualization using Matplotlib
- Interactive Map using Folium
- Open-source GIS libraries (Geopandas, Shapely, Fiona, Pyproj)

## Installation & Setup
### 1. Install Required Packages (Ubuntu)
```
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Clone Repository
```
git clone https://github.com/MenakaGodakanda/GIS_Project.git
cd GIS_Project
```

### 3. Install Required Libraries
```
pip install geopandas matplotlib folium shapely fiona pyproj
```
- **Geopandas**: Handles geospatial data in Pandas-like DataFrames.
- **Matplotlib**: Used for static map plotting.
- **Folium**: Creates interactive web-based maps.
- **Shapely**: Works with geometric objects.
- **Fiona & Pyproj**: Helps with geospatial data handling and projections.

## Running the Project
### 1. Generate GIS Data
- `generate_data.py` will generate random geospatial data.
```
python3 scripts/generate_data.py
```
- This creates `points.geojson` and `polygons.geojson` in the `data/` folder.
- `points.geojson`: Contains randomly generated points.
- Example content of `points.geojson`:
- `polygons.geojson`: Contains randomly generated polygons.
- Example content of `polygons.geojson`:

### 2. Create Static Map
```
python3 scripts/plot_static_map.py
```
- This generates `outputs/static_map.png` (visualizing points & polygons).
  - Polygons in light blue with black borders.
  - Points in red.

### 3. Create Interactive Map
- For an interactive map, use `folium`.
```
python3 scripts/interactive_map.py
```
- This creates `outputs/interactive_map.html`, which can be opened in a browser.
  - A world map centered at (0,0).
  - Random polygons displayed as blue shapes.
  - Points represented by red markers.
  - Clicking a point shows coordinates in a popup.

## Project Structure
```
GIS_Project/
│── data/                  # Stores generated GIS data
│   ├── points.geojson     # Random points
│   ├── polygons.geojson   # Random polygons
│
│── scripts/               # Contains Python scripts
│   ├── generate_data.py     # Generates random GIS data
│   ├── plot_static_map.py   # Plots static GIS map
│   ├── interactive_map.py   # Creates interactive map
│
│── outputs/               # Stores output files
│   ├── static_map.png       # Static GIS visualization
│   ├── interactive_map.html # Interactive GIS map
```

## License

This project is open-source under the MIT License.
