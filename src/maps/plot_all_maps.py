import pandas as pd
import requests
import folium   
import io
import os
# Images
from PIL import Image


def get_geojson() -> dict:
    state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
    ).json()

    
    return state_geo

def merge_geojson_perc(state_json, data):
#    state_json.merge
    return 0   
    

    # Filtrar el GeoDataFrame para conservar solo los países que tienen datos en sum_volume
    #gdf_filtered = gdf.merge(sum_volume, left_on='name', right_on='country', how='inner')

def plot_map(state_geo, state_data):
        
    m = folium.Map(location=[48, -102], zoom_start=4)

    folium.Choropleth(
        geo_data=state_geo,
        name="permit",
        data=state_data,
        columns=["code", "permit_perc"],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Permit (%)",
    ).add_to(m)

    folium.Choropleth(
        geo_data=state_geo,
        name="hand_gun",
        data=state_data,
        columns=["code", "handgun_perc"],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Hand_gun (%)",
    ).add_to(m)

    folium.Choropleth(
        geo_data=state_geo,
        name="long_gun",
        data=state_data,
        columns=["code", "longgun_perc"],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="long_gun (%)",
    ).add_to(m)


    folium.LayerControl().add_to(m)

    m.save(os.path.join("output", "map.html"))
    print("Map saved in output/map.html. Open it in your favorite browser to check the results.")

def plot_maps_to_image(state_geo, state_data):
    
    m1 = folium.Map(location=[48, -102], zoom_start=4)

    folium.Choropleth(
        geo_data=state_geo,
        name="permit",
        data=state_data,
        columns=["code", "permit_perc"],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Permit (%)",
    ).add_to(m1)
    
    img_data = m1._to_png(5)
    img = Image.open(io.BytesIO(img_data))
    img.save(os.path.join('output', 'm1.png'))
    print("Permit map saved in output/m1.png")
    
    m2 = folium.Map(location=[48, -102], zoom_start=4)

    folium.Choropleth(
        geo_data=state_geo,
        name="hand_gun",
        data=state_data,
        columns=["code", "handgun_perc"],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="hand_gun (%)",
    ).add_to(m2)
    
    img_data = m2._to_png(5)
    img = Image.open(io.BytesIO(img_data))
    img.save(os.path.join('output', 'm2.png'))
    
    print("Hand gun map saved in output/m2.png")
    
    m3 = folium.Map(location=[48, -102], zoom_start=4)

    folium.Choropleth(
        geo_data=state_geo,
        name="long_gun",
        data=state_data,
        columns=["code", "longgun_perc"],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="long_gun (%)",
    ).add_to(m3)
    
    img_data = m3._to_png(5)
    img = Image.open(io.BytesIO(img_data))
    img.save(os.path.join('output', 'm3.png'))
    
    print("Long gun map saved in output/m3.png")
    

def main_maps(df: pd.DataFrame):
    
    state_geo = get_geojson()


    plot_map(state_geo, df)
    
    plot_maps_to_image(state_geo, df)
