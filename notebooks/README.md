# 📓 Jupyter Notebooks – Solar Challenge Week 0

This folder contains all exploratory and analytical notebooks created during the 10 Academy Week 0 Challenge. Each notebook focuses on profiling, cleaning, and analyzing solar irradiance data for a specific West African country or comparing them across regions.

---

## 🗂️ Notebooks

### 📍 `benin_eda.ipynb`
Exploratory Data Analysis (EDA) for Benin (Malanville) solar dataset:
- Summary statistics and missing value handling
- Outlier detection using Z-scores
- Time series plots for GHI, DNI, DHI, Tamb
- Cleaning impact analysis (ModA/ModB)
- Correlation and distribution plots

### 📍 `sierraleone_eda.ipynb`
EDA for Sierra Leone (Bumbuna) solar dataset:
- Same structure as Benin analysis
- Wind rose, bubble charts, and histogram exploration

### 📍 `togo_eda.ipynb`
EDA for Togo (Dapaong) solar dataset:
- Full end-to-end cleaning and visualization
- Includes insights into humidity, wind, and temperature interactions

### 📍 `compare_countries.ipynb`
Cross-country comparison notebook:
- Combines cleaned data from Benin, Sierra Leone, and Togo
- Side-by-side boxplots for GHI, DNI, DHI
- Summary statistics table (mean, median, std)
- Optional ANOVA test for statistical significance
- Key insights and a final ranking bar chart by average GHI

---

## 📌 Notes

- All datasets are loaded from the `../data/` folder (excluded via `.gitignore`)
- Each notebook includes markdown cells summarizing key insights
- Cleaned datasets were saved as `*_clean.csv` files for reuse

---

## 🚀 Next Step

See the `app/` directory for the Streamlit dashboard (bonus task).

