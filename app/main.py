import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, get_summary

# Page config
st.set_page_config(page_title="West Africa Solar Dashboard", layout="wide")

# Custom theme setup (optional via settings or Streamlit config)
st.markdown(
    """
    <style>
    .main { background-color: #f8f9fa; }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    .stMarkdown h1, .stMarkdown h2 {
        color: #1e3d59;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load and prepare data
df = load_data()
countries = df['Country'].unique().tolist()

# --- Header ---
st.title("☀️ West Africa Solar Energy Dashboard")
st.markdown("Explore and compare solar irradiance potential in **Benin**, **Sierra Leone**, and **Togo** using cleaned data.")

st.markdown("---")

# --- Sidebar Filters ---
with st.sidebar:
    st.header("🔍 Filter")
    selected_countries = st.multiselect("Select countries", countries, default=countries)
    selected_metric = st.selectbox("Select solar metric", ['GHI', 'DNI', 'DHI'])

filtered_df = df[df['Country'].isin(selected_countries)]

# --- KPI Display ---
st.subheader("📊 Key Solar Statistics")

summary_df = get_summary(filtered_df)

kpi_cols = st.columns(len(selected_countries))

for i, country in enumerate(selected_countries):
    avg_ghi = summary_df.loc[country, ('GHI', 'mean')]
    kpi_cols[i].metric(label=f"{country}", value=f"{avg_ghi:.1f} W/m²", delta="Avg GHI")

st.markdown("---")

# --- Boxplot ---
st.subheader(f"📦 Distribution of {selected_metric} by Country")

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=filtered_df, x='Country', y=selected_metric, palette='Set2', ax=ax1)
ax1.set_title(f'{selected_metric} Distribution by Country')
ax1.set_ylabel(f"{selected_metric} (W/m²)")
st.pyplot(fig1)

# --- Summary Table ---
st.subheader("📋 Summary Statistics Table")
st.dataframe(summary_df)

# --- GHI Ranking ---
st.subheader("🏆 Country Ranking by Average GHI")

avg_ghi = filtered_df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
fig2, ax2 = plt.subplots(figsize=(8, 5))
avg_ghi.plot(kind='barh', color='#3e9b9f', ax=ax2)
ax2.set_xlabel("Average GHI (W/m²)")
ax2.set_title("Average GHI Ranking")
st.pyplot(fig2)

st.markdown("---")
st.caption("📌 Data source: 10 Academy Week 0 Challenge — Cleaned datasets from Benin, Sierra Leone, and Togo.")
