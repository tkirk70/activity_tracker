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

# Format the Date column
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')  # Change the format as needed

# Format the Duration column to two decimal places
df['Duration'] = df['Duration'].round(2)

st.sidebar.header("Filter By:")

employee_filter = st.sidebar.selectbox("Filter by Employee:",
                                  options=df['Employee'].unique(),
                                  default=None)
customer_filter = st.sidebar.selectbox("Filter by Customer:",
                                  options=df['Customer'].unique(),
                                  default=None)
activity_filter = st.sidebar.selectbox("Filter by Activity:",
                                  options=df['Activity'].unique(),
                                  default=None)

# Apply filters
if customer_filter and employee_filter and activity_filter:
    selection_query = df.query(
        "Employee in @employee_filter and Customer in @customer_filter and Activity in @activity_filter"
    )
elif customer_filter and employee_filter:
    selection_query = df.query(
        "Customer in @customer_filter and Employee in @employee_filter"
    )
elif employee_filter and activity_filter:
    selection_query = df.query(
        "Employee in @employee_filter and Activity in @activity_filter"
    )
elif customer_filter and activity_filter:
    selection_query = df.query(
        "Customer in @customer_filter and Activity in @activity_filter"
    )
elif customer_filter:
    selection_query = df.query(
        "Customer in @customer_filter"
    )
elif activity_filter:
    selection_query = df.query(
        "Activity in @activity_filter"
    )
elif employee_filter:
    selection_query = df.query(
        "Employee in @employee_filter"
    )
else:
    selection_query=df 

st.dataframe(selection_query)

st.divider()  # 👈 Draws a horizontal rule

total_hours = round((selection_query['Duration'].sum()),2)

st.markdown("### Employee, Customer, Activity:")
if employee_filter:
    employee_filter1 = employee_filter
else:
    employee_filter1 = "All Employees"
if customer_filter:
    customer_filter1 = customer_filter
else:
    customer_filter1 = "All Customers"
if activity_filter:
    activity_filter1 = activity_filter
else:
    activity_filter1 = "All Activities"
    
st.subheader(f'{employee_filter1}, {customer_filter1}, {activity_filter1}')
if total_hours:
    st.subheader(f'Total Hours: {total_hours}')
else:
    total_hours = '0'

# figure out what chart to use here and if we need to groupby the df
fig = px.pie(df, values='Duration', names='Customer', title="Employee Time by Customer", width=800, height=600, hover_data=['Duration'], labels={'Duration': 'Hours'})
fig.update_traces(textposition='inside', textinfo='percent+label', texttemplate='%{label}: %{percent:.0%} (%{value:.0f} hours)')
# Format the hover data
fig.update_traces(hovertemplate='%{label}: %{value:.0f} Hours<extra></extra>')
fig.show()
st.plotly_chart(fig)
# Custom CSS style for the text
custom_style = '<div style="text-align: right; font-size: 20px;">✨ A TDS Application ✨</div>'

# Render the styled text using st.markdown
st.markdown(custom_style, unsafe_allow_html=True)
