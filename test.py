import plotly.express as px
import pandas as pd
import streamlit as st

#Import File:
df = pd.read_csv(r'/home/mike/Environments/Streamlit/Data/eCars.csv').query("Model_Year == 2023").query("Fuel_Code in ['ELEC']")#, 'HYBR', 'PHEV'
df = df.groupby(['Manufacturer']).size().reset_index(name='Total')

#Add Slider:
#all_years = df["Model_Year"] #tried: df.Model_Year.unique() and df["Model_Year"] and others
#selected_years = st.slider("Model_Year", all_years)
#filtered_df = df[df["Model_Year"].isin(selected_years)]

fig = px.pie(filtered_df, values='Total', names='Manufacturer', title="EV Totals 1993 - 2023",)
st.plotly_chart(fig, theme=None)