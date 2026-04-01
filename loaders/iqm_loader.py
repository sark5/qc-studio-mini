import pandas as pd


def load_iqm(file):
    return pd.read_csv(file, sep="\t")