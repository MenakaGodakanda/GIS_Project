# GIS Project - Simulated Geospatial Data Visualization

This project demonstrates the use of **open-source GIS tools** to generate, visualize, and interact with simulated geospatial data. It creates random **points** and **polygons**, visualizes them as a **static map (Matplotlib)** and an **interactive web-based map (Folium)**.

## Overview
<img width="1017" alt="Screenshot 2025-02-05 at 4 23 46 pm" src="https://github.com/user-attachments/assets/88f79403-6c76-46d6-87ba-e78df0038b17" />

### Explanation
#### 1. Generate Simulated GIS Data (`generate_data.py`)
- Creates random points
- Creates random polygons
- Saves data as `GeoJSON`

#### 2. Visualize Static Map - Matplotlib (`plot_static_map.py `)
- Reads GeoJSON files
- Plots points & polygons
- Saves `static_map.png`

#### 3. Create Interactive Map - Folium (`interactive_map.py `)
- Reads GeoJSON files
- Creates interactive map
- Saves `interactive_map.html`

#### 4. View Outputs
- `static_map.png` (image)
- `interactive_map.html` (web)

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
### 3. Create a Virtual Environment
```
python3 -m venv gis
source gis/bin/activate
```

### 4. Install Required Libraries
```
pip install geopandas matplotlib folium shapely fiona pyproj
```
- **Geopandas**: Handles geospatial data in Pandas-like DataFrames.
- **Matplotlib**: Used for static map plotting.
- **Folium**: Creates interactive web-based maps.
- **Shapely**: Works with geometric objects.
- **Fiona & Pyproj**: Helps with geospatial data handling and projections.
![Screenshot 2025-02-05 151414](https://github.com/user-attachments/assets/c513e8e3-221d-4c18-927e-f569cded147e)

## Running the Project
### 1. Generate GIS Data
- `generate_data.py` will generate random geospatial data.
```
python3 scripts/generate_data.py
```
![Screenshot 2025-02-05 151558](https://github.com/user-attachments/assets/89192e9d-c0f1-4265-9350-03b213e13128)

- This creates `points.geojson` and `polygons.geojson` in the `data/` folder.
![Screenshot 2025-02-05 151606](https://github.com/user-attachments/assets/67b1867d-6cb5-4419-9a64-5fb5b027f9ce)

- `points.geojson`: Contains randomly generated points.
- Example content of `points.geojson`:
![Screenshot 2025-02-05 151624](https://github.com/user-attachments/assets/aee69095-47e5-4120-96bb-206ed6d8bf0a)

- `polygons.geojson`: Contains randomly generated polygons.
- Example content of `polygons.geojson`:
![Screenshot 2025-02-05 151633](https://github.com/user-attachments/assets/ef55dceb-0cb4-4954-a131-3c20d0e5288e)

### 2. Create Static Map
```
python3 scripts/plot_static_map.py
```
- This generates `outputs/static_map.png` (visualizing points & polygons).
  - Polygons in light blue with black borders.
  - Points in red.
![Screenshot 2025-02-05 151726](https://github.com/user-attachments/assets/79538f52-10b2-4c9e-ab94-773a1114d82c)

### 3. Create Interactive Map
- For an interactive map, use `folium`.
```
python3 scripts/interactive_map.py
```
![Screenshot 2025-02-05 152355](https://github.com/user-attachments/assets/e19b5954-dad9-495f-adab-3b901ac5c1fd)

- This creates `outputs/interactive_map.html`, which can be opened in a browser.
  - A world map centered at (0,0).
  - Random polygons displayed as blue shapes.
  - Points represented by red markers.
  - Clicking a point shows coordinates in a popup.

![Screenshot 2025-02-05 152406](https://github.com/user-attachments/assets/709039e7-a785-48a3-95de-d1b537fa0738)
![Screenshot 2025-02-05 154359](https://github.com/user-attachments/assets/cf4310b6-c821-4607-93bc-682d1eeeb57e)

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
