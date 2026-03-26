import pandas as pd

def load_iqm(file):
    df = pd.read_csv(file, sep="\t")
    return df