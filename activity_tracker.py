# import dependencies
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='centered')
# image = 'pics/1611005178271.jpg'
image = 'pics/tcg_continuum_llc_cover.jfif'
st.image(image, use_column_width='auto', clamp=False, channels="RGB", output_format="auto")
st.title('Activity Tracker - October 2024')
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
# Customize the hover text
# Customize the hover text
fig.update_traces(hovertemplate='<b>%{parent}</b><br><b>%{label}</b><br>Hours: %{value:.2f}')

# Add title and subtitle
fig.update_layout(
    title={
        'text': "Employee Labor Hours by Customer and Activity",
        'y':0.99,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    annotations=[
        dict(
            text="Click on the customers and/or activity for more detailed view.  Hover over the data points.",
            x=0.5,
            y=0.99,
            showarrow=False,
            xanchor='center',
            yanchor='top'
        )
    ]
)


fig.show()
st.plotly_chart(fig)

# Custom CSS style for the text
custom_style = '<div style="text-align: right; font-size: 20px;">✨ A TDS Application ✨</div>'

# Render the styled text using st.markdown
st.markdown(custom_style, unsafe_allow_html=True)

# # Alternatively, use HTML and CSS for more control over positioning
# st.markdown(
#     """
#     <style>
#     .center {
#         display: block;
#         margin-left: auto;
#         margin-right: auto;
#         width: 50%;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown(f'<img src="data:image/jpeg;base64,{image}" class="center"/>', unsafe_allow_html=True)

