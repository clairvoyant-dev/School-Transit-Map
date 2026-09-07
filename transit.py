import streamlit as st
import pandas as pd

st.title("School & Transit Analysis")

# Read our data
distance = pd.read_csv("Distance.csv")

far_schools = pd.read_csv("FarSchools.csv")

# Show the chart
st.header("Distance to Nearest Transit Station")

st.bar_chart(
    distance,
    x=distance.columns[0],
    y=distance.columns[1],
    horizontal=True
)

# Show the map
st.header("School and Transit Locations")

st.map(
    locations,
    latitude="Latitude",
    longitude="Longitude"
)
