import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

lat, lon = 4.624335, -74.063644

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=lat,
        longitude=lon,
        zoom=11,
        pitch=50,
    )))