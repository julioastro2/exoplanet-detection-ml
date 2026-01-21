import pandas as pd

def load_exoplanet_data(path):
    return pd.read_csv(
        path,
        sep=",",
        comment="#"
    )