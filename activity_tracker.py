# import dependencies
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
# image = 'pics/1611005178271.jpg'
image = 'pics/tcg_continuum_llc_cover.jfif'
st.image(image, use_column_width='auto', clamp=False, channels="RGB", output_format="auto")
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

# Format the Date column
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')  # Change the format as needed

# Format the Duration column to two decimal places
df['Duration'] = df['Duration'].round(2)

# Set the float format for no decimals
pd.options.display.float_format = '{:.0f}'.format

# Center the dataframe
st.markdown('<div class="centered-dataframe">', unsafe_allow_html=True)
st.dataframe(data=df, width=None, height=None, use_container_width=True, hide_index=None, column_order=None, column_config=None, key=None, on_select="ignore", selection_mode="multi-row")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()  # 👈 Draws a horizontal rule

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
        'yanchor': 'top',
        'font' : {
            'size' : 29
        }
    },
    annotations=[
        dict(
            text="Click on the customer or activity.  Hover over the data points.",
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

