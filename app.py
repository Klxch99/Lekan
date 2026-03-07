import os
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import io

df = pd.read_csv("vehicles_us.csv.csv")


st.header("🚗 Used Vehicle Market Explorer")

st.write(
    "This interactive application allows users to explore used vehicle listings "
    "and analyze price distributions and relationships with mileage."
)


show_condition = st.checkbox("Color plots by vehicle condition")


if show_condition:
    fig_hist = px.histogram(
        df,
        x="price",
        color="condition",
        nbins=50,
        title="Vehicle Price Distribution by Condition"
    )
else:
    fig_hist = px.histogram(
        df,
        x="price",
        nbins=50,
        title="Overall Vehicle Price Distribution"
    )

st.plotly_chart(fig_hist, use_container_width=True)


if show_condition:
    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        color="condition",
        opacity=0.6,
        title="Price vs Mileage (Colored by Condition)"
    )
else:
    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        opacity=0.6,
        title="Price vs Mileage"
    )

st.plotly_chart(fig_scatter, use_container_width=True)

