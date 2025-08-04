import pandas as pd
import folium
from folium.plugins import MarkerCluster, HeatMap

# Load and clean data
df = pd.read_csv("../data/sf_crime_data.csv")
df = df.dropna(subset=['Latitude', 'Longitude'])
df = df[df['Incident Date'] >= '2023-01-01']
df_sampled = df.sample(n=1000, random_state=42)  # Adjust n for performance

# Create base map
sf_map = folium.Map(location=[37.77, -122.42], zoom_start=12)

# Clustered markers
marker_cluster = MarkerCluster().add_to(sf_map)
for _, row in df_sampled.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Incident Category']
    ).add_to(marker_cluster)
    


# Save map
sf_map.save("../output/sf_crime_clustered_map.html")

# Optional: HeatMap overlay
heat_data = df_sampled[['Latitude', 'Longitude']].values.tolist()
HeatMap(heat_data, radius=10).add_to(sf_map)
sf_map.save("../output/sf_crime_heatmap.html")
