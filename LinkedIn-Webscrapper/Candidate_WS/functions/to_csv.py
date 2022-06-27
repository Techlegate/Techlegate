import pandas as pd

def to_csv(dict):
    df = pd.DataFrame(dict)
    df.to_csv('Details.csv')