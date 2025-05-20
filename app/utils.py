import pandas as pd

def load_data():
    df_benin = pd.read_csv("data/benin_clean.csv")
    df_sierraleone = pd.read_csv("data/sierraleone_clean.csv")
    df_togo = pd.read_csv("data/togo_clean.csv")

    df_benin['Country'] = 'Benin'
    df_sierraleone['Country'] = 'Sierra Leone'
    df_togo['Country'] = 'Togo'

    return pd.concat([df_benin, df_sierraleone, df_togo], ignore_index=True)

def get_summary(df):
    return df.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std']).round(2)
