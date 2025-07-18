import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

st.title("Obesity and Physical Activity Dashboard")

df = pd.read_csv("data.csv")

indicator = st.sidebar.selectbox("Select Indicator", df["Indicator"].unique())
states = st.sidebar.multiselect("Select States", df["State"].unique(), default=df["State"].tolist())

filtered_df = df[(df["Indicator"] == indicator) & (df["State"].isin(states))]

chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X("State:N", sort="-y"),
    y="Value (%):Q",
    color="State:N",
    tooltip=["State", "Value (%)"]
).properties(width=700, height=400)

st.altair_chart(chart, use_container_width=True)