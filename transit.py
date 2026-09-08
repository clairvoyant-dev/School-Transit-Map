import streamlit as st
import pandas as pd

#st.title("School & Transit Analysis")

# Read our data
distance = pd.read_csv("Distance.csv")

far_schools = pd.read_csv("Locations.csv")

#st.bar_chart(
#   distance,
#   x=distance.columns[0],
#   y=distance.columns[1],
#   horizontal=True
#)

# Show the map
#st.header("School and Transit Locations")

import streamlit as st

st.title("Congressional District 35: Public Transit & Schools Analysis")
st.write("This analysis explores public transit accessibility for local schools in our district.")
df = pd.read_csv("Avg of Distance (miles) by School Name.csv")
st.dataframe(df, use_container_width=True)

st.header("1. Overview: Distance of Transit Stations by School")
st.image("Distance of Transit Station by School Name.jpg", caption="Distance of Transit Station by School Name")

st.header("2. Focus Area: Schools More Than 0.5 Miles Away")
st.write("These schools face the greatest distance from public transit options.")
st.image("Schools With Bus Stops More Than 0.5 Miles away by School Name.jpg", caption="Schools with Bus Stops > 0.5 Miles Away")

st.header("3. Geographic Map View")
st.image("School with Bus Stop Map.jpg", caption="Map of Schools (Blue) and Transit Stops (Orange)")
