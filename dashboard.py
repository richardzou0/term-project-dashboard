import streamlit as st
import pandas as pd
import altair as alt

# Set page layout
st.set_page_config(layout="wide")

# Load the cleaned data
df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip()

# Filter data for 2023
df_2023 = df[df["Year"] == 2023]
# Sidebar for user input
st.sidebar.header("Filter Options")
selected_state = st.sidebar.selectbox("Select State", df_2023["State"].unique())
selected_category = st.sidebar.selectbox("Select Category", df_2023["Category"].unique())

filtered_df = df_2023[
    (df_2023["State"] == selected_state) & 
    (df_2023["Category"] == selected_category)
]
                

st.title("Health Indicators Dashboard")
st.subheader(f"Data for {selected_state} - {selected_category} (2023)")
st.write(filtered_df)


if not filtered_df.empty:
    chart = alt.Chart(filtered_df).mark_bar().encode(
        x=alt.X("Indicator", sort=None, axis=alt.Axis(labelAngle=-45)),
        y=alt.Y("Value (%)", axis=alt.Axis(title="Percentage")),
        color="Indicator",
        tooltip=["Indicator", "Value (%)"]
    ).properties(
        title=f"{selected_category} Indicators for {selected_state} (2023)"
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.write("No data available for the selected filters.")

st.subheader("Comparison of Selected States")
selected_states = st.sidebar.multiselect(
    "Select States for Comparison",
    options=df_2023["State"].unique(),
    default=["California", "Texas", "Florida", "New York", "Illinois"]
)
if selected_states:
    comparison_df = df_2023[df_2023["State"].isin(selected_states)]
    
    comparison_chart = alt.Chart(comparison_df).mark_bar().encode(
        x=alt.X("Indicator", sort=None),
        y=alt.Y("Value (%)", axis=alt.Axis(title="Percentage")),
        color="State",
        column="State",
        tooltip=["State", "Indicator", "Value (%)"]
    ).properties(
        title="Comparison of Health Indicators Across Selected States (2023)"
    )

    st.altair_chart(comparison_chart, use_container_width=True)
else:
    st.write("Please select states to compare their health indicators.")