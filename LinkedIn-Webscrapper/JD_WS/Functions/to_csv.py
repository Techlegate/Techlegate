import pandas

def to_csv(dict):
    df = pandas.DataFrame(dict)
    df.to_csv('Assets/Details.csv')