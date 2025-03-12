# Delhi Bus and Metro Transit Map

## Overview
This project provides an interactive transit map for Delhi, displaying bus stops and metro stations using **Folium** and **Flask**. It allows users to explore Delhi's public transportation system with key features such as real-time location tracking and detailed information on stops.

## Features
- 📍 **Interactive Map** powered by Leaflet.js and Folium.
- 🚏 **Bus Stop Markers** loaded dynamically from a JSON dataset.
- 🚇 **Delhi Metro Network** displayed via GeoJSON overlays.
- 🏙 **Delhi Boundary Layer** for contextual reference.
- 🔍 **Clustered Markers** for better visibility of bus stops.
- 📡 **Find My Location** feature for users to locate themselves on the map.
- 🖥 **Flask Web App** for serving the interactive map.

## Project Structure
```
📂 Project Root
├── 📂 templates
│   ├── map.html           # Main HTML file for rendering the interactive map
│   ├── map_base.html      # Base map template generated dynamically
├── 📂 static              # Static assets (CSS, JS, images if needed)
├── delhi_boundary.geojson # GeoJSON file for Delhi administrative boundary
├── delhi_metro_lines.geojson # GeoJSON file containing Delhi Metro routes
├── delhi_metro_stations.geojson # GeoJSON file for Metro station points
├── bus_stops_delhi.json   # JSON dataset of bus stops with metadata
├── app.py                 # Flask application to render the map
├── README.md              # Project documentation (this file)
└── requirements.txt       # Dependencies for the project
```

## Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/delhi-transit-map.git
cd delhi-transit-map
```

### 2️⃣ Create a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App
```sh
python app.py
```
The application will be accessible at `http://127.0.0.1:5000/`.

## Usage
1. Open `http://127.0.0.1:5000/` in your browser.
2. Explore the bus stops and metro stations using the interactive map.
3. Click on markers to view detailed information about transit stops.
4. Use the "Find My Location" button to locate yourself on the map.

## Dependencies
- **Flask** (For serving the web application)
- **Folium** (For generating interactive maps)
- **Leaflet.js** (For map rendering in the frontend)
- **Bootstrap & jQuery** (For UI enhancements)

## Contributing
1. Fork the repository 📌
2. Create a feature branch 🔀 (`git checkout -b feature-xyz`)
3. Commit your changes 📝 (`git commit -m 'Add feature xyz'`)
4. Push to the branch 🚀 (`git push origin feature-xyz`)
5. Create a Pull Request 🔄

## License
This project is licensed under the **MIT License**.

## Acknowledgements
- **OpenStreetMap contributors** for providing the base map tiles.
- **Delhi Transport Corporation (DTC) & Metro data sources** for transit information.
- **Folium & Leaflet.js** for mapping functionalities.
