import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.title("Capitales del Mundo")
st.write('Seleccione un país de la lista.')

#df
df = pd.read_csv('data_cap.csv')
cols = list(df.columns)
new_cols = [s.lower() for s in cols]
df.columns = new_cols

# select box
option = st.selectbox('Seleccione un país', df['country'])
capital = df[df.country == option].capital.iloc[0]
lat = df[df.country == option].latitude.iloc[0]
lon = df[df.country == option].longitude.iloc[0]

st.write('Ha seleccionado: ', option)
txt = ', ubicada en Latitud {lat_:.2f}, Longitud {lon_:.2f}.'.format(lat_ = lat, lon_ = lon)
st.write('Su capital es: ', capital, txt)

def find_capital(option):
    country = df[df.country == option]
    map_data = (country[['latitude','longitude']])
    return map_data


st.map(find_capital(option))

