import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
from utils import predict_country_from_usernames
import requests

def read_country_coords_from_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Convert the DataFrame to a dictionary
    country_coords = {row['country_id']: (row['lat'], row['long']) for index, row in df.iterrows()}

    return country_coords
# Function to map country codes to latitude and longitude
def map_coords(country_code):
    # Example coordinates; replace with accurate values
    # Example usage
    file_path = 'country_coords.csv'
    coords = read_country_coords_from_csv(file_path)
   
    return coords.get(country_code, (None, None))


def calculate_probability(df):
    # URL of the Nationalize API
    api_url = "https://api.nationalize.io"
    
    # Initialize a list to hold probability results
    probabilities = []
    
    # Process each name in the DataFrame
    for name in df['username']:
        # API request for each name
        response = requests.get(api_url, params={'name': name})
        data = response.json()
        print(data)
        # Calculate the highest probability nationality (if available)
        if data['country']:
            # Sort countries by probability and select the highest
            max_prob = max(data['country'], key=lambda x: x['probability'])
            probabilities.append(max_prob['probability'] * 100)  # Scale probability to 0-100
        else:
            probabilities.append(0)  # Set probability to 0 if no data available

    # Add probabilities to the DataFrame
    df['probability'] = probabilities
    return df

# File uploader allows user to add their own CSV
uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file is not None:
    predict_country_from_usernames(uploaded_file.name,'output.csv')
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv('output.csv')
data = calculate_probability(dataframe)

# Load data directly for demonstration

# Map the country codes to coordinates
data[['lat', 'lon']] = data['country_id'].apply(lambda x: pd.Series(map_coords(x)))

# Streamlit interface
st.title('Instagram Username Nationality Predictor')
st.write(data)

# Prepare map data
map_data = data.dropna(subset=['lat', 'lon'])
 # Ensure there are no NaN values
print(map_data)
# PyDeck chart
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=30,  # Central latitude for the initial view
        longitude=100,  # Central longitude for the initial view
        zoom=1,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            'HeatmapLayer',
            data=map_data,
            get_position=['lon', 'lat'],
            get_weight='probability',
            radius_pixels=60,
            intensity=5,
            color_range=[
                [255, 255, 204],
                [255, 237, 160],
                [254, 217, 118],
                [254, 178, 76],
                [253, 141, 60],
                [252, 78, 42],
                [227, 26, 28],
                [177, 0, 38],
                [128, 0, 38]
            ],
            threshold=0.5,
            opacity=0.8
        )
    ]
))
