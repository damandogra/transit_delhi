from flask import Flask, render_template, send_from_directory
import folium
import json
from folium.plugins import MarkerCluster

app = Flask(__name__)

# Serve static files (prank image)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/')
def index():
    # Create a map centered at Delhi
    start_coords = (28.64035, 77.22048)
    folium_map = folium.Map(location=start_coords, zoom_start=12)

    # Create FeatureGroup for bus stops
    bus_stops_layer = folium.FeatureGroup(name="Bus Stops").add_to(folium_map)
    marker_cluster = MarkerCluster().add_to(bus_stops_layer)

    # Load bus stop data
    with open('bus_stops_delhi.json') as f:
        data = json.load(f)

    # Add each bus stop as a marker with detailed popup info
    for element in data['elements']:
        lat = element['lat']
        lon = element['lon']
        tags = element.get('tags', {})
        
        name = tags.get('name', 'Unnamed Bus Stop')
        operator = tags.get('operator', 'Unknown')
        network = tags.get('network', 'N/A')
        wheelchair = tags.get('wheelchair', 'Unknown')
        shelter = tags.get('shelter', 'Unknown')
        tactile_paving = tags.get('tactile_paving', 'Unknown')
        departures_board = tags.get('departures_board', 'Not Available')
        
        popup_content = f"""
        <b>Bus Stop:</b> {name}<br>
        <b>Operator:</b> {operator}<br>
        <b>Network:</b> {network}<br>
        <b>Wheelchair Accessible:</b> {wheelchair}<br>
        <b>Shelter:</b> {shelter}<br>
        <b>Tactile Paving:</b> {tactile_paving}<br>
        <b>Departures Board:</b> {departures_board}<br>
        """

        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(marker_cluster)

    # Load and add the administrative boundary
    with open('delhi_boundary.geojson', "r", encoding="utf-8") as f:
        boundary_data = json.load(f)
    folium.GeoJson(
        boundary_data,
        name='Delhi Boundary',
        style_function=lambda x: {
            'fillOpacity': 0,
            'color': 'blue',
            'weight': 2
        }
    ).add_to(folium_map)

    # Load and add Delhi Metro Lines
    with open('delhi_metro_lines.geojson', "r", encoding="utf-8") as f:
        metro_lines = json.load(f)
    folium.GeoJson(
        metro_lines,
        name="Delhi Metro Lines",
        style_function=lambda x: {
            "color": "#87CEEB",
            "weight": 3,
            "opacity": 0.7
        }
    ).add_to(folium_map)

    # Create a FeatureGroup for metro stations
    metro_stations_layer = folium.FeatureGroup(name="Metro Stations").add_to(folium_map)

    # Load and add Metro Stations
    with open('delhi_metro_stations.geojson', "r", encoding="utf-8") as f:
        metro_stations = json.load(f)
    
    for feature in metro_stations["features"]:
        if feature["geometry"]["type"] == "Point":
            coords = feature["geometry"]["coordinates"]
            station_name = feature["properties"].get("name", "Unnamed Metro Station")

            # Popup Content with Prank Image
            popup_content = f"""
            <b>Metro Station:</b> {station_name}<br>
            <img src='/static/prank.jpg' width='200px' style='border-radius: 10px;'>
            """

            folium.CircleMarker(
                location=[coords[1], coords[0]],
                radius=4,  # Reduced size
                color="darkpurple",
                fill=True,
                fill_color="darkpurple",
                fill_opacity=0.5,  # Reduced opacity by 30%
                popup=folium.Popup(popup_content, max_width=300)
            ).add_to(metro_stations_layer)

    # Add legend and curated by text
    legend_html = '''
    <div style="
        position: fixed;
        bottom: 30px; right: 10px;
        width: 220px; height: auto;
        background-color: white;
        z-index: 9999;
        font-size: 14px;
        border-radius: 8px;
        padding: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    ">
        <strong>Legend:</strong>
        <ul style="list-style-type:none; padding:0; margin:0;">
            <li><span style="background:red; width: 12px; height: 12px; display:inline-block; margin-right:5px;"></span> Bus Stop</li>
            <li><span style="background:darkpurple; width: 12px; height: 12px; display:inline-block; margin-right:5px;"></span> Metro Station</li>
            <li><span style="background:blue; width: 12px; height: 12px; display:inline-block; margin-right:5px;"></span> Delhi Boundary</li>
            <li><span style="background:#87CEEB; width: 12px; height: 12px; display:inline-block; margin-right:5px;"></span> Metro Line</li>
        </ul>
        <hr style="margin: 5px 0;">
        <i style="display:block; text-align:right;">Curated by Daman Dogra</i>
    </div>
    '''
    
    folium_map.get_root().html.add_child(folium.Element(legend_html))

    # Add Layer Control
    folium.LayerControl().add_to(folium_map)

    # Save the map
    folium_map.save('templates/map_base.html')

    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9001)

