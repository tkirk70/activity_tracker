import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Data Construction",
    page_icon=":construction:",
    layout="centered",
    initial_sidebar_state="auto",
    # menu_items={
    #     'Get help': 'https://tcg3pl.sharepoint.com/SitePages/Activity-Tracker.aspx',
    #     'Report a bug': "https://tcg3pl.sharepoint.com/",
    #     'About': "This app is a collection of warehouse hours broken down by customer and activity"
    # }
)

st.title('Page Two is under construction.')


# adjust sidebar width - looks like there is a minimum but this worked and the menu can not be expanded or contracted.
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

df=pd.read_excel('./ActivityTracker.xlsx')

st.sidebar.header("Filter By:")

employee_filter = st.sidebar.multiselect("Filter by Employee:",
                                  options=df['Employee'].unique(),
                                  default=None)
customer_filter = st.sidebar.multiselect("Filter by Customer:",
                                  options=df['Customer'].unique(),
                                  default=None)

# Apply filters
if customer_filter and employee_filter:
    selection_query = df.query(
        "Employee in @employee_filter and Customer in @customer_filter"
    )
elif customer_filter:
    selection_query = df.query(
        "Customer in @customer_filter"
    )
else:
    selection_query = df.query(
        "Employee in @employee_filter"
    )    

st.dataframe(selection_query)