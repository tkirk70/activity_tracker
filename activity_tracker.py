# import dependencies
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="center")
image = '/pics/tcg_logo.jpg'
st.image(image, use_column_width='auto', clamp=False, channels="RGB", output_format="auto")
st.title('TCG Activity Tracker - October 2024')
# read the excel file into a pandas datafram while trying to set the float format for NO decimals
df = pd.read_excel('ActivityTracker.xlsx', sheet_name='TimeSheet')
# round to two decimal places in python pandas
pd.options.display.float_format = '{:.0f}'.format
st.dataframe(data=df, width=None, height=None, use_container_width=False, hide_index=None, column_order=None, column_config=None, key=None, on_select="ignore", selection_mode="multi-row")

df = pd.read_excel('ActivityTracker.xlsx', sheet_name='TimeSheet')
df = df.groupby(['Customer', 'Activity', 'Employee'])['Duration'].sum().reset_index()
# round to two decimal places in python pandas
pd.options.display.float_format = '{:.0f}'.format
fig = px.sunburst(df, path=['Customer', 'Activity', 'Employee'], values='Duration', width=1200, height=800)
fig.show()
st.plotly_chart(fig)

# Custom CSS style for the text
custom_style = '<div style="text-align: right; font-size: 20px;">✨ A TDS Application ✨</div>'

# Render the styled text using st.markdown
st.markdown(custom_style, unsafe_allow_html=True)

