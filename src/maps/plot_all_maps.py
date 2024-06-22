import pandas as pd
import requests
import folium   
import io
import os
# Images
from PIL import Image


def get_geojson() -> dict:
    """
    Fetches the GeoJSON data for US states from a remote URL.

    Args:
        No input
    Returns:
        dict: The GeoJSON data representing US states.
    """
    
    state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
    ).json()

    
    return state_geo


def plot_map(state_geo, state_data):
    """
    Plots one single map with multiple Choropleth layers for permit, handgun, and long gun data.

    Args:
        state_geo (dict): The GeoJSON data for US states.
        state_data (pd.DataFrame): The DataFrame containing the state data with columns 
                                   'code', 'permit_perc', 'handgun_perc', and 'longgun_perc'.

    Returns:
        None: The function saves the generated map as an HTML file in the output folder.
    """
    
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
    """
    Plots and saves individual maps for permit, handgun, and long gun data as images.

    Args:
        state_geo (dict): The GeoJSON data for US states.
        state_data (pd.DataFrame): The DataFrame containing the state data with columns 
                                   'code', 'permit_perc', 'handgun_perc', and 'longgun_perc'.

    Returns:
        None: The function saves the generated maps as PNG images in the output folder.
    """
    
        
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
    """
    Main function to plot maps and save them as both HTML and PNG images.

    Args:
        df (pd.DataFrame): The DataFrame containing the state data.

    Returns:
        None: The function generates and saves maps.
    """
    
    
    state_geo = get_geojson()


    plot_map(state_geo, df)
    
    plot_maps_to_image(state_geo, df)
