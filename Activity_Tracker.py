import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    layout='wide',
    page_title='Activity Tracker',
    page_icon=':watch:'
)

# Inject custom CSS to set the width of the sidebar
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 101px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

image = 'pics/tcg_continuum_llc_cover.jfif'
st.image(image, use_container_width=True, clamp=False, channels="RGB", output_format="auto")

# Center the title using HTML and CSS
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-size: 2em;
        margin-top: 0;
    }
    .centered-dataframe {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add the centered title
st.markdown('<h1 class="centered-title">Activity Tracker - October 2024</h1>', unsafe_allow_html=True)

# Read the Excel file into a pandas dataframe
df = pd.read_excel('ActivityTracker.xlsx', sheet_name='TimeSheet')

# Drop column 'Unnamed: 9'
df.drop('Unnamed: 9', axis=1, inplace=True)

# Format the Date column
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')  # Change the format as needed

# Format the Duration column to two decimal places
df['Duration'] = df['Duration'].round(2)

# Set the float format for no decimals
pd.options.display.float_format = '{:.0f}'.format

# Center the dataframe
st.markdown('<div class="centered-dataframe">', unsafe_allow_html=True)
st.dataframe(data=df, width=None, height=None, use_container_width=True, hide_index=True, column_order=None, column_config=None, key=None, on_select="ignore", selection_mode="multi-row")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()  # 👈 Draws a horizontal rule

df = pd.read_excel('ActivityTracker.xlsx', sheet_name='TimeSheet')
df = df.groupby(['Customer', 'Activity', 'Employee'])['Duration'].sum().reset_index()

# Check for NaN values and replace them
df = df.fillna(0)

# Ensure columns are of correct type
df['Customer'] = df['Customer'].astype(str)
df['Activity'] = df['Activity'].astype(str)
df['Employee'] = df['Employee'].astype(str)
df['Duration'] = df['Duration'].astype(float)


# Aggregate data to reduce the number of rows
df_aggregated = df.groupby(['Customer', 'Activity', 'Employee'])['Duration'].sum().reset_index()

fig = px.sunburst(df_aggregated, path=['Customer', 'Activity', 'Employee'], values='Duration', width=1300, height=900)
fig.update_traces(hovertemplate='<b>%{parent}</b><br><b>%{label}</b><br>Hours: %{value:.2f}')


# fig = px.sunburst(sample_df, path=['Customer', 'Activity', 'Employee'], values='Duration', width=1300, height=900)
# fig.update_traces(hovertemplate='<b>%{parent}</b><br><b>%{label}</b><br>Hours: %{value:.2f}')

fig.update_layout(
    title={
        'text': "Employee Labor Hours by Customer and Activity",
        'y':1.00,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font' : {
            'size' : 29
        }
    },
    annotations=[
        dict(
            text="Click on the customer or activity. Hover over the data points.",
            x=0.5,
            y=1.05,
            showarrow=False,
            xanchor='center',
            yanchor='top',
            font=dict(
                size=23
            )
        )
    ]
)

st.plotly_chart(fig)

df = df.groupby(['Customer', 'Activity', 'Employee'])['Duration'].sum().reset_index()

custom_style = '<div style="text-align: right; font-size: 20px;">✨ A TDS Application ✨</div>'
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

