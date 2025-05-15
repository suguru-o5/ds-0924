import streamlit as st
import pandas as pd
import plotly.express as px

# Read csv
data = pd.read_csv('real_estate_listings.csv')

st.title('Real Estate Price Analysis Dashboard')

if st.checkbox("Display the data frame") :
    st.dataframe(data)

# Filter
st.sidebar.header("🔧 Filter")
price_range = st.sidebar.slider(
    "Price（USD）", 
    int(data['Price'].min()), 
    int(data['Price'].max()), 
    (int(data['Price'].min()), int(data['Price'].max()))
)
filtered_data = data[
    (data['Price'] >= price_range[0]) & 
    (data['Price'] <= price_range[1])
]

# Histogram
st.subheader("📊 Histogram")
fig_hist = px.histogram(filtered_data, x='Price', nbins=10, title="Price Histogram")
st.plotly_chart(fig_hist)

# Scatter plot
st.subheader("📈 SquareFeet vs Price")
fig_scatter = px.scatter(
    filtered_data, x='SquareFeet', y='Price', 
    hover_name='Address',
    size='Bedrooms',
    color='Bathrooms',
    labels={'SquareFeet': 'SquareFeet', 'Price': 'Price（USD）'},
    title="SquareFeet vs Price"
)
st.plotly_chart(fig_scatter)

# Location
st.subheader("🗺️ Location")
fig_map = px.scatter_mapbox(
    filtered_data,
    lat="Latitude",
    lon="Longitude",
    hover_name="Address",
    hover_data=["Price", "Bedrooms", "Bathrooms"],
    color="Price",
    size="Price",
    size_max=20,
    zoom=11,
    height=400
)
fig_map.update_layout(mapbox_style="open-street-map")
fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig_map)

# Insights
st.subheader("📝 Insights")
st.markdown("""
#### Price Distribution
- Most listings are concentrated in two ranges: **\$250k–\$300k** and **above $800k**.
- There is a relative scarcity of mid-priced properties, suggesting a **bipolar market**.

#### SquareFeet vs Price
- A general **positive correlation** is observed between square footage and price.
- Some smaller properties are priced highly, implying **location or premium renovations**.

#### Location Map
- **Higher-priced properties** tend to be located near the **downtown core**.
- **Lower-priced properties** are more common in **suburban or outlying areas**, possibly reflecting older homes or larger lots.

---
These insights suggest that **location and property features beyond size** (like condition or amenities) strongly influence price, and the market targets both entry-level and luxury buyers.
""")